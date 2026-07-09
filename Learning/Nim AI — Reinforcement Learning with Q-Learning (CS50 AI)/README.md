# Nim AI — Reinforcement Learning with Q-Learning (CS50 AI)

## Author

**Caroline Mildred Gomes**

---

## Project Overview

This project is part of **CS50's Introduction to Artificial Intelligence with Python**.

The objective of this project is to build an Artificial Intelligence capable of learning how to play the game **Nim** using **Reinforcement Learning**, specifically the **Q-Learning** algorithm.

Unlike traditional programming, where every rule is manually written, this AI improves its gameplay through experience. By repeatedly playing against itself, it gradually discovers which actions increase the probability of winning and which actions should be avoided.

This project introduces one of the fundamental ideas behind modern Machine Learning: **learning through interaction with an environment**.

---

# What is Nim?

Nim is a mathematical strategy game consisting of several piles of objects.

Example initial board:

```
Pile 0 : 1
Pile 1 : 3
Pile 2 : 5
Pile 3 : 7
```

Players alternate turns.

During each turn, a player may remove one or more objects from a single pile.

The player who removes the final object loses the game.

---

# Project Objective

The AI should learn the optimal strategy without being explicitly programmed with game rules.

Instead of hard-coding decisions, the AI:

* Observes the current state
* Chooses an action
* Receives a reward
* Updates its knowledge
* Improves over thousands of games

---

# Reinforcement Learning

This project uses Reinforcement Learning.

The learning cycle is:

```
Current State
      ↓
Choose Action
      ↓
Receive Reward
      ↓
Update Q-Value
      ↓
Improve Strategy
```

Each completed game makes the AI more intelligent.

---

# Q-Learning

The AI stores knowledge in a Q-table.

Each entry represents:

```
(State, Action) → Q-Value
```

The Q-value estimates how beneficial taking a particular action is from a particular game state.

The update rule is:

```
Q(s,a) = Old Q + α × (Reward + Future Reward − Old Q)
```

where:

* **α (alpha)** = Learning rate
* **Reward** = Immediate reward
* **Future Reward** = Best expected future outcome

---

# State Representation

A game state is represented as a list of pile sizes.

Example:

```
[1, 3, 5, 7]
```

Internally, states are converted into tuples to allow them to be used as dictionary keys.

---

# Action Representation

Each action is represented by:

```
(i, j)
```

where:

* **i** = pile index
* **j** = number of objects removed

Example:

```
(3, 2)
```

means removing two objects from pile 3.

---

# Reward System

The reinforcement learning model uses three rewards:

* **+1** → Winning move
* **0** → Intermediate move
* **−1** → Losing move

These rewards allow the AI to gradually estimate the quality of every possible move.

---

# Epsilon-Greedy Strategy

To balance learning and performance, the AI follows the epsilon-greedy strategy.

Most of the time it chooses the highest-valued action.

Occasionally it selects a random action to explore alternative strategies that may prove even better.

---

# Project Structure

```
nim.py
```

Contains:

* Nim game implementation
* Q-learning AI
* Training function
* Human vs AI gameplay

```
play.py
```

Trains the AI and starts an interactive game against the user.

---

# Training Process

The AI plays thousands of games against itself.

For each move it:

1. Observes the current state.
2. Chooses an action.
3. Applies the action.
4. Receives a reward.
5. Updates the Q-value.
6. Repeats until the game finishes.

After enough games, the AI develops a strong strategy entirely through experience.

---

# Key Functions Implemented

### `get_q_value()`

Retrieves the Q-value associated with a `(state, action)` pair.

Returns `0` if the pair has not been encountered before.

### `update_q_value()`

Applies the Q-learning update equation to improve the stored Q-value.

### `best_future_reward()`

Evaluates every possible action from a given state and returns the highest expected future reward.

### `choose_action()`

Selects an action using either:

* Greedy selection (best known action), or
* Epsilon-greedy exploration.

---

# Technologies Used

* Python 3
* Reinforcement Learning
* Q-Learning
* Dictionaries (Q-table)
* Self-play training
* Object-Oriented Programming

---

# Learning Outcomes

Through this project I gained practical experience with:

* Reinforcement Learning
* Q-Learning
* State and action representation
* Reward-based learning
* Epsilon-greedy exploration
* Temporal Difference (TD) learning
* Self-learning game agents
* Artificial Intelligence fundamentals
* Python object-oriented programming

---

# Conclusion

This project demonstrates how an AI can learn optimal decision-making without explicitly programmed strategies.

Instead of relying on predefined rules, the agent continuously improves by interacting with its environment, receiving rewards, and refining its Q-values over thousands of simulated games.

The project serves as an excellent introduction to Reinforcement Learning and provides a strong conceptual foundation for more advanced techniques such as Deep Q-Networks (DQN), policy-gradient methods, and other modern reinforcement learning algorithms.

---

**Author:** Caroline Mildred Gomes
