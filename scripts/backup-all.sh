#!/bin/bash
MAIN="/home/pmello/.openclaw/workspace"
BACKUP_DIR="$MAIN/swarm-backup"
mkdir -p "$BACKUP_DIR/swarm" "$BACKUP_DIR/mini-agents" "$BACKUP_DIR/bob"

cp -r /home/pmello/.openclaw/workspace-swarm/* "$BACKUP_DIR/swarm/" 2>/dev/null
for i in 1 2 3 4 5 6 7 8; do
  src="/home/pmello/.openclaw/workspace-mini-$i"
  dst="$BACKUP_DIR/mini-agents/mini-$i"
  mkdir -p "$dst/memory" "$dst/tools"
  cp "$src/MEMORY.md" "$src/TOOLS.md" "$src/IDENTITY.md" "$dst/" 2>/dev/null
  cp -r "$src/memory/"* "$dst/memory/" 2>/dev/null
  cp -r "$src/tools/"* "$dst/tools/" 2>/dev/null
done
cp -r /home/pmello/.openclaw/workspace-bob/findings "$BACKUP_DIR/bob/" 2>/dev/null
cp -r /home/pmello/.openclaw/workspace-bob/tasks "$BACKUP_DIR/bob/" 2>/dev/null

cd "$MAIN"
git add -A
git diff --cached --quiet || git commit -m "swarm backup $(date +%Y-%m-%d_%H%M)"
git push
