# Deep Learning – Simple Neural Network

## Objective

To understand the basic working of an Artificial Neural Network (ANN) by training a small neural network to recognize a simple pattern.

## Description

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers to learn patterns from data.

In this activity, we use a small neural network in Python.

The neural network is trained using a simple XOR dataset.

The model learns the relationship between two input values and predicts the correct output.

This activity helps us understand the basic idea of:

- Input data
- Training data
- Neural network
- Hidden layers
- Output
- Prediction

The Grade 9 book explains that an Artificial Neural Network contains interconnected neurons arranged into input, hidden and output layers. The connections have weights that are adjusted during training. :contentReference[oaicite:2]{index=2}

---

## Important Note

The Grade 9 book's Chapter 6 is mainly an introduction to Deep Learning and Artificial Neural Networks. It explains the structure and concepts of neural networks rather than providing this exact XOR Python practical.

Therefore, this activity is a simple hands-on implementation created to demonstrate the ANN concepts taught in the chapter.

---

# What is Deep Learning?

Deep Learning is a powerful subset of Machine Learning that uses artificial neural networks with many layers to learn complex patterns from data.

The Grade 9 book explains that Deep Learning can automatically learn useful features from raw data instead of requiring a person to manually select all the features. :contentReference[oaicite:3]{index=3}

---

# What is an Artificial Neural Network?

An Artificial Neural Network, or ANN, is a mathematical model inspired loosely by the human brain.

It consists of connected neurons arranged in layers.

A basic neural network contains:

```text
Input Layer
     ↓
Hidden Layer
     ↓
Output Layer
```

## Theory based on the Grade 9 book

The Grade 9 book introduces Deep Learning and Artificial Neural Networks (ANNs). It explains neurons, layers (input, hidden, output), and the idea that connections (weights) are adjusted during training so the network can learn patterns from examples. The chapter is conceptual and uses diagrams rather than code.

This activity follows those ideas and gives a small hands‑on implementation so students can see training and prediction in action.

## How the activity works

The program trains a small neural network on the XOR pattern (four examples). During training, the network adjusts weights to reduce errors on the training examples. After training the program tests the network on the same examples and prints the predicted outputs.

## Requirements

- Laptop with `python3`
- `numpy` and `scikit-learn` Python libraries
- Text editor (for example, VS Code)

No extra hardware is needed.

## Software installation

Install the required Python libraries with:

```bash
python3 -m pip install --user numpy scikit-learn
```

If you cannot install packages on your computer, use an online environment such as Google Colab and run the same install command there.

## Procedure

Follow the step-by-step instructions in `procedure.md`. In summary:

1. Install the required libraries.
2. Open `code/main.py` and read the comments.
3. Run the program:

```bash
python3 code/main.py
```

4. Observe the printed training messages and predictions.
5. Change `hidden_layer_sizes` or `new_input` and re-run to experiment.

## Source Code

The code is in `code/main.py`. It defines the XOR dataset, creates an `MLPClassifier` neural network, trains it with `model.fit(X, y)`, and prints predictions.

## Code Explanation

- `X` contains the four input pairs for XOR.
- `y` contains the correct outputs for each pair.
- `MLPClassifier(...)` creates a small neural network; `hidden_layer_sizes=(8,8)` means two hidden layers of 8 neurons each.
- `model.fit(X, y)` trains the network.
- `model.predict(...)` returns the network's outputs for given inputs.

## Expected Output

When the program runs successfully you should see output similar to:

```
Neural network trained successfully!

Input    Expected    Predicted
--------------------------------
[0 0]       0           0
[0 1]       1           1
[1 0]       1           1
[1 1]       0           0

New Input: [1 0]
Prediction: 1
```

Exact formatting may differ; the important part is that predicted values match the XOR outputs.

## Result

After running the program, note the printed predictions. The neural network should correctly predict the XOR outputs for these training examples.

## Small Challenge

Try changing `hidden_layer_sizes` to `(4,4)` or `(16,16)` and observe whether the network still learns the XOR pattern. Also try changing `max_iter` to a larger value if the model issues a convergence warning.

## Troubleshooting

- `ModuleNotFoundError: No module named 'sklearn'` — run the install command above.
- Convergence warnings — increase `max_iter` or try a different `solver` (for example `adam`).
- If training is slow, reduce hidden layer sizes or run on a faster machine.

## Learning Outcomes

- Understand the basic ANN structure (input, hidden, output).
- See that training adjusts weights to fit examples.
- Run a simple Python program to train and test a neural network.
- Experiment with model size and observe effects on learning.

## Conclusion

This activity implements a tiny neural network to demonstrate the Deep Learning concepts introduced in the Grade 9 book. It is a small, practical exercise meant to make the chapter's ideas concrete.

## References

- Grade 9 AIRR Robotry book, Chapter 6 (Deep Learning) — used as the conceptual source. The book explains ANN structure and training but does not provide this exact XOR Python example; this implementation is a minimal hands-on follow-up.
