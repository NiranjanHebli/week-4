# Q1. Concetual

# Types of Machine Learning

## Description

Machine learning is a branch of AI where computers learn patterns from data and make predictions or decisions without being explicitly programmed for every task. The main types of machine learning are based on how the model receives data and feedback during training.

# 1. Supervised Learning

## Explanation

In supervised learning, the model is trained using labeled data, meaning both input and correct output are already known. The algorithm learns the relationship between inputs and outputs and then predicts results for new data.

## Examples

- Predicting house prices using past price data (regression)
- Predicting whether an email is spam or not (classification)


# 2. Unsupervised Learning

## Explanation

In unsupervised learning, the data has no target labels. The model tries to discover hidden patterns, groups, or structures in the data by itself.

## Examples

- Customer segmentation based on shopping behavior
- Grouping similar news articles automatically


# 3. Reinforcement Learning

## Explanation

In reinforcement learning, an agent learns by interacting with an environment and receiving rewards or penalties based on actions. The goal is to maximize total reward over time.

## Examples

- A robot learning to walk
- Game-playing systems like AlphaGo learning to win games


# 4. Semi-Supervised Learning

## Explanation

Semi-supervised learning uses a small amount of labeled data and a large amount of unlabeled data. It is useful when labeling data is expensive or time-consuming.

## Examples

- Image recognition where only some images are labeled
- Speech recognition systems trained with partial labels

# Q2. Coding


```python
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Filter rows where target variable meets condition
survived = df[df['Survived'] == 1]

# Compute average fare for survived passengers
average_fare = survived['Fare'].mean()

print("Average Fare of Survived Passengers:", average_fare)
```

## File Link:- 

### [`coding_problem.ipynb`](coding_problem.ipynb)


# Q3. Conceptual


## Regression

Regression is used when the target output is a continuous numeric value, meaning the answer can be any number within a range. This is often the case in estimation or prediction problems where the goal is to output a numerical value. For example, predicting the price of a house, estimating the cost of a medical procedure, or forecasting the number of customers in a given time frame are all regression problems.

### Examples:

-  Predicting house price based on size, location, and number of rooms
-  Estimating cab fare from trip distance and traffic
-  Forecasting monthly sales revenue


## Classification

Classification is used when the target output belongs to categories or classes. This is often the case in decision making problems where the goal is to assign an instance to one or more predefined categories. For example, classifying emails as spam or not spam, diagnosing a disease based on symptoms, or predicting customer churn based on their behavior are all classification problems.

### Examples:

- Email spam detection (Spam / Not Spam)
- Disease prediction (Positive / Negative)
- Customer churn prediction (Will Leave / Will Stay)