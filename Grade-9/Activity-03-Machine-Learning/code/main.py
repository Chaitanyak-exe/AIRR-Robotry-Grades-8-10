"""
Simple Machine Learning demo for Grade 9 students.

Loads the Iris dataset, trains a k-NN classifier, prints accuracy,
and shows example predictions. Includes a simple interactive option.
"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


def main():
    # Load the Iris dataset (small and suitable for teaching)
    iris = datasets.load_iris()
    X = iris.data  # features: sepal/petal lengths and widths
    y = iris.target  # labels: species (0,1,2)

    # Split into train and test sets (70% train, 30% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )

    # Create and train a k-NN classifier with k=3
    k = 3
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)

    # Evaluate on the test set
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    print(f"k-NN (k={k}) accuracy on test set: {acc*100:.1f}%")
    print("\nExample predictions (first 5 test samples):")
    for i in range(min(5, len(X_test))):
        features = X_test[i]
        pred = clf.predict(features.reshape(1, -1))[0]
        actual = y_test[i]
        print(f"Sample {i+1}: features={np.round(features,2).tolist()} -> predicted={iris.target_names[pred]}, actual={iris.target_names[actual]}")

    # Interactive: allow the student to type in a feature vector
    print("\nInteractive prediction: enter four numbers separated by spaces (or press Enter to skip)")
    try:
        line = input("Enter sepal_length sepal_width petal_length petal_width: ")
    except EOFError:
        line = ""

    if line.strip():
        try:
            vals = [float(x) for x in line.strip().split()]
            if len(vals) != 4:
                print("Please enter exactly four numbers.")
            else:
                vals = np.array(vals).reshape(1, -1)
                p = clf.predict(vals)[0]
                print(f"Predicted species: {iris.target_names[p]}")
        except ValueError:
            print("Invalid input — please enter numeric values.")


if __name__ == "__main__":
    main()
