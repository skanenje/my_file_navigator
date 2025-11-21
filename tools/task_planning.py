# tools/task_planning.py
from .tool_result import ToolResult

def plan_task(user_query: str, available_tools: list = None) -> ToolResult:
    """Create a step-by-step plan for complex tasks"""
    try:
        if available_tools is None:
            available_tools = [
                "read_file", "write_file", "run_shell", "search_in_project",
                "explain_code", "git_status", "git_safe_command", "generate_tests",
                "analyze_error", "run_diagnostics", "refactor_code", "create_backup"
            ]
        
        # Analyze query for task complexity
        task_plan = {
            "user_query": user_query,
            "complexity": "simple",
            "estimated_steps": 1,
            "subtasks": [],
            "recommended_tools": [],
            "execution_order": [],
            "internal_reasoning": ""
        }
        
        # Basic task classification
        query_lower = user_query.lower()
        
        if any(word in query_lower for word in ["refactor", "improve", "optimize"]):
            task_plan.update({
                "complexity": "complex",
                "estimated_steps": 4,
                "subtasks": [
                    "Read and analyze existing code",
                    "Create backup of original file",
                    "Identify refactoring opportunities", 
                    "Apply refactoring with safety checks"
                ],
                "recommended_tools": ["read_file", "create_backup", "refactor_code", "write_file"],
                "execution_order": ["read_file", "create_backup", "refactor_code", "write_file"]
            })
        elif any(word in query_lower for word in ["test", "testing", "unit test"]):
            task_plan.update({
                "complexity": "medium",
                "estimated_steps": 3,
                "subtasks": [
                    "Analyze source code structure",
                    "Generate test template",
                    "Write test file"
                ],
                "recommended_tools": ["read_file", "generate_tests", "write_file"],
                "execution_order": ["read_file", "generate_tests", "write_file"]
            })
        elif any(word in query_lower for word in ["debug", "error", "fix"]):
            task_plan.update({
                "complexity": "medium", 
                "estimated_steps": 3,
                "subtasks": [
                    "Analyze error message",
                    "Run diagnostics on relevant files",
                    "Provide fix suggestions"
                ],
                "recommended_tools": ["analyze_error", "run_diagnostics", "read_file"],
                "execution_order": ["analyze_error", "run_diagnostics", "read_file"]
            })
        elif any(word in query_lower for word in ["search", "find", "locate"]):
            task_plan.update({
                "complexity": "simple",
                "estimated_steps": 2,
                "subtasks": [
                    "Search project for matching files",
                    "Present results to user"
                ],
                "recommended_tools": ["search_in_project"],
                "execution_order": ["search_in_project"]
            })
        
        # Add internal reasoning (hidden from user)
        task_plan["internal_reasoning"] = f"""
        Task Analysis:
        - Query: {user_query}
        - Detected complexity: {task_plan['complexity']}
        - Key actions needed: {', '.join(task_plan['subtasks'])}
        - Tool sequence: {' -> '.join(task_plan['execution_order'])}
        """
        
        return ToolResult(
            status="ok",
            result=task_plan,
            meta={"tool": "plan_task", "query": user_query}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "plan_task", "query": user_query}
        )