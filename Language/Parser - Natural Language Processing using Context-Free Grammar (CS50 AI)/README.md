# Parser - Natural Language Processing using Context-Free Grammar (CS50 AI)

## Overview

This project was developed as part of **CS50's Introduction to Artificial Intelligence with Python (Harvard University)**.

The objective is to build a Natural Language Processing (NLP) parser that understands the grammatical structure of English sentences using **Context-Free Grammar (CFG)**.

Instead of treating text as a sequence of words, the parser analyzes how words relate to one another and constructs a syntax tree that represents the sentence's grammatical structure.

The project also extracts **noun phrase chunks**, which are useful for understanding the key subjects and objects in a sentence.

---

# Objectives

- Learn the fundamentals of Natural Language Processing.
- Understand Context-Free Grammar (CFG).
- Build a grammar parser using NLTK.
- Tokenize English sentences.
- Remove unnecessary punctuation and numeric tokens.
- Generate syntax trees.
- Extract noun phrase chunks.

---

# Features

- Sentence preprocessing
- Word tokenization
- Automatic lowercase conversion
- Removal of punctuation
- Context-Free Grammar parser
- Parse tree generation
- Noun phrase chunk extraction

---

# Technologies Used

- Python 3
- NLTK
- Context-Free Grammar (CFG)
- Chart Parser

---

# Project Structure

parser/
│
├── parser.py
├── README.md
├── requirements.txt
└── sentences/

---

# How It Works

1. Read an English sentence.
2. Tokenize the sentence.
3. Convert all words to lowercase.
4. Remove punctuation and numbers.
5. Parse the sentence using CFG.
6. Build a syntax tree.
7. Extract the smallest noun phrases.

---

# Example

Input

Holmes sat in the red armchair.

Output

Noun Phrase Chunks

Holmes

the red armchair

---

# AI Concepts Learned

- Natural Language Processing
- Context-Free Grammar
- Parsing
- Parse Trees
- Syntax Analysis
- Computational Linguistics
- Tree Traversal
- Recursive Grammar
- Tokenization
- Noun Phrase Extraction

---

# Learning Outcomes

After completing this project, I learned how computers analyze human language through grammar rules rather than simply reading words sequentially. I gained practical experience implementing a Context-Free Grammar, preprocessing text, parsing English sentences into syntax trees, and extracting meaningful noun phrases. This project also strengthened my understanding of recursion, tree structures, and one of the foundational techniques in Natural Language Processing.

---

# Future Improvements

- Support larger English vocabularies.
- Improve grammar coverage.
- Handle punctuation more naturally.
- Add semantic analysis.
- Integrate machine learning-based parsing.
- Build an interactive NLP visualization tool.

---

# License

This project was created for educational purposes as part of Harvard University's CS50 AI course.

---

## Author

**Caroline Mildred Gomes**

GitHub:
https://github.com/carolinemildredgomes-hub
