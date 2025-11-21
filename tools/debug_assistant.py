# tools/debug_assistant.py
from .tool_result import ToolResult
from .read_file import read_file
from .run_shell import run_shell

def analyze_error(error_message: str, file_path: str = None) -> ToolResult:
    """Analyze error message and provide debugging assistance"""
    try:
        analysis = {
            "error_message": error_message,
            "error_type": "Unknown",
            "probable_causes": [],
            "fix_suggestions": [],
            "files_to_check": []
        }
        
        # Basic error classification
        if "ImportError" in error_message or "ModuleNotFoundError" in error_message:
            analysis["error_type"] = "Import Error"
            analysis["probable_causes"] = [
                "Missing dependency",
                "Incorrect import path",
                "Module not installed"
            ]
            analysis["fix_suggestions"] = [
                "Check if module is installed: pip list",
                "Verify import path",
                "Install missing dependency"
            ]
        elif "SyntaxError" in error_message:
            analysis["error_type"] = "Syntax Error"
            analysis["probable_causes"] = [
                "Missing parentheses/brackets",
                "Incorrect indentation",
                "Invalid syntax"
            ]
        elif "AttributeError" in error_message:
            analysis["error_type"] = "Attribute Error"
            analysis["probable_causes"] = [
                "Object doesn't have the attribute",
                "Typo in attribute name",
                "Object is None"
            ]
        elif "FileNotFoundError" in error_message:
            analysis["error_type"] = "File Not Found"
            analysis["probable_causes"] = [
                "Incorrect file path",
                "File doesn't exist",
                "Permission issues"
            ]
        
        # If file_path provided, add it to files to check
        if file_path:
            analysis["files_to_check"].append(file_path)
        
        return ToolResult(
            status="ok",
            result=analysis,
            meta={"tool": "analyze_error", "file_path": file_path}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "analyze_error", "file_path": file_path}
        )

def run_diagnostics(file_path: str) -> ToolResult:
    """Run basic diagnostics on a file"""
    try:
        # Check if file exists and is readable
        file_result = read_file(file_path)
        if hasattr(file_result, 'status') and file_result.status != "ok":
            return file_result
        
        # Run basic syntax check for Python files
        if file_path.endswith('.py'):
            syntax_check = run_shell(f"python -m py_compile {file_path}")
            return ToolResult(
                status="ok",
                result={
                    "file_path": file_path,
                    "syntax_check": syntax_check.to_dict() if hasattr(syntax_check, 'to_dict') else syntax_check,
                    "file_readable": True
                },
                meta={"tool": "run_diagnostics", "file_path": file_path}
            )
        
        return ToolResult(
            status="ok",
            result={"file_path": file_path, "file_readable": True},
            meta={"tool": "run_diagnostics", "file_path": file_path}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "run_diagnostics", "file_path": file_path}
        )