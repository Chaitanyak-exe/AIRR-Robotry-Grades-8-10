# Activity 07 – Neural Networks

## Objective

Understand the structure of a simple Artificial Neural Network by drawing its layers, neurons and connections, and counting the total number of connections (weights).

## Description

In this activity you will draw a neural-network diagram with four layers: an input layer, two hidden layers, and an output layer. You will label the layers and neurons, draw every connection between adjacent layers, mark one connection as a weight, and calculate how many weights (connections) there are in total.

Keep your drawing neat and label each part clearly.

## Neural Network Architecture

The network in this activity has the following structure:

- Input layer: 4 neurons (features)
  - Petal length
  - Petal width
  - Sepal length
  - Sepal width
- Hidden layer 1: 6 neurons
- Hidden layer 2: 4 neurons
- Output layer: 3 neurons (classes)
  - Setosa
  - Versicolor
  - Virginica

Visually the network is:

Input (4) → Hidden 1 (6) → Hidden 2 (4) → Output (3)

## Activity

Follow the procedure to draw the network on paper or in a diagram program. Make sure to:

- Draw all four layers and the correct number of neurons in each layer.
- Draw every connection between adjacent layers (every neuron in one layer connects to every neuron in the next layer).
- Label each layer and the input and output neurons with their names.
- Label one connection as a weight (for example `w1`).
- Count and record the number of connections between each pair of adjacent layers and the total number of connections.

## Weight Calculation

Calculate the number of connections as follows:

Input → Hidden 1:

4 × 6 = 24

Hidden 1 → Hidden 2:

6 × 4 = 24

Hidden 2 → Output:

4 × 3 = 12

Total connections (weights):

24 + 24 + 12 = 60

## Observation

| Connection          | Calculation | Number |
| ------------------- | ----------: | -----: |
| Input → Hidden 1    |       4 × 6 |     24 |
| Hidden 1 → Hidden 2 |       6 × 4 |     24 |
| Hidden 2 → Output   |       4 × 3 |     12 |
| Total               |             |     60 |

## Result

Template result (update after you do the drawing):

"The neural network architecture was drawn successfully and the total number of connections between adjacent layers was calculated as 60."

Only replace this sentence with your real result after you complete and photograph the drawing.

## Small Challenge

If Hidden Layer 1 had 8 neurons instead of 6, calculate the new total number of connections. Do not look up the answer — try to calculate it yourself first.

## Learning Outcomes

- Understand neural-network layers: input, hidden, output.
- Identify neurons and connections.
- Understand what a weight is in a neural network.
- Calculate the number of connections between layers.
- Represent a neural-network architecture visually.

## Conclusion

Drawing a neural network helps you see how inputs travel through layers and how the number of neurons affects the number of connections. This simple activity builds intuition before learning about training and weights in later lessons.

## References

- AIRR Robotry Grade 9 — Chapter 6: Deep Learning Basics (used as the conceptual source for this activity)
