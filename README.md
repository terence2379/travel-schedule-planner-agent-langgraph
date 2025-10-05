# travel-schedule-planner-agent-langgraph

```shell
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate
source .venv/Scripts/activate #windows

pip install uv

# Initialize UV and install dependencies
uv init
uv pip install -r pyproject.toml

pip install pygraphviz --config-settings=--global-option=build_ext --config-settings=--global-option="-IC:\Program Files\Graphviz\include" --config-settings=--global-option="-LC:\Program Files\Graphviz\lib"

# test src functions, eg.
python -m src.utils_email
```