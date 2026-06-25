# Degrees of Separation (CS50 AI Project 0)

## Overview

This project is part of Harvard University's CS50 Introduction to Artificial Intelligence with Python course.

The goal of the project is to determine the shortest degree of separation between two actors based on the movies in which they have appeared together. The program models actors and movies as a graph and uses Breadth-First Search (BFS) to find the shortest connection between any two actors.

## Problem Statement

Given two actors:

* Source Actor
* Target Actor

The program searches through a movie database and finds the shortest chain of actors and movies connecting them.

Example:

Emma Watson → Brendan Gleeson → Michael Fassbender → Jennifer Lawrence

Degree of Separation: 3

## Concepts Used

* Graph Representation
* Breadth-First Search (BFS)
* Queue Frontier
* State Space Search
* Parent Tracking
* Path Reconstruction
* Python Data Structures (Dictionaries, Sets, Lists)

## Dataset

The project uses IMDb-inspired datasets:

### people.csv

Contains actor information.

### movies.csv

Contains movie information.

### stars.csv

Contains relationships between actors and movies.

## Algorithm

The solution uses Breadth-First Search because BFS guarantees the shortest path in an unweighted graph.

Steps:

1. Start from the source actor.
2. Add the actor to a queue frontier.
3. Explore neighboring actors through shared movies.
4. Track visited actors.
5. Stop when the target actor is found.
6. Reconstruct the path using parent pointers.

## Example Output

```text
Loading data...
Data loaded.

Name: Emma Watson
Name: Jennifer Lawrence

3 degrees of separation.

1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Skills Demonstrated

* Artificial Intelligence Search Techniques
* Graph Traversal
* Breadth-First Search
* Problem Solving
* Data Processing
* Algorithm Design
* Python Programming

## Author

Caroline Mildred Gomes

## Course

CS50 Introduction to Artificial Intelligence with Python
Harvard University
