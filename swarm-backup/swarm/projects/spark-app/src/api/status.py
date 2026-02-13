"""
Flask Blueprint that provides agent status endpoint.

This module reads per-agent status files from
`/home/pmello/.openclaw/workspace-swarm/comms/` and augments
them with information about the agent's workspace.

Each status file is expected to contain a JSON object with at least
the keys:

- name: agent name
- model: language model in use
- workspace: path to the agent's workspace directory
- last_activity: ISO formatted timestamp

The endpoint returns a JSON array of these status objects.
"""

import os
import json
import glob
from datetime import datetime
from flask import Blueprint, jsonify

# Base directories
BASE_COMMS_DIR = "/home/pmello/.openclaw/workspace-swarm/comms"
BASE_WORKSPACES_DIR = "/home/pmello/.openclaw/workspace-swarm"

status_bp = Blueprint("status", __name__)

@status_bp.route("/api/status", methods=["GET"])
def get_status():
    """Return a JSON list of all agent statuses.

    Each status entry is merged with the most recent modification
    timestamp found in the agent's workspace directory.  If no
    workspace files exist, the field ``workspace_last_modified`` is
    omitted.
    """
    agents = []

    # Find all *.md files in the comms directory
    for file_path in glob.glob(os.path.join(BASE_COMMS_DIR, "*.md")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Try JSON first, fall back to YAML-like if needed
            try:
                status = json.loads(content)
            except json.JSONDecodeError:
                # Very simple YAML to dict conversion for key: value pairs
                status = {}
                for line in content.splitlines():
                    if ':' in line:
                        k, v = line.split(":", 1)
                        status[k.strip()] = v.strip()
            # Ensure required fields
            if not all(k in status for k in ("name", "model", "workspace")):
                continue

            # Resolve workspace path relative to base workspaces dir
            workspace_path = os.path.join(BASE_WORKSPACES_DIR, status["workspace"])
            status["workspace"] = os.path.abspath(workspace_path)

            # Find most recent file in workspace
            recent_ts = None
            if os.path.isdir(workspace_path):
                for root, _, files in os.walk(workspace_path):
                    for fname in files:
                        fpath = os.path.join(root, fname)
                        try:
                            mtime = os.path.getmtime(fpath)
                        except OSError:
                            continue
                        if recent_ts is None or mtime > recent_ts:
                            recent_ts = mtime
                if recent_ts:
                    status["workspace_last_modified"] = datetime.fromtimestamp(recent_ts).isoformat()

            agents.append(status)
        except Exception:
            # Skip files that cannot be processed
            continue

    return jsonify(agents)

# Ensure the blueprint registers on import
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(status_bp)
    app.run(debug=True)
