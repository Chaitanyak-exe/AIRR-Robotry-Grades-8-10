# Activity 01 – Human Neural Network

## Objective

This hands-on demonstration is designed to physically demonstrate the neural-network concepts introduced in Grade 10 Chapter 1. Students will act as neurons and pass information through a small network to understand how information moves through input, hidden and output layers.

## Source Basis

This activity is a student-created physical demonstration based on the neural-network concepts covered in Grade 10 AIRR Robotry Chapter 1 — Neural Networks — Deep Dive. It is not an official Robotry classroom activity; it is adapted by students to show the ideas in a physical, easy-to-understand way.

## Introduction (simple)

- Artificial Neural Network: A set of connected neurons (simple computing units) organised in layers that process information.
- Neuron / Node: A basic computing unit that multiplies inputs by weights, adds a bias, sums them, and (in real networks) applies an activation function.
- Layer: A group of neurons that process data together. Layers are arranged in depth (stacked) and width (number of neurons per layer).
- Weight: A parameter on a connection that controls how strongly one neuron's output affects the next neuron. In this activity weights are shown as thick or thin lines, not numeric values.
- Bias: An extra constant value added to a neuron's sum before the activation step.
- Input: The starting values fed into the network.
- Output: The final decision or result produced by the network.
- Hidden layer: Layers between input and output that transform information.

The Grade 10 source describes a neuron as a unit that multiplies inputs by weights, sums them, and applies an activation function; layers group neurons and Dense layers connect every neuron to every neuron in the previous layer.

## Network Structure for This Activity

3 Input Neurons
↓
4 Hidden Neurons (Hidden Layer 1)
↓
3 Hidden Neurons (Hidden Layer 2)
↓
2 Output Neurons

| Layer | Number of Students | Role |
|---|---:|---|
| Input | 3 | Receive input values (features) |
| Hidden 1 | 4 | Process information from input layer |
| Hidden 2 | 3 | Further process information |
| Output | 2 | Produce final result |

## Roles (what each student does)

- Input students: Receive the starting values (for example, Student Height, Student Age, Study Hours) and pass them to the next layer.
- Hidden-layer students: Receive information from the previous layer, combine the received information (verbally or by voting), and pass a simplified result forward.
- Output students: Receive the final information and represent the final decision (for example, "Pass" or "Needs More Practice").

Be clear that students are demonstrating the idea of neurons, not performing exact mathematical neuron computations.

## What is a Weight? (simple classroom analogy)

A weight controls how strongly one neuron's output influences the next neuron. In class:

- Represent a strong connection by a thick string or bold arrow.
- Represent a weak connection by a thin string or faint arrow.

Do NOT assign numeric trained weight values — this is only an analogy.

## What is a Bias?

A bias is an extra constant added to a neuron's sum before activation. In this activity you can show the bias as a small card attached to a neuron labelled "Bias". Do not claim real numerical bias values are being trained or used.

## Activation Functions

Activation functions let networks learn non-linear patterns. The Grade 10 chapter mentions ReLU, Sigmoid, Leaky ReLU and Softmax. Do not implement these physically — just mention them and explain their purpose in simple language.

## Activity Flow (summary)

Input Students → Hidden Layer 1 → Hidden Layer 2 → Output Students

## Requirements

See `components.md` in this folder.

## Procedure

See `procedure.md` in this folder for step-by-step instructions written for beginners.

## Observation

| Stage | Observation |
|---|---|
| Input Layer | |
| Hidden Layer 1 | |
| Hidden Layer 2 | |
| Output Layer | |
| Information Flow | |

Leave these observations blank while preparing — fill them after running the activity.

## Result

The human neural network demonstration was used to understand how information can move through input, hidden and output layers. Replace this sentence with your real result after completing the activity and recording observations.

## Learning Outcomes

- Understand neural-network layers (input, hidden, output).
- Understand what a neuron represents.
- Understand information flow through layers.
- Understand the basic idea of weights and how connections can be stronger or weaker.
- Understand the role of bias in a neuron.
- Know examples of activation functions (ReLU, Sigmoid, Leaky ReLU, Softmax) and their purpose.
- Relate a physical classroom activity to abstract neural-network concepts.

## Conclusion

This student-created demonstration helps visualise how inputs move through layers, how hidden layers transform information, and how outputs are formed. It prepares students for later lessons on training, weights, and evaluation using tools like TensorFlow/Keras.

## Reference

Grade 10 AIRR Robotry Study Book,
Chapter 1 — Neural Networks — Deep Dive
