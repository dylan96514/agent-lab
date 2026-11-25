=== COURSE CHECKPOINT ===
date: 2026-11-25
completed: C00
current: C01, segment 1 (not started)
built so far:
- agent-lab: private GitHub repo (dylan96514/agent-lab) with .gitignore
- labs/c00/hello.py: one model call; system prompt, usage and stop reason printed
- labs/c00/two_calls.py: two separate calls; second does not know the name
- labs/c00/conversation.py: one call, three messages; model knows the name
- jq-course/: clone of JQ's repo, beside agent-lab
can explain:
- a model is a function with no memory and no hands; each call stands alone
- context is everything on the page for one call; the model re-reads all of it
- chat "memory" is the history being resent; cost grows as the history grows
- max_tokens is a hard cut (stop reason max_tokens vs end_turn)
- a system prompt is extra standing text on the page, paid for each call
- how to read a traceback: last line first, then the first line in his own file
shaky:
- call vs model vs message: said "two models" for two calls, and "multiple calls" for one call holding several messages
- who resends the history: reached "the app's code, automatically, every call" only after a prompt
- new today, recheck in passing: inference vs training, function vs variable, argument
setup: MacBook; Python 3.14 from python.org inside agent-lab/.venv (system python3 is 3.9.6, do not use); packages anthropic, openai, httpx; provider Anthropic; ANTHROPIC_API_KEY and AGENT_MODEL=claude-haiku-5-5 in ~/.zshrc; edits files with TextEdit (open -e); no Homebrew; gh has two accounts, dylan96514 active (for Quetta work: gh auth switch --user Quetta-labs); wants full commands for setup steps; remind him to run "cd ~/Documents/agent-lab" and "source .venv/bin/activate" before terminal work
next: C01 segment 1, the hook question "Is ChatGPT an agent?"
=== END CHECKPOINT ===