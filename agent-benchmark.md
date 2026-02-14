# Agent Model Benchmark Plan

## Models to Test
1. gpt-oss:120b-ctx131k (Bob) — 81GB loaded
2. gpt-oss:20b (current minis) — 14GB loaded
3. qwen2.5vl:7b (vision, new) — 6GB
4. qwen2.5:7b (text, pulling) — ~5GB
5. llava:latest (7B vision, old) — 4.7GB
6. phi3:latest (3.8B) — 2.2GB

## Test Categories
### A. Instruction Following (can it do what it's told cleanly?)
- "Reply with only your name and role in one line"
- "Write a 3-bullet status update about your current work"
- "Say NO_REPLY" (test if it leaks reasoning)

### B. Tool Use (can it actually use read/write/exec?)
- "Read /tmp/test.txt and summarize it"
- "Write a file to /tmp/agent-test-output.txt with today's date"
- "Run `uname -a` and report the result"

### C. Collaboration (can it work with shared files?)
- "Read comms/mini-1-status.md and write a response in comms/mini-X-response.md"
- "Check proposals/ and vote on any open proposals"

### D. Reasoning (can it solve problems?)
- "What's 17 * 23 + 456 / 12?"
- "Given these 3 options, which is best and why: [scenario]"
- "Debug this Python code: [broken snippet]"

### E. Vision (qwen2.5vl + llava only)
- Analyze a screenshot
- Read text from an image
- Describe a diagram

## Metrics
- Response quality (1-5)
- Reasoning leaked? (yes/no)
- Tool use success? (yes/no)
- Response time
- Token usage
