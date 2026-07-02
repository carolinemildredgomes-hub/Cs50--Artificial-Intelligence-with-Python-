# 🌐 PageRank AI – Web Page Ranking System

## Author
**Caroline Mildred Gomes**

---

## 📌 Overview

This project implements Google's PageRank algorithm using two approaches:

1. Sampling (Random Surfer Simulation)
2. Iterative Mathematical Convergence

It ranks web pages based on importance derived from link structure.

---

## 🧠 Concept

A page is important if:

> Important pages link to it

---

## 🎲 Random Surfer Model

A user:

- Follows links (85%)
- Randomly jumps (15%)

---

## ⚙️ Features

- Transition probability model
- Markov Chain simulation
- Iterative PageRank computation
- Convergence detection

---

## 🚀 How to Run

```bash
python pagerank.py corpus0


📊 Output Example

Sampling:

1.html: 0.2223
2.html: 0.4303
3.html: 0.2145
4.html: 0.1329

Iteration:

1.html: 0.2202
2.html: 0.4289
3.html: 0.2202
4.html: 0.1307

📚 Concepts Used
Markov Chains
Probability distributions
Graph theory
Random processes
Iterative convergence

📂 Project Structure
pagerank.py
corpus0/
corpus1/
README.md


✨ Author

Caroline Mildred Gomes
