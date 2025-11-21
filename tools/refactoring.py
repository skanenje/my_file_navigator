# tools/refactoring.py
import os
import shutil
from .tool_result import ToolResult
from .read_file import read_file

def refactor_code(file_path: str, refactor_type: str = "extract_function", backup: bool = True) -> ToolResult:
    """Analyze code for refactoring opportunities"""
    try:
        # Read the original file
        file_result = read_file(file_path)
        if hasattr(file_result, 'status') and file_result.status != "ok":
            return file_result
        
        # Extract code content
        if hasattr(file_result, 'result'):
            original_code = file_result.result.get("text", "")
        else:
            original_code = file_result.get("result", {}).get("text", "")
        
        # Create backup if requested
        backup_path = None
        if backup:
            backup_path = f"{file_path}.backup"
        
        # Analyze refactoring opportunities
        refactor_analysis = {
            "file_path": file_path,
            "original_code": original_code,
            "refactor_type": refactor_type,
            "backup_path": backup_path,
            "suggestions": [],
            "rollback_plan": f"Restore from backup: {backup_path}" if backup_path else "Manual rollback required",
            "trade_offs": []
        }
        
        # Basic refactoring suggestions based on type
        if refactor_type == "extract_function":
            refactor_analysis["suggestions"] = [
                "Look for repeated code blocks that can be extracted into functions",
                "Identify long functions that can be broken down",
                "Find complex expressions that can be simplified"
            ]
            refactor_analysis["trade_offs"] = [
                "Pro: Improved code reusability and readability",
                "Con: Slight increase in function call overhead",
                "Pro: Easier testing and maintenance"
            ]
        elif refactor_type == "rename_variables":
            refactor_analysis["suggestions"] = [
                "Identify unclear variable names",
                "Ensure consistent naming conventions",
                "Replace abbreviations with full names"
            ]
        elif refactor_type == "simplify_conditionals":
            refactor_analysis["suggestions"] = [
                "Look for complex if-else chains",
                "Consider using guard clauses",
                "Simplify boolean expressions"
            ]
        
        return ToolResult(
            status="ok",
            result=refactor_analysis,
            meta={"tool": "refactor_code", "file_path": file_path, "refactor_type": refactor_type}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "refactor_code", "file_path": file_path}
        )

def create_backup(file_path: str) -> ToolResult:
    """Create a backup of a file before refactoring"""
    try:
        if not os.path.exists(file_path):
            return ToolResult(
                status="error",
                error=f"File {file_path} does not exist",
                meta={"tool": "create_backup", "file_path": file_path}
            )
        
        backup_path = f"{file_path}.backup"
        shutil.copy2(file_path, backup_path)
        
        return ToolResult(
            status="ok",
            result={
                "original_file": file_path,
                "backup_file": backup_path,
                "message": f"Backup created at {backup_path}"
            },
            meta={"tool": "create_backup", "file_path": file_path, "backup_path": backup_path}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "create_backup", "file_path": file_path}
        )