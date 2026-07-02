# 🧬 Heredity AI – Genetic Trait Probability Inference

## Author
**Caroline Mildred Gomes**

---

## 📌 Project Overview

This project is part of CS50 AI and implements a probabilistic AI system that predicts:

- Probability of a person having 0, 1, or 2 copies of a gene
- Probability of expressing a genetic trait (e.g., hearing impairment)

The system uses a **Bayesian Network** to model genetic inheritance and mutation.

---

## 🧠 Key Idea

Genes are **hidden variables** — we cannot directly observe them.

However, we can observe:

- Family relationships
- Whether a trait is expressed

Using this information, the AI infers genetic probabilities.

---

## 📊 Model Used

The system is based on a **Bayesian Network**:
Parent Genes → Child Genes → Trait


It considers:

- Gene inheritance from parents
- Mutation probability (1%)
- Trait probability based on gene count

---

## 📁 Dataset Format

CSV files contain:


name,mother,father,trait


Example:


Harry,Lily,James,
James,,,1
Lily,,,0


---

## ⚙️ How It Works

The program:

1. Loads family data
2. Enumerates all possible gene and trait combinations
3. Computes joint probabilities
4. Aggregates results
5. Normalizes probabilities

---

## 🧮 Probability Model

### Gene Probability

- 0 copies → 96%
- 1 copy → 3%
- 2 copies → 1%

### Trait Probability

| Genes | P(Trait=True) |
|------|--------------|
| 2 | 0.65 |
| 1 | 0.56 |
| 0 | 0.01 |

---

## 🔁 Mutation

Each gene passed from parent has:

- 1% chance of flipping (mutation)

---

## 🚀 How to Run

```bash
python heredity.py data/family0.csv
📌 Output Example

Harry:
Gene:
2: 0.0092
1: 0.4557
0: 0.5351

Trait:
True: 0.2665
False: 0.7335

🧩 Functions Implemented
1. joint_probability()

Computes probability of a complete world (genes + traits).

2. update()

Accumulates probabilities into distributions.

3. normalize()

Ensures all probability distributions sum to 1.

📈 Concepts Used
Bayesian Networks
Conditional Probability
Joint Probability
Genetic Inheritance
Enumeration of possible worlds
Probability normalization
🧪 Example Applications

This type of model is used in:

Genetic disease prediction
Medical diagnosis systems
AI decision-making systems
Risk analysis models
🛠️ Requirements
Python 3.x
No external libraries required
📌 Project Status

✔ Completed
✔ Fully Functional
✔ CS50 AI Compatible

📜 License

This project is for educational purposes.

🙌 Credits

CS50 AI – Harvard University

✍️ Author

Caroline Mildred Gomes
