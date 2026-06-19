# numpy_similarity.py
# Demonstrates masking, broadcasting, and cosine similarity

import numpy as np


# Create array
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original Array:")
print(arr)

# -------------------------
# Masking
# Filter values > 35
# -------------------------

mask = arr > 35

print("\nBoolean Mask:")
print(mask)

print("\nFiltered Values (>35):")
print(arr[mask])

# -------------------------
# Broadcasting
# Add 5 to every element
# -------------------------

scaled_array = arr + 5

print("\nBroadcasting Example (+5):")
print(scaled_array)


# -------------------------
# Cosine Similarity Function
# -------------------------

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)

    magnitude1 = np.linalg.norm(v1)
    magnitude2 = np.linalg.norm(v2)

    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity


# Test vector pair 1
vector1 = np.array([1, 2, 3])
vector2 = np.array([2, 4, 6])

# Test vector pair 2
vector3 = np.array([1, 0, 1])
vector4 = np.array([0, 1, 1])

print("\nCosine Similarity Results")

print(
    f"Vector1 vs Vector2: "
    f"{cosine_similarity(vector1, vector2):.4f}"
)

print(
    f"Vector3 vs Vector4: "
    f"{cosine_similarity(vector3, vector4):.4f}"
)