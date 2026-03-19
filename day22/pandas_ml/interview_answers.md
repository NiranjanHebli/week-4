# Q1 :- Conceptual

In pandas, `loc` and `iloc` are both used to select data from a DataFrame, but they differ in how rows and columns are referenced.

Difference between loc and iloc

### 1. loc (label-based selection)

- Uses row labels and column names
- Includes the last index in slicing

Example:

```python 
df.loc[0:3, ['sepal length (cm)', 'species']]
```

This selects:

- Rows 0 to 3
- Columns named sepal length (cm) and species

Here row 3 is included.
 
### 2. iloc (index-based selection)

- Uses integer positions
- Excludes the last index in slicing

Example:

```python
df.iloc[0:3, 0:2]
```


# Q2:- Coding 

## File:-

### [`filter_data.ipynb`](filter_data.ipynb)


# Q3:- Conceptual

### What is the purpose of describe()?

The purpose of describe() in pandas is to quickly summarize the main statistical properties of numerical columns in a dataset. It automatically calculates values such as count, mean, standard deviation, minimum, and maximum. This output helps understand how the data is distributed and how much variation exists.


### What insights can we get from it?

we can quickly understand the central tendency, spread, and range of data, and identify potential outliers or patterns.
