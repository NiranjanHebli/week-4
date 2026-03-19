# Q1 - Conceptual

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


# Q2 - Coding

## File:

### [`mse.ipynb`](mse.ipynb) :- 
Mean Squared Error (MSE) is a measure of the average squared difference between predicted and actual values. It is used to evaluate the performance of a model in regression problems.


# Q3 - Conceptual

## Bias–Variance Tradeoff

Bias–variance tradeoff explains the balance between a model being too simple and too complex.

- Bias is the error caused by simplifying assumptions in the model. High bias means the model cannot capture important patterns.
- Variance is the error caused by sensitivity to training data. High variance means the model changes too much with different datasets.

A good model finds a balance where both bias and variance are reasonably low.


## Underfitting

Underfitting happens when the model is too simple to learn the data properly.

- High bias, low variance
- Performs poorly on both training and test data
- Misses important relationships in data

Example:- Using a straight line to fit highly curved data.

## Overfitting

Overfitting happens when the model learns training data too closely, including noise.

- Low bias, high variance
- Very good training performance but poor test performance
- Fails to generalize to new data

Example:- Using a very high-degree polynomial for simple data.
