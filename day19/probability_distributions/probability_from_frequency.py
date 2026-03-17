# Probability from Frequency Function
def probability_from_frequency(data, event):
    """ Calculate the probability of an event based on frequency data."""
    total = len(data)
    event_count = data.count(event)
    return event_count / total

# Example frequency data
data = ['A', 'B', 'A', 'C', 'A', 'B', 'A', 'C', 'B', 'A']

# Probability of event A
print("Probability of A:", probability_from_frequency(data, 'A'))

