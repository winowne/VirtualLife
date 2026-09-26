# VirtualLife

**English** | [Русский](README.ru.md)

VirtualLife is an experimental simulation of a small living world, created from scratch in Python.

The current version contains a cell that learns to find food on a grid using a simple Q-learning algorithm.

## How it works

- The world is a `20 x 20` grid.
- The cell and food are placed on the grid.
- The cell receives the distance to the food as its state.
- It can move up, down, left, or right.
- Moving gives a small penalty, hitting a wall gives a larger penalty, and finding food gives a reward.
- After training, the learned behavior is shown in a Matplotlib window.

## Installation

Python 3.14 or newer is required by the project configuration.

```bash
git clone https://github.com/winowne/VirtualLife.git
cd VirtualLife
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with:

```bash
.venv\Scripts\activate
```

### macOS

Install Python with [Homebrew](https://brew.sh/) if it is not already installed:

```bash
brew install python
```

Create and activate the virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Linux

On Debian or Ubuntu, install Python, the virtual environment module, and the Tk backend used by Matplotlib:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-tk
```

Then create the environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

`main.py` runs the project in order:

1. `train.py` trains the Q-table for 3000 episodes.
2. The table is saved to `q_table.pkl`.
3. `demo.py` opens the visualization and runs the trained cell for 200 steps.

The generated `q_table.pkl` file is local training data and is ignored by Git.

## Training Parameters

The main parameters are defined in `src/agent.py`:

| Parameter | Value | Purpose |
| --- | ---: | --- |
| `epsilon` | `1.0` | Probability of choosing a random action at the start of training |
| `gamma` | `0.95` | Importance of future rewards |
| `alpha` | `0.1` | Q-table update speed |

In `train.py`, training runs for `3000` episodes. After each episode, `epsilon` is multiplied by `0.995` and never falls below `0.05`. One episode lasts no more than `200` steps.

To start training from scratch, delete `q_table.pkl` and run `main.py` again.

## Run Individual Parts

Normally, run the whole project:

```bash
python main.py
```

The parts can also be run separately:

```bash
python -m src.train
python -m src.demo
```

Run these commands from the project root with the `src` package path:

```bash
python -m src.train
python -m src.demo
```

Run `src.train` first if the Q-table does not exist or has been deleted. Then run `src.demo` to view the result.

## What Happens During Run

During training, the total reward for each episode is printed to the terminal. The values do not have to increase continuously because the agent still performs random actions.

After training, a visualization window opens:

- dark cells are empty space;
- the white cell is the agent;
- the red cell is food.

To stop the demonstration, close the Matplotlib window or press `Ctrl+C` in the terminal.

## If the Window Does Not Open

On Linux, Matplotlib may require a graphical backend. If the project is running on a server without a graphical interface, the visualization window cannot be opened. Training can still be run separately:

```bash
python -m src.train
```

If the dependencies were not installed in the active virtual environment, install them with:

```bash
python -m pip install -r requirements.txt
```

## Current Limitations

- The agent currently consists of one cell.
- The cell's body is effectively one grid cell long.
- The `hunger` and `health` fields exist in `Cell`, but are not yet used in the reward or state.
- The state only contains the offset to the food and does not include movement history.
- Food appears randomly; there are no obstacles or other organisms yet.
- Training and demonstration start when their files are imported, so `main.py` uses them as sequential stages.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Runs training and visualization in order |
| `src/env.py` | Defines the world, cell, food, movement, rewards, and rendering grid |
| `src/agent.py` | Stores the Q-table and chooses actions |
| `src/train.py` | Trains the agent and saves `q_table.pkl` |
| `src/demo.py` | Displays the trained agent with Matplotlib |

## Status

This is an early experimental project. The environment and learning rules are intentionally simple and will become more complex over time.
