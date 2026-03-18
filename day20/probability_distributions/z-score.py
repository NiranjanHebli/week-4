# Function to calculate Z-score
def z_score(x, mean, std):
    """Calculates the Z-score for a given value, mean, and standard deviation."""
    return (x - mean) / std


# Dataset
data = [45, 50, 55, 60, 65]

# Compute mean manually
mean = sum(data) / len(data)

# Compute standard deviation manually
variance = sum((x - mean) ** 2 for x in data) / len(data)
std = variance ** 0.5

# Apply Z-score on dataset
z_scores = []
for x in data:
    z_scores.append(z_score(x, mean, std))

print("Mean:", mean)
print("Standard Deviation:", std)
print("Z-scores:", z_scores)