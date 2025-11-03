# 🧭 Travel Schedule Planner Agent (LangGraph Demo)

This repository showcases a simple agent-based travel schedule planner built using [LangGraph](https://github.com/langchain-ai/langgraph). It's designed as a demonstration of LangGraph's capabilities for orchestrating multi-step workflows with modular agents.

> ⚠️ This is a demo project — not intended for production use.

---

## ✨ Features

- 🧠 Agent-based reasoning with LangGraph  
- 🛠️ Modular node structure for planning, formatting, and email generation  
- 📬 Email output simulation  
- 📦 Lightweight and easy to extend  

---

## 📁 Project Structure
```
travel-schedule-planner-agent-langgraph/ ├── src/ # Core logic and utilities │ └── utils_email.py # Email formatting helper ├── test_node/ # Node-level test scripts ├── v2_not_used/ # Archived or experimental code ├── main.ipynb # Jupyter notebook demo ├── pyproject.toml # Dependency configuration └── README.md # Project overview
```


---

## 🚀 Getting Started

### 1. Create and activate a virtual environment

```shell
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
source .venv/Scripts/activate    # Windows
```

### 2. Install dependencies

```shell
pip install uv
uv pip install -r pyproject.toml
```

### Install Graphviz (for pygraphviz)

```shell
pip install pygraphviz --config-settings=--global-option=build_ext \
  --config-settings=--global-option="-IC:\\Program Files\\Graphviz\\include" \
  --config-settings=--global-option="-LC:\\Program Files\\Graphviz\\lib"
```
