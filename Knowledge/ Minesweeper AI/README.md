# Minesweeper AI

## Overview

This project is part of Harvard University's **CS50's Introduction to Artificial Intelligence with Python**.

The goal of the project is to build an intelligent agent capable of playing the classic Minesweeper game using logical inference rather than guessing whenever possible.

The AI maintains a knowledge base of logical sentences representing information about the game board and continuously updates this knowledge as new safe cells are revealed. Using propositional reasoning and subset inference, the agent identifies cells that are guaranteed to be safe or guaranteed to contain mines.

---

## Problem Statement

In Minesweeper, every revealed cell contains a number indicating how many neighboring cells contain mines.

The challenge is to use this information to determine:

- Which cells are definitely safe.
- Which cells definitely contain mines.
- Which moves require random guessing.

Instead of brute-force searching every board configuration, this project implements a **knowledge-based AI** that reasons using logical constraints.

---

## Features

- Knowledge-based AI agent
- Logical sentence representation
- Automatic inference of safe cells
- Automatic identification of mines
- Subset inference for discovering new knowledge
- Random move selection when no safe move exists
- Interactive graphical interface using Pygame

---

## AI Concepts Used

- Knowledge-Based Agents
- Propositional Logic
- Logical Inference
- Constraint Satisfaction
- Set Operations
- Subset Inference
- Artificial Intelligence Reasoning

---

## Project Structure

```
minesweeper/
│
├── minesweeper.py      # Game logic and AI
├── runner.py           # Graphical interface
├── requirements.txt
└── README.md
```

---

## How the AI Works

The AI stores information as logical sentences of the form:

```
{Cell1, Cell2, Cell3} = Count
```

Example:

```
{A, B, C} = 1
```

This means exactly one of the three cells contains a mine.

The AI continuously:

1. Marks revealed cells as safe.
2. Adds new logical sentences.
3. Updates existing knowledge.
4. Infers additional safe cells.
5. Infers new mines.
6. Creates new knowledge using subset inference.

---

## Algorithms

The AI performs the following reasoning steps:

- Mark safe cells
- Mark mines
- Remove known cells from sentences
- Update mine counts
- Generate new logical sentences
- Apply subset inference repeatedly
- Select safe moves whenever possible
- Make random legal moves if no safe move exists

---

## Skills Demonstrated

- Python Programming
- Object-Oriented Programming
- Artificial Intelligence
- Logical Reasoning
- Knowledge Representation
- Set Manipulation
- Algorithm Design
- Problem Solving

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python runner.py
```

---

## Learning Outcomes

Through this project I learned:

- How knowledge-based AI agents reason
- How logical sentences can represent knowledge
- How inference allows an AI to discover new information
- How subset relationships generate additional knowledge
- How logical reasoning differs from brute-force search

---

## Future Improvements

Possible extensions include:

- Probability-based guessing
- Improved inference techniques
- Performance optimization
- Larger board support
- Advanced constraint propagation

---

## Course

Harvard University

CS50's Introduction to Artificial Intelligence with Python

Project 1 — Minesweeper

---

## Author

**Caroline Mildred Gomes**

GitHub:
https://github.com/carolinemildredgomes-hub
