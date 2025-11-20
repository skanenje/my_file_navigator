# tools/tool_result.py
from typing import Any, Dict, Optional

class ToolResult:
    def __init__(self, status: str, result: Optional[Any] = None, meta: Optional[Dict] = None, error: Optional[Dict] = None):
        self.status = status  # "ok" or "error"
        self.result = result
        self.meta = meta or {}
        self.error = error

    def to_dict(self):
        return {
            "status": self.status,
            "result": self.result,
            "meta": self.meta,
            "error": self.error,
        }
