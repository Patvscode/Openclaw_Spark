from flask import Blueprint, request, jsonify, Response
import json
from datetime import datetime

# Import database helpers and constants from models
from models import get_conn, DB_FILE

# Blueprint for training data API
training_bp = Blueprint('training_bp', __name__, url_prefix='/api/training')

# Helper to serialize row to dict
def _row_to_dict(row: tuple) -> dict:
    # columns: id, agent_id, input, output, tools_used, success, quality, created
    return {
        'id': row[0],
        'agent_id': row[1],
        'input': row[2],
        'output': row[3],
        'tools_used': json.loads(row[4]) if row[4] else None,
        'success': bool(row[5]) if row[5] is not None else None,
        'quality': row[6],
        'created': row[7],
    }

@training_bp.route('', methods=['GET'])
def get_training_data():
    """Return all training data entries as JSON."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM training_data')
        rows = cur.fetchall()
    data = [_row_to_dict(r) for r in rows]
    return jsonify(data)

@training_bp.route('', methods=['POST'])
def log_training_data():
    """Log a new training data point.
    Expected JSON payload: {
        "agent_id": int,
        "input": str,
        "output": str,
        "tools_used": list,
        "success": bool,
        "quality": float
    }
    """
    payload = request.get_json(force=True)
    required = ['agent_id', 'input', 'output', 'tools_used', 'success', 'quality']
    if not payload or any(k not in payload for k in required):
        return jsonify({'error': 'Missing required fields'}), 400

    agent_id = payload['agent_id']
    input_text = payload['input']
    output_text = payload['output']
    tools_used = payload['tools_used']
    success = 1 if payload['success'] else 0
    quality = float(payload['quality'])
    created = datetime.utcnow().isoformat()

    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            '''INSERT INTO training_data (agent_id, input, output, tools_used, success, quality, created)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (agent_id, input_text, output_text, json.dumps(tools_used), success, quality, created),
        )
        conn.commit()
        new_id = cur.lastrowid

    return jsonify({'id': new_id, 'status': 'created'}), 201

@training_bp.route('/export', methods=['GET'])
def export_training_data():
    """Export all training data as JSONL suitable for fine‑tuning."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM training_data')
        rows = cur.fetchall()
    # Build JSONL string
    lines = []
    for r in rows:
        record = _row_to_dict(r)
        # Flatten to typical fine‑tune format: input, output, tools_used, success, quality
        lines.append(json.dumps(record))
    content = '\n'.join(lines)
    return Response(content, mimetype='application/jsonl', headers={'Content-Disposition': 'attachment; filename=training_export.jsonl'})
