import numpy as np
from sklearn.neural_network import MLPClassifier

# XOR training data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected outputs
y = np.array([0, 1, 1, 0])

# Create a small neural network
model = MLPClassifier(
    hidden_layer_sizes=(8, 8),
    activation="relu",
    solver="lbfgs",
    max_iter=2000,
    random_state=42
)

# Train the neural network
model.fit(X, y)

print("Neural network trained successfully!")
print()

# Test the model
predictions = model.predict(X)

print("Input    Expected    Predicted")
print("--------------------------------")

for inputs, expected, predicted in zip(X, y, predictions):
    print(
        f"{inputs}       {expected}           {predicted}"
    )

# Test a new input
new_input = np.array([[1, 0]])
prediction = model.predict(new_input)

print()
print("New Input:", new_input[0])
print("Prediction:", prediction[0])