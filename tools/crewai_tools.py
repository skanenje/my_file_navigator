# tools/crewai_tools.py
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from .read_file import read_file as _read_file
from .write_file import write_file as _write_file
from .run_shell import run_shell as _run_shell
from .search_project import search_in_project as _search_project

class ReadFileInput(BaseModel):
    path: str = Field(description="Path to the file to read")

class WriteFileInput(BaseModel):
    path: str = Field(description="Path to the file to write")
    content: str = Field(description="Content to write to the file")

class RunShellInput(BaseModel):
    command: str = Field(description="Shell command to execute")

class SearchProjectInput(BaseModel):
    query: str = Field(description="Search query to find files in the project")

class ReadFileTool(BaseTool):
    name: str = "read_file"
    description: str = "Read the contents of a file"
    args_schema: Type[BaseModel] = ReadFileInput

    def _run(self, path: str) -> str:
        result = _read_file(path)
        return str(result)

class WriteFileTool(BaseTool):
    name: str = "write_file"
    description: str = "Write content to a file"
    args_schema: Type[BaseModel] = WriteFileInput

    def _run(self, path: str, content: str) -> str:
        result = _write_file(path, content)
        return str(result)

class RunShellTool(BaseTool):
    name: str = "run_shell"
    description: str = "Execute a shell command"
    args_schema: Type[BaseModel] = RunShellInput

    def _run(self, command: str) -> str:
        result = _run_shell(command)
        return str(result)

class SearchProjectTool(BaseTool):
    name: str = "search_in_project"
    description: str = "Search for files in the project matching a query"
    args_schema: Type[BaseModel] = SearchProjectInput

    def _run(self, query: str) -> str:
        result = _search_project(query)
        return str(result)