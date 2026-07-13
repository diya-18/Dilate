#  Dilate

> *A computational simulator for subjective time perception.*

Why does an hour disappear when you're deeply focused while five minutes in an exam feel endless?

Dilate is a rule-based cognitive simulator that models how **stress, attention, fatigue, effort, novelty, and emotion** evolve over time and collectively influence our perception of time. Instead of using machine learning, Dilate relies on interpretable mathematical equations, dynamic state updates, and systems simulation to recreate common psychological experiences.

Rather than predicting how the brain works exactly, the project explores how simple computational rules can reproduce familiar human experiences such as **flow**, **panic**, **gaming**, **boredom**, **meditation**, and **exam stress**.

---

# Features

- Dynamic cognitive state simulation
- Rule-based subjective time perception model
- Six built-in cognitive scenarios
  - Flow
  - Gaming
  - Meditation
  - Boredom
  - Exam
  - Panic
- Adjustable simulation duration
- Interactive command-line interface
- Multiple scientific visualizations
- Animated cognitive state evolution
- Phase-space trajectory analysis
- End-to-end testing suite
- Modular architecture for experimentation

---

# Cognitive Variables

Every simulation evolves six internal cognitive variables.

| Variable | Description |
|----------|-------------|
| **Stress** | Mental pressure experienced by the subject. Higher stress generally expands subjective time. |
| **Attention** | Degree of sustained focus. High attention compresses perceived time and produces flow states. |
| **Fatigue** | Mental exhaustion accumulated during the simulation. |
| **Novelty** | Perceived newness of the environment or task. Novel situations often feel longer. |
| **Effort** | Cognitive work required to perform the task. |
| **Emotion** | Emotional intensity (positive or negative). Strong emotions amplify time perception. |

These variables continuously interact throughout the simulation rather than remaining fixed.

---

# Time Distortion

Dilate predicts a **time distortion factor**.

```
Perceived Time = Real Time × Distortion
```

Interpretation:

| Distortion | Meaning |
|------------|---------|
| **< 1.0** | Time feels shorter than reality (Flow, Meditation) |
| **= 1.0** | Time feels approximately normal |
| **> 1.0** | Time feels longer than reality (Exam, Panic, Boredom) |

Example:

```
Real Time      : 300 s
Distortion     : 1.92×

Perceived Time : 576 s
```

---

# Built-in Scenarios

| Scenario | Behaviour |
|----------|-----------|
| **Flow** | Deep concentration with minimal stress. Time appears compressed. |
| **Gaming** | Sustained attention with gradually increasing fatigue. |
| **Meditation** | Calm, emotionally stable, low-stress state. |
| **Boredom** | Low engagement causes time to feel slower. |
| **Exam** | Rising stress, effort and fatigue increase subjective time. |
| **Panic** | High stress and emotional intensity dramatically expand perceived time. |

---

# Visualizations

Dilate provides multiple visualization modes.

## 1. Subjective vs Objective Time

Compares actual elapsed time with the simulated perceived time.

---

## 2. Cognitive State Evolution

Shows how

- Stress
- Attention
- Fatigue
- Novelty
- Effort
- Emotion

change throughout the simulation.

---

## 3. Time Distortion

Displays the evolution of the computed distortion factor during the simulation.

---

## 4. Stress–Attention Phase Space

Plots the trajectory of the cognitive state in Stress–Attention space.

This provides a systems-level view of how different scenarios evolve.

---

# Animation

Dilate can animate the evolution of cognitive variables over time.

The animation displays:

- Stress
- Attention
- Fatigue

against

```
X-axis : Simulation Time (seconds)

Y-axis : Normalized Cognitive State
```

allowing users to observe how the simulated mind evolves throughout the scenario.

---

# Project Structure

```text
Dilate/
│
├── cli.py
├── simulator.py
├── requirements.txt
│
├── core/
│   ├── constants.py
│   ├── dynamics.py
│   ├── model.py
│   ├── scenarios.py
│   └── state.py
│
├── visualization/
│   ├── animation.py
│   └── plotter.py
│
└── tests/
    ├── test_model.py
    ├── test_dynamics.py
    └── test_simulation.py
```

---

# Installation

```bash
git clone <repo-url>

cd Dilate

pip install -r requirements.txt
```

---

# Usage

Run a simulation:

```bash
python cli.py flow
```

Run another scenario:

```bash
python cli.py panic
```

Custom simulation duration:

```bash
python cli.py exam --duration 600
```

---

# Generate Plots

Generate every plot:

```bash
python cli.py flow --plot all
```

Generate individual plots:

```bash
python cli.py flow --plot time
```

```bash
python cli.py flow --plot cognitive
```

```bash
python cli.py flow --plot distortion
```

```bash
python cli.py flow --plot phase
```

Save plots instead of displaying them:

```bash
python cli.py flow --plot all --save
```

---

# Animate

Animate cognitive state evolution:

```bash
python cli.py flow --animate cognitive
```

Works for every scenario:

```bash
python cli.py panic --animate cognitive
```

```bash
python cli.py meditation --animate cognitive
```

---

# Run Tests

Model validation

```bash
python -m tests.test_model
```

Dynamics validation

```bash
python -m tests.test_dynamics
```

Full simulation validation

```bash
python -m tests.test_simulation
```

---

# Disclaimer
**Dilate isn't intended to perfectly model the human brain. It's just an experiment in using simple computational rules to explore aspects of cognition and our subjective experience of time.**
