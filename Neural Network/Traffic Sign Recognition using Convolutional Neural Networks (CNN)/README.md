# Traffic Sign Recognition using Convolutional Neural Networks (CNN)

## Introduction

Traffic Sign Recognition is one of the fundamental applications of Computer Vision in autonomous driving systems. A self-driving vehicle must correctly recognize traffic signs such as Stop, Yield, Speed Limit, No Entry, and many others in order to make safe driving decisions.

This project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify traffic signs from images. The model is trained on the German Traffic Sign Recognition Benchmark (GTSRB), which contains thousands of labeled traffic sign images across 43 categories.

This project was completed as part of **Harvard CS50's Introduction to Artificial Intelligence with Python**.

---

# Project Objectives

The primary objectives of this project are:

* Learn the fundamentals of Computer Vision.
* Understand how Convolutional Neural Networks process images.
* Load and preprocess image datasets using OpenCV.
* Build and train a CNN using TensorFlow/Keras.
* Evaluate model performance using unseen test data.
* Save the trained model for future use.

---

# Dataset

The project uses the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset.

Dataset characteristics:

* 43 traffic sign categories
* More than 39,000 training images
* Real-world road sign photographs
* Various lighting conditions
* Different viewing angles
* Different distances and scales

Each category is stored inside its own directory.

Example:

gtsrb/

```
0/
    image1.ppm
    image2.ppm

1/
    image1.ppm
    image2.ppm

...

42/
```

Each folder number represents the corresponding class label.

---

# Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* Scikit-Learn

---

# Project Structure

```text
traffic/

│
├── gtsrb/
│     ├── 0/
│     ├── 1/
│     ├── ...
│     └── 42/
│
├── traffic.py
├── requirements.txt
├── README.md
└── model.keras (optional)
```

---

# Machine Learning Workflow

The complete workflow of the project is:

1. Load every image from the dataset.
2. Resize each image to 30 × 30 pixels.
3. Store images and labels.
4. Convert labels into one-hot encoded vectors.
5. Split the dataset into training and testing sets.
6. Build a Convolutional Neural Network.
7. Train the model.
8. Evaluate model accuracy.
9. Save the trained model.

---

# Image Preprocessing

Before training, every image undergoes the following preprocessing steps:

* Read using OpenCV.
* Resize to 30 × 30 pixels.
* Store as a NumPy array.
* Assign the corresponding category label.

Resizing ensures that every image has the same dimensions, which is required by TensorFlow.

---

# Neural Network Architecture

The implemented CNN consists of:

Input Layer

↓

Conv2D (32 filters)

↓

MaxPooling2D

↓

Conv2D (64 filters)

↓

MaxPooling2D

↓

Flatten

↓

Dense (128 neurons)

↓

Dropout (0.5)

↓

Output Layer (43 neurons with Softmax)

This architecture is simple, computationally efficient, and performs well for the GTSRB dataset.

---

# Layer Descriptions

### Convolution Layers

Extract important visual features such as edges, shapes, and textures.

### Max Pooling Layers

Reduce image dimensions while preserving the most important information.

### Flatten Layer

Converts feature maps into a one-dimensional vector.

### Dense Layer

Learns high-level relationships between extracted features.

### Dropout Layer

Randomly disables neurons during training to reduce overfitting.

### Softmax Output Layer

Produces a probability for each of the 43 traffic sign categories.

---

# Model Compilation

The model uses:

Optimizer:

* Adam

Loss Function:

* Categorical Crossentropy

Evaluation Metric:

* Accuracy

---

# Experimentation Process

Several CNN architectures were considered before selecting the final model. Initially, a network with a single convolutional layer was explored. While this trained quickly, it struggled to learn more complex visual patterns and produced lower validation accuracy.

A second convolutional layer was then added, allowing the network to detect higher-level features such as arrows, circles, and traffic sign shapes. This noticeably improved performance.

Different Dense layer sizes (64 and 128 neurons) were also considered. The 128-neuron configuration provided stronger learning capacity without significantly increasing training time.

Finally, a Dropout layer with a rate of 0.5 was included to reduce overfitting. Without Dropout, the model achieved very high training accuracy but showed a larger gap between training and testing performance. Adding Dropout improved the model's ability to generalize to previously unseen images.

Overall, the selected architecture provided a good balance between accuracy, computational efficiency, and simplicity, making it well suited for this classification task.

---

# Results

After training for multiple epochs, the model successfully learned to classify traffic signs across all 43 categories.

Typical observations included:

* Training loss decreased steadily.
* Training accuracy increased over time.
* Test accuracy remained high, indicating good generalization.
* Dropout helped reduce overfitting.

Actual accuracy may vary depending on hardware, TensorFlow version, random initialization, and train/test split.

---

# Challenges

Some of the main challenges encountered during this project include:

* Loading thousands of images efficiently.
* Understanding image preprocessing.
* Designing an appropriate CNN architecture.
* Preventing overfitting.
* Choosing suitable hyperparameters.

---

# Possible Future Improvements

Future improvements may include:

* Data Augmentation
* Batch Normalization
* Additional Convolutional Layers
* Learning Rate Scheduling
* Early Stopping
* Transfer Learning using pretrained CNNs such as MobileNet or ResNet
* Hyperparameter tuning

---

# Installation

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Train the model:

```bash
python traffic.py gtsrb
```

Train and save the model:

```bash
python traffic.py gtsrb traffic_model.keras 
```

---

# Skills Learned

This project demonstrates knowledge of:

* Computer Vision
* Deep Learning
* Convolutional Neural Networks
* TensorFlow
* Keras
* OpenCV
* Image Preprocessing
* Multi-Class Classification
* Machine Learning Pipelines

---

# Acknowledgements

This project was completed as part of **Harvard CS50's Introduction to Artificial Intelligence with Python**.

Dataset:

German Traffic Sign Recognition Benchmark (GTSRB)

---

# Author

**Caroline Mildred Gomes**

Student of English Literature

Artificial Intelligence & Software Engineering Enthusiast

GitHub: carolinemildredgomes-hub
