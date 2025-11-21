# main.py
import argparse
import os
from dotenv import load_dotenv
from agents.agent_loop import run_agent_repl

load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q", type=str, help="User query for the agent")
    args = parser.parse_args()
    if not args.query:
        args.query = input("Ask the agent: ")
    out = run_agent_repl(args.query)
    print("=== RESULT ===")
    from pprint import pprint
    pprint(out)

if __name__ == "__main__":
    main()
