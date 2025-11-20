# tools/write_file.py
import os, time
from typing import Optional
from .tool_result import ToolResult

def write_file(path: str, content: str, mode: str = "w") -> dict:
    meta = {"tool": "write_file", "path": path, "mode": mode}
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, mode, encoding="utf-8") as f:
            f.write(content)
        meta.update({"written_bytes": len(content)})
        return ToolResult("ok", {"path": path}, meta).to_dict()
    except Exception as e:
        return ToolResult("error", None, meta, {"code":"RUNTIME_ERROR","message": str(e)}).to_dict()
