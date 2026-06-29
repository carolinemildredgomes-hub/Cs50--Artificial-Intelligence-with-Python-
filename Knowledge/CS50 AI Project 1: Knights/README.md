# CS50 AI Project 1: Knights

## Overview

This project is part of Harvard University's CS50's Introduction to Artificial Intelligence with Python. The objective is to solve classic "Knights and Knaves" logic puzzles using propositional logic and model checking instead of manually reasoning through the puzzles.

Each character is either a Knight, who always tells the truth, or a Knave, who always lies. The program constructs a logical knowledge base describing the puzzle and uses an automated model-checking algorithm to determine the identity of each character.

## Objectives

* Learn knowledge representation using propositional logic.
* Build logical knowledge bases for different puzzles.
* Apply logical connectives such as AND, OR, NOT, Implication, and Biconditional.
* Use automated reasoning through model checking.
* Understand how AI systems can infer conclusions from logical rules.

## Features

* Represents logical propositions using Python classes.
* Encodes four Knights and Knaves puzzles.
* Automatically determines whether each character is a Knight or a Knave.
* Uses exhaustive model checking to evaluate every possible logical model.
* Demonstrates fundamental concepts of symbolic Artificial Intelligence.

## Technologies Used

* Python 3
* Propositional Logic
* Model Checking
* Symbolic AI

## Project Structure

```
knights/
│── logic.py        # Logical sentence classes and model checker
│── puzzle.py       # Knowledge bases for the four puzzles
│── README.md
```

## Learning Outcomes

After completing this project, I gained experience with:

* Knowledge representation
* Logical reasoning
* Propositional logic
* AI inference
* Model checking algorithms
* Symbolic Artificial Intelligence

## How to Run

```bash
python puzzle.py
```

## Sample Output

```
Puzzle 0
A is a Knave

Puzzle 1
A is a Knave
B is a Knight

Puzzle 2
A is a Knight
B is a Knave

Puzzle 3
A is a Knight
B is a Knave
C is a Knight
```

## Author

**Caroline Mildred Gomes**

CS50 AI – Harvard University

This project was completed as part of my learning journey in Artificial Intelligence and demonstrates the use of symbolic reasoning and logical inference to solve knowledge-based problems.
