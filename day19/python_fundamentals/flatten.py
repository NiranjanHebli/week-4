# Flattening a nested list and removing even numbers by using list comprehension
def flatten_remove_even(nested_list):
    """Flattens a nested list and removes even numbers."""
    return [num for sublist in nested_list for num in sublist if num % 2 != 0]


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = flatten_remove_even(data)

print(result)
