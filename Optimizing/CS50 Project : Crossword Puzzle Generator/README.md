# CS50 AI Project  – Crossword Generator

## Overview

This project is part of **CS50's Introduction to Artificial Intelligence with Python**. The objective is to build an AI that automatically fills a crossword puzzle by modeling it as a **Constraint Satisfaction Problem (CSP)**.

The solver assigns words to crossword variables while satisfying all unary and binary constraints.

## Features

* Node Consistency
* Arc Consistency (AC-3)
* Backtracking Search
* Minimum Remaining Values (MRV)
* Degree Heuristic
* Least Constraining Value (LCV)

## Algorithms Used

* Constraint Satisfaction Problem (CSP)
* Node Consistency
* Arc Consistency
* AC-3 Algorithm
* Recursive Backtracking Search

## Project Structure

```text
crossword/
│── crossword.py
│── generate.py
│── data/
│── assets/
```

## How to Run

```bash
python generate.py data/structure1.txt data/words1.txt
```

To generate an image:

```bash
python generate.py data/structure1.txt data/words1.txt output.png
```

## Skills Demonstrated

* Artificial Intelligence
* Constraint Satisfaction Problems
* Search Algorithms
* Recursive Programming
* Heuristic Search
* Python Programming
* Problem Solving

## Learning Outcomes

Through this project, I learned how AI models a real-world problem as a Constraint Satisfaction Problem, reduces the search space using Node and Arc Consistency, applies AC-3 for constraint propagation, and efficiently searches for a valid solution using Backtracking with MRV, Degree, and LCV heuristics.

## Author

**Caroline Mildred Gomes**
