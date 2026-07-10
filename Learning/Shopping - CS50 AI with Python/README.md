# Shopping - CS50 AI with Python

## Overview

This project is part of **CS50's Introduction to Artificial Intelligence with Python**. The objective is to build a machine learning classifier that predicts whether an online shopping visitor will complete a purchase based on their browsing session.

The project uses the **K-Nearest Neighbors (KNN)** algorithm with **k = 1** from the Scikit-learn library.

---

## Project Objective

Given information about a user's browsing session, such as:

* Number of administrative pages visited
* Product-related pages viewed
* Time spent on pages
* Bounce rate
* Exit rate
* Month of visit
* Visitor type
* Weekend or weekday

the model predicts whether the customer will generate revenue (make a purchase).

---

## Technologies Used

* Python 3
* Scikit-learn
* CSV Module

---

## Machine Learning Algorithm

**K-Nearest Neighbors (KNN)**

* Algorithm: K-Nearest Neighbor
* Number of neighbors: 1
* Library: `sklearn.neighbors.KNeighborsClassifier`

---

## Dataset

The dataset contains approximately **12,000 online shopping sessions**.

Each record contains **17 features** describing a visitor's browsing behavior.

Target variable:

* Revenue

  * `1` → Customer made a purchase
  * `0` → Customer did not make a purchase

---

## Features Used

1. Administrative
2. Administrative_Duration
3. Informational
4. Informational_Duration
5. ProductRelated
6. ProductRelated_Duration
7. BounceRates
8. ExitRates
9. PageValues
10. SpecialDay
11. Month
12. OperatingSystems
13. Browser
14. Region
15. TrafficType
16. VisitorType
17. Weekend

---

## Project Workflow

1. Load the dataset.
2. Convert categorical values into numerical values.
3. Separate evidence and labels.
4. Split the data into training and testing sets.
5. Train a KNN classifier (`k=1`).
6. Predict customer purchases on the test set.
7. Evaluate the model using Sensitivity and Specificity.

---

## Evaluation Metrics

### Sensitivity (True Positive Rate)

Measures how well the model identifies customers who actually make a purchase.

[
Sensitivity = \frac{True\ Positives}{Actual\ Positives}
]

### Specificity (True Negative Rate)

Measures how well the model identifies customers who do not make a purchase.

[
Specificity = \frac{True\ Negatives}{Actual\ Negatives}
]

---

## Learning Outcomes

Through this project I learned:

* Reading CSV files in Python
* Data preprocessing
* Feature encoding
* Machine learning with Scikit-learn
* K-Nearest Neighbors (KNN)
* Model training
* Model prediction
* Performance evaluation using Sensitivity and Specificity

---

## How to Run

```bash
python shopping.py shopping.csv
```

---

## Example Output

```text
Correct: 4100
Incorrect: 832
True Positive Rate: 43.18%
True Negative Rate: 90.25%
```

(The exact numbers vary because the train/test split is random.)

---

## Repository Structure

```text
shopping/
│── shopping.py
│── shopping.csv
│── README.md
```

---

## Author

**Caroline Mildred Gomes**

Student of English Literature | AI & Python Learner

Harvard CS50 – Introduction to Artificial Intelligence with Python

GitHub: https://github.com/carolinemildredgomes-hub

---

## License

This project was developed for educational purposes as part of Harvard's CS50 AI course.
