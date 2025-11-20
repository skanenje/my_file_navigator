# My File Navigator 🧭

[![GitHub Repo stars](https://img.shields.io/github/stars/skanenje/my_file_navigator?style=social)](https://github.com/skanenje/my_file_navigator)

## Overview

**My File Navigator** is an AI-powered file system navigator and manipulator built with Python and Ollama. It allows you to interact with your file system using natural language queries via a REPL interface. The agent can read files, write files, execute shell commands in a sandboxed environment, and more.

Powered by local Ollama models for privacy-focused, offline operation.

## ✨ Features

- **Natural Language Interface**: Ask the agent to navigate, read, edit files, or run commands (e.g., "Read main.py", "List files in agents/", "Write a hello world to test.txt").
- **Tool Integration**: Built-in tools for:
  - File reading (`read_file`)
  - File writing (`write_file`)
  - Shell execution (`run_shell`) in a secure sandbox.
- **REPL Loop**: Interactive chat-like experience with persistent context.
- **Ollama Integration**: Uses local LLMs (e.g., Llama3) for reasoning and tool calls.
- **Sandboxed Execution**: Shell commands run in isolated environments for safety.
- **Prompt Templates**: Optimized prompts for agent behavior.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/skanenje/my_file_navigator.git
   cd my_file_navigator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama**:
   - Install [Ollama](https://ollama.com/) and pull a model (e.g., `ollama pull llama3`).
   - Create `.env` file:
     ```
     OLLAMA_URL=http://localhost:11434
     MODEL=llama3
     ```

4. **Run the agent**:
   ```bash
   python main.py
   ```
   Or with a query:
   ```bash
   python main.py -q "List all Python files"
   ```

## 🚀 Usage

Enter queries in natural language:

```
Ask the agent: Show me the contents of main.py
Agent: [tool call result]
Ask the agent: Create a new file called example.txt with "Hello World"
Agent: [result]
```

The agent maintains conversation history for context-aware responses.

## 🏗️ Architecture

```
my_file_navigator/
├── main.py              # CLI entrypoint
├── agents/
│   ├── agent_loop.py    # Core REPL loop & tool orchestration
│   └── ollama_client.py # Ollama LLM client
├── tools/               # Agent tools
│   ├── read_file.py
│   ├── write_file.py
│   ├── run_shell.py
│   └── tool_result.py
├── utils/
│   ├── prompt_templates.py  # System/user prompts
│   └── sandbox.py           # Secure shell execution
├── requirements.txt
├── .env.example          # (Add this for env vars)
└── README.md
```

- **Agent Loop**: Parses LLM responses for tool calls, executes tools, feeds results back.
- **Tools**: Structured outputs for agent actions.
- **Sandbox**: Isolates shell commands.

## 🤝 Contributing

1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit changes (`git commit -m 'Add amazing feature'`).
4. Push to branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

### Development

- Run tests: `pytest`
- Lint: (Add black/flake8 to requirements if needed)

## 📄 License

MIT License - see [LICENSE](LICENSE) (create if needed).

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/)
- Python community

---

