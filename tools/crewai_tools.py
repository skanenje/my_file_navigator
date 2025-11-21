# tools/crewai_tools.py
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from .read_file import read_file as _read_file
from .write_file import write_file as _write_file
from .run_shell import run_shell as _run_shell
from .search_project import search_in_project as _search_project
from .explain_code import explain_code as _explain_code
from .git_operations import git_status as _git_status, git_safe_command as _git_safe_command
from .test_generation import generate_tests as _generate_tests
from .debug_assistant import analyze_error as _analyze_error, run_diagnostics as _run_diagnostics

class ReadFileInput(BaseModel):
    path: str = Field(description="Path to the file to read")

class WriteFileInput(BaseModel):
    path: str = Field(description="Path to the file to write")
    content: str = Field(description="Content to write to the file")

class RunShellInput(BaseModel):
    command: str = Field(description="Shell command to execute")

class SearchProjectInput(BaseModel):
    query: str = Field(description="Search query to find files in the project")

class ExplainCodeInput(BaseModel):
    path: str = Field(default=None, description="Path to file to explain")
    code_snippet: str = Field(default=None, description="Code snippet to explain")

class GitSafeCommandInput(BaseModel):
    command: str = Field(description="Safe git command to execute")

class GenerateTestsInput(BaseModel):
    file_path: str = Field(description="Path to file to generate tests for")
    test_framework: str = Field(default="pytest", description="Test framework (pytest/unittest)")

class AnalyzeErrorInput(BaseModel):
    error_message: str = Field(description="Error message to analyze")
    file_path: str = Field(default=None, description="Optional file path related to error")

class RunDiagnosticsInput(BaseModel):
    file_path: str = Field(description="Path to file to run diagnostics on")

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

class ExplainCodeTool(BaseTool):
    name: str = "explain_code"
    description: str = "Explain code from file or snippet"
    args_schema: Type[BaseModel] = ExplainCodeInput

    def _run(self, path: str = None, code_snippet: str = None) -> str:
        result = _explain_code(path=path, code_snippet=code_snippet)
        return str(result)

class GitStatusTool(BaseTool):
    name: str = "git_status"
    description: str = "Get git repository status"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self) -> str:
        result = _git_status()
        return str(result)

class GitSafeCommandTool(BaseTool):
    name: str = "git_safe_command"
    description: str = "Execute safe git commands (read-only)"
    args_schema: Type[BaseModel] = GitSafeCommandInput

    def _run(self, command: str) -> str:
        result = _git_safe_command(command)
        return str(result)

class GenerateTestsTool(BaseTool):
    name: str = "generate_tests"
    description: str = "Generate test templates for a file"
    args_schema: Type[BaseModel] = GenerateTestsInput

    def _run(self, file_path: str, test_framework: str = "pytest") -> str:
        result = _generate_tests(file_path, test_framework)
        return str(result)

class AnalyzeErrorTool(BaseTool):
    name: str = "analyze_error"
    description: str = "Analyze error messages and provide debugging help"
    args_schema: Type[BaseModel] = AnalyzeErrorInput

    def _run(self, error_message: str, file_path: str = None) -> str:
        result = _analyze_error(error_message, file_path)
        return str(result)

class RunDiagnosticsTool(BaseTool):
    name: str = "run_diagnostics"
    description: str = "Run diagnostics on a file"
    args_schema: Type[BaseModel] = RunDiagnosticsInput

    def _run(self, file_path: str) -> str:
        result = _run_diagnostics(file_path)
        return str(result)