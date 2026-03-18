## Q1. Conceptual

### What is the difference between *args and **kwargs?

- *args allows a function to accept multiple positional arguments and stores them in a tuple. **kwargs allows a function to accept multiple keyword arguments and stores them in a dictionary. The main difference is that *args handles unnamed values, while **kwargs handles named values.

### When would you use each?

- Use *args when the number of positional inputs is unknown, such as summing many numbers. Use **kwargs when you need flexible named inputs, such as optional user details. They are commonly used in reusable functions where input requirements may vary.


## Q2. Coding

### File :- 
[`student.ipynb`](./student.ipynb)

## Q3. Conceptual

### What are dunder methods in Python?

- Dunder methods (double underscore methods) are special methods in Python whose names begin and end with double underscores, such as `__init__`. They define how objects behave with built in operations like printing, addition, or comparison. Python automatically calls them when related operations are performed.

### Why are they important?

- Dunder methods allow custom classes to behave like built in data types. They make objects more readable, reusable, and compatible with Python operators and functions. This is important for implementing operator overloading and object customization.

### Give 3 examples.

- `__init__` initializes object attributes when an object is created.
-  `__str__` defines how an object is displayed when printed. 
- `__add__` enables addition between objects using the + operator.