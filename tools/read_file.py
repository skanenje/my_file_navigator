# tools/read_file.py
import os
import time
from typing import Optional
from .tool_result import ToolResult

DEFAULT_CHUNK_SIZE = 4096  # bytes

def read_file(path: str, start: Optional[int] = None, end: Optional[int] = None) -> ToolResult:
    meta = {"tool": "read_file", "path": path}
    t0 = time.time()
    try:
        if not os.path.exists(path):
            return ToolResult("error", None, {**meta}, {"code": "FILE_NOT_FOUND", "message": f"{path} not found"}).to_dict()
        file_size = os.path.getsize(path)
        if start is None and end is None:
            # read up to DEFAULT_CHUNK_SIZE to avoid huge memory reads; caller should request offsets for bigger files
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read(DEFAULT_CHUNK_SIZE)
            meta.update({"read_bytes": len(content), "file_size": file_size, "start": 0, "end": min(DEFAULT_CHUNK_SIZE, file_size)})
            return ToolResult("ok", {"text": content}, meta).to_dict()
        else:
            start = int(start or 0)
            end = int(end or min(start + DEFAULT_CHUNK_SIZE, file_size))
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                f.seek(start)
                content = f.read(end - start)
            meta.update({"read_bytes": len(content), "file_size": file_size, "start": start, "end": end})
            return ToolResult("ok", {"text": content}, meta).to_dict()
    except PermissionError as e:
        return ToolResult("error", None, meta, {"code":"PERMISSION_DENIED", "message": str(e)}).to_dict()
    except Exception as e:
        return ToolResult("error", None, meta, {"code":"RUNTIME_ERROR", "message": str(e)}).to_dict()
