# agents/agent_loop.py
import json, time
from typing import Dict
from agents.ollama_client import call_ollama
from utils.prompt_templates import AGENT_SYSTEM_PROMPT
from tools.read_file import read_file
from tools.write_file import write_file
from tools.run_shell import run_shell

TOOL_MAP = {
    "read_file": read_file,
    "write_file": write_file,
    "run_shell": run_shell,
}

def parse_llm_line(line: str):
    line = line.strip()
    if line.startswith("TOOL_CALL:"):
        json_part = line[len("TOOL_CALL:"):].strip()
        return ("tool_call", json.loads(json_part))
    if line.startswith("FINAL:"):
        return ("final", line[len("FINAL:"):].strip())
    # fallback: nothing recognized
    return ("unknown", line)

def run_agent_repl(user_input: str, model: str = None, max_iterations: int = 6):
    history = []
    system = AGENT_SYSTEM_PROMPT + "\nUser: " + user_input
    loop_count = 0
    while loop_count < max_iterations:
        loop_count += 1
        prompt = system + "\n\nConversation history:\n" + "\n".join(history) + "\nAssistant:"
        llm_out = call_ollama(prompt, model=model)
        typ, payload = parse_llm_line(llm_out)
        if typ == "final":
            return {"status":"ok", "answer": payload, "history": history}
        elif typ == "tool_call":
            tool_name = payload.get("tool")
            args = payload.get("args", {})
            if tool_name not in TOOL_MAP:
                history.append(f"ERROR: Unknown tool {tool_name}")
                continue
            tool = TOOL_MAP[tool_name]
            # call tool and add to history
            tool_res = tool(**args)
            history.append(f"TOOL_RESULT: {tool_res}")
            # feed tool result back next loop iteration
            continue
        else:
            # unrecognized output — add to history and ask LLM to clarify
            history.append("UNRECOGNIZED_OUTPUT: " + str(payload))
            # break to avoid infinite loops — in practice you'd ask LLM to reformat
            return {"status":"error", "reason":"unrecognized_llm_output", "output": payload, "history": history}
    return {"status":"error", "reason":"max_iterations_exceeded", "history": history}
