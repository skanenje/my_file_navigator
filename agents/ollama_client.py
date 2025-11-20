# agents/ollama_client.py
import subprocess, shlex, json, os, tempfile
from typing import Optional

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")  # change to your model name

def call_ollama(prompt: str, model: Optional[str] = None, max_tokens: int = 1024) -> str:
    model = model or OLLAMA_MODEL
    # The exact CLI may vary. This uses a simple pattern that should work on many setups:
    # ollama run <model> --prompt "<prompt>" --json
    # If your ollama supports `--json` output, prefer that. Otherwise parse stdout.
    try:
        cmd = f'ollama run {shlex.quote(model)} --prompt {shlex.quote(prompt)}'
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        return proc.stdout.strip()
    except Exception as e:
        return f"ERROR_CALLING_OLLAMA: {e}"
