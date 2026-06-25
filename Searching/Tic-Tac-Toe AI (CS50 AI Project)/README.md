# Tic-Tac-Toe AI (CS50 AI Project)

## Overview

This project is part of Harvard University's CS50 Introduction to Artificial Intelligence with Python.

The goal of the project is to build an unbeatable Tic-Tac-Toe AI using the Minimax algorithm. The AI evaluates all possible future game states and selects the optimal move that maximizes its chances of winning while minimizing the opponent's opportunities.

## Features

* Interactive Tic-Tac-Toe game using Pygame
* Unbeatable AI opponent
* Implementation of the Minimax decision-making algorithm
* Complete game-state evaluation
* Automatic win, loss, and tie detection

## Concepts Used

* Artificial Intelligence
* Adversarial Search
* Minimax Algorithm
* Recursive Decision Trees
* Game Theory
* State Space Search
* Python Programming

## How It Works

The game represents each board configuration as a state.

The AI explores every possible future move:

* X attempts to maximize the score.
* O attempts to minimize the score.

Utility values:

* X Win = 1
* Tie = 0
* O Win = -1

Using Minimax, the AI selects the move that guarantees the best possible outcome against an optimal opponent.

## Files

* `tictactoe.py` — Game logic and Minimax implementation
* `runner.py` — Graphical interface using Pygame

## Skills Demonstrated

* Recursive algorithms
* Artificial Intelligence search techniques
* Decision-making systems
* Python software development
* Algorithm design and optimization

## Author

Caroline Mildred Gomes

## Course

CS50 Introduction to Artificial Intelligence with Python

Harvard University
