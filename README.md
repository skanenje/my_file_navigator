# My File Navigator

My File Navigator is an AI-powered file system agent designed to help you navigate, search, and manipulate files in your project using natural language. It supports both a direct agent loop and a CrewAI-based agent for more complex task orchestration.

## Features

- **Natural Language Interface**: Interact with your file system using plain English.
- **Dual Modes**:
    - **Direct Agent**: A lightweight, fast agent loop for quick queries.
    - **CrewAI Agent**: A robust agent based on the CrewAI framework for complex tasks.
- **File Operations**:
    - **Read**: Read file contents.
    - **Write**: Create and edit files.
    - **Search**: Find files by name or pattern within the project.
- **Shell Execution**: Run shell commands directly from the agent.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd my_file_navigator
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Google API Key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```
    (Note: The project uses Gemini models by default).

## Usage

Run the main script to start the agent:

```bash
python main.py
```

### Command Line Arguments

-   `--query`, `-q`: Provide a query directly from the command line.
    ```bash
    python main.py --query "Find all python files in the tools directory"
    ```
-   `--crew`: Use the CrewAI agent instead of the default direct agent.
    ```bash
    python main.py --crew --query "Analyze the project structure and write a summary to summary.md"
    ```

### Examples

**Interactive Mode:**
```bash
python main.py
# Then type your query when prompted:
# Ask the agent: List all files in the current directory
```

**Direct Query:**
```bash
python main.py -q "Read config.py and tell me the default settings"
```
