# main.py
import argparse
import os
from dotenv import load_dotenv
from config import Config

load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q", type=str, help="User query for the agent")
    parser.add_argument("--crew", action="store_true", help="Use CrewAI instead of direct agent")
    args = parser.parse_args()
    
    if not args.query:
        args.query = input("Ask the agent: ")
    
    # Choose between CrewAI and direct agent
    if args.crew or Config.USE_CREWAI:
        from agents.crew_agent import run_crew_task
        out = run_crew_task(args.query)
    else:
        from agents.agent_loop import run_agent_repl
        out = run_agent_repl(args.query)
    
    print("=== RESULT ===")
    from pprint import pprint
    pprint(out)

if __name__ == "__main__":
    main()
