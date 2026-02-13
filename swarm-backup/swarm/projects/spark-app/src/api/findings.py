from flask import Blueprint, jsonify, request, abort
from pathlib import Path
import os
import datetime

# Blueprint for findings API
findings_bp = Blueprint('findings', __name__)

# Base directories to scan for .md files
BASE_DIRECTORIES = [
    Path("/home/pmello/.openclaw/workspace-bob/findings"),
    Path("/home/pmello/.openclaw/workspace-mini-4"),
]

# Helper to collect all markdown files in the base directories
def _collect_markdown_files():
    files = []
    for base in BASE_DIRECTORIES:
        if base.exists():
            for md in base.rglob("*.md"):
                if md.is_file():
                    files.append(md)
    return files

# Endpoint to list findings
@findings_bp.route('/api/findings', methods=['GET'])
def list_findings():
    files = _collect_markdown_files()
    result = []
    for path in files:
        try:
            content = path.read_text(encoding='utf-8')
        except Exception:
            content = ""
        preview = content[:200]
        stat = path.stat()
        item = {
            "title": path.stem,
            "path": path.as_posix(),
            "agent": path.parent.name,
            "date": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "preview": preview,
        }
        result.append(item)
    return jsonify(result)

# Endpoint to get full content of a finding by path
@findings_bp.route('/api/findings/<path:file_path>', methods=['GET'])
def get_finding(file_path):
    files = _collect_markdown_files()
    # Normalize path to posix string
    requested = Path(file_path).as_posix()
    # Find matching file
    target = None
    for p in files:
        if p.as_posix() == requested:
            target = p
            break
    if target is None:
        abort(404, description="Finding not found")
    try:
        content = target.read_text(encoding='utf-8')
    except Exception as e:
        abort(500, description=str(e))
    return content
