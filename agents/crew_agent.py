# agents/crew_agent.py
import os
from crewai import Agent, Task, Crew
from crewai.llm import LLM
from tools.crewai_tools import ReadFileTool, WriteFileTool, RunShellTool, SearchProjectTool, ExplainCodeTool, GitStatusTool, GitSafeCommandTool, GenerateTestsTool, AnalyzeErrorTool, RunDiagnosticsTool, RefactorCodeTool, CreateBackupTool, PlanTaskTool

def create_file_navigator_agent():
    """Create a CrewAI agent for file navigation"""
    llm = LLM(
        model="gemini/gemini-2.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    agent = Agent(
        role="File Navigator",
        goal="Navigate and manipulate files using available tools",
        backstory="You are an expert file system navigator that can read, write, and execute commands.",
        llm=llm,
        tools=[ReadFileTool(), WriteFileTool(), RunShellTool(), SearchProjectTool(), ExplainCodeTool(), GitStatusTool(), GitSafeCommandTool(), GenerateTestsTool(), AnalyzeErrorTool(), RunDiagnosticsTool(), RefactorCodeTool(), CreateBackupTool(), PlanTaskTool()],
        verbose=True
    )
    return agent

def run_crew_task(query: str):
    """Run a task using CrewAI"""
    agent = create_file_navigator_agent()
    
    task = Task(
        description=query,
        agent=agent,
        expected_output="A clear response to the user's request"
    )
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )
    
    result = crew.kickoff()
    return {"status": "ok", "answer": str(result), "history": []}