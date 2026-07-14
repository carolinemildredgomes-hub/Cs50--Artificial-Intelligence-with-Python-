# BERT Masked Language Model & Attention Visualization

## Author

**Caroline Mildred Gomes**

---

# Project Overview

This project was completed as part of **CS50's Introduction to Artificial Intelligence with Python (Harvard University).**

The objective is to understand how **BERT (Bidirectional Encoder Representations from Transformers)** predicts missing words and how the **Transformer Attention Mechanism** helps language models understand natural language.

Unlike traditional language models that process text sequentially, BERT analyzes the entire sentence simultaneously using Self-Attention, allowing every word to consider every other word in the sentence.

The program predicts masked words and visualizes the attention patterns learned by BERT.

---

# Learning Objectives

- Understand Natural Language Processing (NLP)
- Learn Masked Language Modeling (MLM)
- Understand BERT architecture
- Learn Transformer models
- Understand Self-Attention
- Visualize Multi-Head Attention
- Analyze language relationships learned by neural networks

---

# Project Features

- Predicts missing words using BERT
- Tokenizes natural language input
- Identifies the `[MASK]` token
- Uses Hugging Face Transformers
- Generates attention visualization diagrams
- Produces 144 attention maps
- Demonstrates how Transformer attention works

---

# Technologies Used

- Python
- TensorFlow
- Hugging Face Transformers
- Pillow (PIL)
- NumPy
- BERT Base Uncased

---

# Project Structure

```
mask.py
analysis.md
attention/
README.md
```

---

# How It Works

1. User enters a sentence containing `[MASK]`.
2. The tokenizer converts text into BERT tokens.
3. BERT predicts the most likely missing words.
4. The attention scores from every Transformer layer are extracted.
5. One visualization is generated for each attention head.

Since BERT Base contains:

- 12 Transformer Layers
- 12 Attention Heads per Layer

the project generates:

```
12 × 12 = 144 attention diagrams
```

---

# Example

Input

```
The dog chased the [MASK].
```

Possible Predictions

```
cat
ball
rabbit
boy
```

---

# Attention Visualization

Each attention diagram displays:

- Rows → Tokens paying attention
- Columns → Tokens being attended to
- White → High attention
- Black → Low attention

These diagrams help interpret how BERT processes language.

---

# Key Concepts Learned

- Natural Language Processing
- Tokenization
- Masked Language Modeling
- Transformer Architecture
- Self-Attention
- Multi-Head Attention
- Language Representation
- Contextual Word Embeddings
- Neural Networks for NLP

---

# Real-World Applications

The techniques demonstrated in this project are fundamental to many modern AI systems, including:

- AI Chatbots
- Virtual Assistants
- Machine Translation
- Text Summarization
- Search Engines
- Question Answering Systems
- Grammar Correction
- Sentiment Analysis
- Document Classification
- Information Retrieval

---

# Skills Demonstrated

- Python Programming
- Deep Learning Fundamentals
- Transformer Models
- TensorFlow
- Hugging Face Transformers
- Data Visualization
- Natural Language Processing
- AI Model Interpretation

---

# Course

CS50's Introduction to Artificial Intelligence with Python

Harvard University

---

# Author

**Caroline Mildred Gomes**

Bachelor of Arts (Honours) in English Literature

Aspiring AI Engineer | NLP Enthusiast | Python Developer
