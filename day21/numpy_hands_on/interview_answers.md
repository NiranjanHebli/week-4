# Q1 :- Conceptual 

NumPy broadcasting is a feature in NumPy that allows arrays of different shapes to perform arithmetic operations together without manually resizing them. NumPy automatically expands the smaller array across compatible dimensions so that element-wise operations can still happen.

For example, if a 1D array [1, 2, 3] is added to a 2D matrix with 3 columns, NumPy repeats the 1D array across each row before addition.

It is useful because it:

- reduces the need for explicit loops
- makes code shorter and cleaner
- improves performance since operations are vectorized
- saves memory by avoiding unnecessary copies

Example:
If matrix =
[[1, 2, 3],
 [4, 5, 6]]

and vector = [10, 20, 30],

result becomes:
[[11, 22, 33],
 [14, 25, 36]]

Here the vector is automatically broadcast across both rows.


# Q2 :- Coding

## File:- [`normalize.ipynb`](normalize.ipynb)


# Q3:- Conceptual

Vectorisation means performing operations on entire arrays at once using optimized functions in NumPy, while loops process elements one by one using Python statements.

In loops, Python handles each iteration separately, which adds overhead and makes execution slower for large datasets. In vectorisation, NumPy uses compiled low level code (C-based implementation) to apply operations directly on complete arrays.

NumPy is faster because it avoids Python level iteration, uses contiguous memory storage, and performs bulk operations efficiently. This makes vectorised code shorter, cleaner, and much faster for numerical computation.