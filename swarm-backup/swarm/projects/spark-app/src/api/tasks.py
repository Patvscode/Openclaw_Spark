from flask import Blueprint, request, jsonify, abort

from models import db, Task

# Blueprint for task API
bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@bp.route('/', methods=['GET'])
def get_tasks():
    """Return all tasks as JSON."""
    tasks = Task.query.all()
    # Convert each task to a dictionary
    def to_dict(task):
        return {
            "id": task.id,
            "agent_id": task.agent_id,
            "description": task.description,
            "status": task.status,
        }
    return jsonify([to_dict(t) for t in tasks])

@bp.route('/', methods=['POST'])
def create_task():
    """Create a new task.
    Expected JSON body: {"agent_id": <int>, "description": <str>}
    """
    data = request.get_json() or {}
    agent_id = data.get('agent_id')
    description = data.get('description')
    if agent_id is None or description is None:
        abort(400, description="'agent_id' and 'description' are required")
    task = Task(agent_id=agent_id, description=description)
    db.session.add(task)
    db.session.commit()
    return jsonify({
        "id": task.id,
        "agent_id": task.agent_id,
        "description": task.description,
        "status": task.status,
    }), 201

@bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update task status.
    Expected JSON body: {"status": <str>}
    """
    task = Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    status = data.get('status')
    if status is None:
        abort(400, description="'status' field is required")
    task.status = status
    db.session.commit()
    return jsonify({
        "id": task.id,
        "agent_id": task.agent_id,
        "description": task.description,
        "status": task.status,
    })
