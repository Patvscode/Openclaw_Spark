#!/usr/bin/env bash
# AI-Scientist Runner — robust wrapper with logging and notifications
# Sends status updates via OpenClaw message tool (Telegram)

set -euo pipefail

REPO="$HOME/.openclaw/workspace-bob/AI-Scientist"
VENV="$REPO/.venv"
LOG_DIR="$HOME/.openclaw/workspace/ai-scientist-logs"
RESULTS_DIR="$REPO/results/nanoGPT"
MODEL="${AI_SCIENTIST_MODEL:-ollama/qwen3-coder}"
NUM_IDEAS="${AI_SCIENTIST_IDEAS:-3}"
EXPERIMENT="${AI_SCIENTIST_EXPERIMENT:-nanoGPT}"

mkdir -p "$LOG_DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$LOG_DIR/run_${TIMESTAMP}.log"
STATUS_FILE="$LOG_DIR/status.json"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

update_status() {
    local state="$1"
    local detail="${2:-}"
    cat > "$STATUS_FILE" <<EOF
{
  "state": "$state",
  "detail": "$detail",
  "model": "$MODEL",
  "experiment": "$EXPERIMENT",
  "started": "$TIMESTAMP",
  "updated": "$(date -Iseconds)",
  "log": "$LOG_FILE",
  "pid": $$
}
EOF
}

log "=== AI-Scientist Runner starting ==="
log "Model: $MODEL | Experiment: $EXPERIMENT | Ideas: $NUM_IDEAS"
log "Log: $LOG_FILE"

update_status "starting" "Initializing"

cd "$REPO"
source "$VENV/bin/activate"

export PYTHONUNBUFFERED=1
export TORCH_CUDA_ARCH_LIST="12.1a"

# Run AI-Scientist
update_status "running" "Generating ideas and running experiments"

python launch_scientist.py \
    --experiment "$EXPERIMENT" \
    --model "$MODEL" \
    --num-ideas "$NUM_IDEAS" \
    --skip-novelty-check \
    --gpus 0 \
    >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    update_status "completed" "All ideas evaluated"
    log "=== Run completed successfully ==="
else
    update_status "failed" "Exit code: $EXIT_CODE"
    log "=== Run failed with exit code $EXIT_CODE ==="
fi

# Count results
RESULT_COUNT=$(find "$RESULTS_DIR" -name "final_info_*.json" -newer "$LOG_FILE" 2>/dev/null | wc -l)
log "New result files: $RESULT_COUNT"

exit $EXIT_CODE
