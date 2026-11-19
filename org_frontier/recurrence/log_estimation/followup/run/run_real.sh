#!/bin/bash
while [ $(ls ../ev2/*.done|wc -l) -lt 2160 ] && pgrep -f loop2.sh >/dev/null; do sleep 20; done
echo "done files: $(ls ../ev2/*.done|wc -l)"
PYTHONPATH=/workspace/algorithmacy-work/stub:/workspace/algorithmacy-lab PYPHI_WELCOME_OFF=true /workspace/algorithmacy-work/venv/bin/python -u analyze2.py real
