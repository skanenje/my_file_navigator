# tools/explain_code.py
import json
from .tool_result import ToolResult
from .read_file import read_file

def explain_code(path: str = None, code_snippet: str = None) -> ToolResult:
    """Explain code from file or snippet"""
    try:
        if path:
            # Read code from file
            file_result = read_file(path)
            if hasattr(file_result, 'status') and file_result.status != "ok":
                return file_result
            elif isinstance(file_result, dict) and file_result.get('status') != 'ok':
                return ToolResult(status="error", error=str(file_result), meta={"tool": "explain_code"})
            
            # Extract text from result
            if hasattr(file_result, 'result'):
                code_content = file_result.result.get("text", "")
            else:
                code_content = file_result.get("result", {}).get("text", "")
        elif code_snippet:
            code_content = code_snippet
        else:
            return ToolResult(
                status="error",
                error="Either path or code_snippet must be provided",
                meta={"tool": "explain_code"}
            )
        
        # Return structured format for explanation
        explanation_template = {
            "overview": f"Code analysis for: {path or 'snippet'}",
            "content": code_content,
            "flow": "Analyze the code structure and execution flow",
            "key_parts": ["Identify main components", "Extract important functions/classes"],
            "risks": ["Potential issues or vulnerabilities"],
            "improvements": ["Suggestions for enhancement"]
        }
        
        return ToolResult(
            status="ok",
            result=explanation_template,
            meta={"tool": "explain_code", "path": path, "has_snippet": bool(code_snippet)}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "explain_code", "path": path}
        )