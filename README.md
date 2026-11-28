# Autonomous-Racing-in-Trackmania-via-Deep-Reinforcement-Learning---WIDS
### Winter in Data Science (WIDS) — Mentorship Project

## 1. Introduction

What does it take for a machine to learn how to drive?

Racing is a complex control problem involving continuous decision-making, spatial awareness, speed management, and rapid adaptation to changing situations. A successful driver must anticipate turns, maintain control at high speeds, and make precise adjustments to steering, acceleration, and braking.

In this project, we explore these challenges through **Trackmania**, a racing game that provides an interactive environment for studying autonomous driving and reinforcement learning.

Our goal is to develop an autonomous racing agent using **Deep Reinforcement Learning (DRL)**. Instead of explicitly programming every driving decision, we aim to train an agent that learns effective driving strategies through repeated interaction with the environment, feedback, and experimentation.

The project combines theoretical understanding of Reinforcement Learning with practical implementation, ultimately working towards an AI agent capable of competing against manually designed driving strategies.

---

## 2. The Problem

Traditional rule-based controllers rely on predefined instructions to determine how a vehicle should behave in different situations.

However, racing involves numerous interconnected decisions:

- When should the vehicle accelerate or brake?
- How should steering change when approaching a sharp turn?
- How can the agent maintain speed without sacrificing stability?
- How should it recover from mistakes?
- Can it learn to navigate tracks it has never encountered before?

These questions make autonomous racing an interesting application of Reinforcement Learning.

We aim to investigate whether an agent can learn these behaviours through experience rather than relying entirely on manually defined driving rules.

---

## 3. Why Trackmania?

Trackmania offers an engaging environment for experimenting with autonomous control.

Its racing mechanics introduce several challenges relevant to reinforcement learning:

- **High-speed decision-making:** Actions must be selected while the vehicle is moving rapidly.
- **Spatial awareness:** The agent must understand its position, orientation, and relationship with the track.
- **Control precision:** Steering, acceleration, and braking must be balanced.
- **Dynamic decision-making:** The effectiveness of an action depends on the current driving situation.
- **Generalization:** A robust agent should ideally perform well beyond the specific track configurations encountered during training.

These characteristics make Trackmania a useful sandbox for exploring the principles of autonomous driving and sequential decision-making.

---

## 4. Core Concepts Explored

The project will progressively introduce and apply concepts from Reinforcement Learning, Deep Learning, and control systems.

### Reinforcement Learning Fundamentals

Understanding how an agent learns by interacting with an environment.

- Markov Decision Processes (MDPs)
- States, actions, rewards, and transitions
- Policies and value functions
- Exploration versus exploitation
- Q-learning and temporal difference learning

### Deep Reinforcement Learning

Understanding how neural networks can approximate policies and value functions in complex environments.

- Neural networks as function approximators
- Deep Q-Networks (DQN)
- Policy Gradient methods
- Actor-Critic architectures
- Proximal Policy Optimization (PPO)
- Continuous control and action spaces

### Reward Engineering

Designing a reward function that encourages meaningful driving behaviour.

Potential reward considerations include:

- Progress along the track
- Lap completion
- Speed and efficiency
- Stability and control
- Collisions, resets, and undesirable driving behaviour

### Autonomous Control

Understanding how an agent translates observations into driving decisions.

- Vehicle state representation
- Steering and throttle control
- Braking and speed regulation
- Spatial and trajectory awareness
- Action selection and control frequency

---

## 5. Proposed Approach

The project will follow an iterative approach, gradually moving from theoretical foundations to a functioning autonomous racing agent.

**Step 1 — Understanding Reinforcement Learning**

Establish the mathematical and conceptual foundations required to formulate racing as a sequential decision-making problem.

**Step 2 — Environment Exploration**

Investigate how Trackmania can be interfaced with an external agent, including the mechanisms available for extracting observations and executing controls.

**Step 3 — Problem Formulation**

Define the observation space, action space, reward function, and interaction loop required to model the racing task as an RL environment.

**Step 4 — Baseline Development**

Develop a basic rule-based driving controller to establish a benchmark against which learned policies can be evaluated.

**Step 5 — Agent Development and Training**

Implement suitable Deep Reinforcement Learning approaches and train an agent through repeated interaction with the environment.

**Step 6 — Evaluation and Experimentation**

Analyze the agent's performance, compare it against baseline controllers, identify weaknesses, and investigate its ability to generalize to unfamiliar tracks.

The exact algorithms, observation representations, and implementation choices will be determined through experimentation.

---

## 6. The Learning Loop

At the heart of the project is the Reinforcement Learning interaction cycle.

The autonomous driver continuously interacts with Trackmania:

1. **Observe:** Receive information about the current driving situation.
2. **Interpret:** Process the observation to understand the current state.
3. **Act:** Select steering, acceleration, and braking actions.
4. **Interact:** Execute the selected actions in the game.
5. **Receive Feedback:** Obtain rewards based on the resulting behaviour.
6. **Learn:** Improve the driving policy using accumulated experience.

This cycle repeats throughout training, allowing the agent to progressively discover more effective driving strategies.

**Conceptual Pipeline:**

Trackmania Environment → State Observation → RL Agent → Driving Actions → Environment Feedback → Policy Learning

---

## 7. Evaluation and Performance

The effectiveness of the learned agent will be evaluated using measurable performance indicators.

| Metric | What it measures |
|---|---|
| Lap Time | Overall racing speed |
| Completion Rate | Ability to successfully finish tracks |
| Average Speed | Efficiency of driving |
| Crashes and Resets | Stability and reliability |
| Driving Consistency | Repeatability across attempts |
| Generalization | Performance on previously unseen tracks |

A key objective is to compare the learned agent with rule-based driving strategies.

We also aim to investigate whether training on particular tracks limits the agent's performance when introduced to unfamiliar track layouts or surfaces.

---

## 8. Expected Outcomes

By the conclusion of the project, we aim to achieve:

- A practical understanding of Reinforcement Learning and Deep Reinforcement Learning.
- An interface connecting Trackmania with an external learning agent.
- A formulated RL environment for autonomous racing.
- A functioning rule-based baseline controller.
- An implemented and trained DRL agent.
- Experimental comparisons between learned and manually designed driving strategies.
- An evaluation of the agent's driving performance and generalization capabilities.
- Documentation of experiments, observations, challenges, and limitations.

These are intended outcomes rather than claims of completed implementation.

---

## 9. Learning Resources and Implementation

This repository will serve as both a learning resource and the central development space for the project.

It will document the theoretical concepts, implementation experiments, algorithmic explorations, and practical challenges encountered throughout the mentorship.

The emphasis is on understanding the underlying principles rather than simply using pre-existing implementations as black boxes.

The repository will evolve as the project progresses, incorporating relevant learning material, code, experiments, and findings.

---

**From understanding how machines learn to teaching one how to race.**
