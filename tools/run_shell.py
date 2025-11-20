# tools/run_shell.py
import subprocess, tempfile, time, os
from typing import List
from .tool_result import ToolResult
from utils.sandbox import create_sandbox_workspace

def run_shell(command: str, timeout: int = 30, allowed: List[str] = None) -> dict:
    meta = {"tool": "run_shell", "command": command}
    # Very simple allowlist check to reduce accidental destructive commands in dev.
    destructive_tokens = ["rm ", "sudo", "shutdown", "reboot", "mkfs", "dd ", ":(){ :|: & };:"]
    if allowed is None:
        for t in destructive_tokens:
            if t in command:
                return ToolResult("error", None, meta, {"code":"DISALLOWED_COMMAND","message":"Potentially destructive command blocked."}).to_dict()
    workdir = create_sandbox_workspace()
    try:
        proc = subprocess.run(command, shell=True, cwd=workdir, capture_output=True, text=True, timeout=timeout)
        result = {
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "exit_code": proc.returncode,
            "artifacts": [os.path.join(workdir, f) for f in os.listdir(workdir)],
            "workdir": workdir,
        }
        return ToolResult("ok", result, meta).to_dict()
    except subprocess.TimeoutExpired as e:
        return ToolResult("error", None, meta, {"code":"TIMEOUT","message": str(e)}).to_dict()
    except Exception as e:
        return ToolResult("error", None, meta, {"code":"RUNTIME_ERROR","message": str(e)}).to_dict()
