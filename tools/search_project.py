# tools/search_project.py
import os
import glob
from typing import List, Dict
from .tool_result import ToolResult

def search_in_project(query: str, max_results: int = 10) -> ToolResult:
    """Search for files in the project matching the query"""
    try:
        # Get current working directory
        cwd = os.getcwd()
        
        # Search patterns
        patterns = [
            f"**/*{query}*",
            f"**/*.py",
            f"**/*.js",
            f"**/*.md",
            f"**/*.txt"
        ]
        
        found_files = []
        
        for pattern in patterns:
            matches = glob.glob(os.path.join(cwd, pattern), recursive=True)
            for match in matches:
                if os.path.isfile(match):
                    rel_path = os.path.relpath(match, cwd)
                    if query.lower() in rel_path.lower() or query.lower() in os.path.basename(match).lower():
                        found_files.append({
                            "path": rel_path,
                            "size": os.path.getsize(match),
                            "modified": os.path.getmtime(match)
                        })
        
        # Remove duplicates and sort by relevance
        unique_files = []
        seen_paths = set()
        for file_info in found_files:
            if file_info["path"] not in seen_paths:
                unique_files.append(file_info)
                seen_paths.add(file_info["path"])
        
        # Sort by relevance (exact matches first, then by depth)
        unique_files.sort(key=lambda x: (
            0 if query.lower() in os.path.basename(x["path"]).lower() else 1,
            x["path"].count(os.sep)
        ))
        
        result_files = unique_files[:max_results]
        
        return ToolResult(
            status="ok",
            result={
                "query": query,
                "found_count": len(result_files),
                "files": result_files
            },
            meta={"tool": "search_in_project", "query": query, "max_results": max_results}
        )
        
    except Exception as e:
        return ToolResult(
            status="error",
            error=str(e),
            meta={"tool": "search_in_project", "query": query}
        )