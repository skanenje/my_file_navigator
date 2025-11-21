# tools/git_operations.py
from .tool_result import ToolResult
from .run_shell import run_shell

def git_status() -> ToolResult:
    """Get git repository status"""
    return run_shell("git status --porcelain")

def git_safe_command(command: str) -> ToolResult:
    """Execute safe git commands (read-only operations)"""
    safe_commands = ["status", "log", "diff", "branch", "show", "ls-files"]
    
    cmd_parts = command.split()
    if len(cmd_parts) < 2 or cmd_parts[0] != "git":
        return ToolResult(
            status="error",
            error="Command must start with 'git'",
            meta={"tool": "git_safe_command", "command": command}
        )
    
    git_operation = cmd_parts[1]
    if git_operation not in safe_commands:
        return ToolResult(
            status="error", 
            error=f"Command '{git_operation}' not in safe list: {safe_commands}",
            meta={"tool": "git_safe_command", "command": command}
        )
    
    return run_shell(command)