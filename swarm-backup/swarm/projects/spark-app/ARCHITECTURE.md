# Spark App — Swarm Management & Training Platform

## Vision
A local web dashboard for managing Pat's AI swarm, collecting training data, and eventually fine-tuning models.

## Stack
- **Backend:** Python Flask (simple, everyone knows it)
- **Frontend:** HTML/CSS/JS (vanilla or lightweight framework)
- **Database:** SQLite (local, no setup)
- **Hosting:** Local on DGX Spark, accessible via browser

## Features (MVP)

### 1. Agent Dashboard
- Real-time status of all agents (Spark, Bob, 8 Minis)
- Last activity, current task, memory size
- Health indicators (running/idle/error)

### 2. Task Manager
- Create/assign/track tasks for any agent
- Task queue per agent
- Swarm task distribution (break task → assign to minis → Bob reviews)

### 3. Findings Browser
- Browse all research findings from Bob and Minis
- Search, filter, tag
- Quality ratings (for training data)

### 4. Training Data Collector
- Log every agent interaction (input/output/tools used/success)
- Tag interactions by quality, task type, difficulty
- Export as fine-tuning datasets (JSONL format)
- Track per-agent performance metrics over time

### 5. Agent Chat
- Direct chat interface to any agent
- Voice input/output (via Sesame AI when ready)

### 6. Performance Analytics
- Tokens used per agent per day
- Task completion rates
- Speed benchmarks over time
- Quality scores trending

## Module Assignment (Swarm Build)
| Module | Agent | Files |
|--------|-------|-------|
| Flask app skeleton + routing | Alpha (mini-1) | app.py, config.py |
| Agent status API | Beta (mini-2) | api/status.py |
| Task manager API | Gamma (mini-3) | api/tasks.py |
| Findings browser API | Delta (mini-4) | api/findings.py |
| Training data collector | Echo (mini-5) | api/training.py |
| Frontend dashboard HTML/CSS | Foxtrot (mini-6) | templates/, static/ |
| Frontend JS (dynamic updates) | Golf (mini-7) | static/js/ |
| Database models + setup | Hotel (mini-8) | models.py, db_setup.py |
| **Integration & review** | **Bob** | All files |

## Directory
/home/pmello/.openclaw/workspace-swarm/projects/spark-app/src/
