# Procedure – Simple Neural Network

# Part 1 — Prepare Your Laptop

### Step 1: Open Terminal

Press:

```text
Ctrl + Alt + T
```

A terminal window will open.

### Step 2: Check Python

Type:

```bash
python3 --version
```

You should see something like:

```text
Python 3.10.12
```

If you get a Python version, continue.

---

# Part 2 — Install the Required Libraries

You need two Python libraries.

### Step 3: Install NumPy

Run:

```bash
python3 -m pip install numpy
```

Wait for it to finish.

### Step 4: Install scikit-learn

Run:

```bash
python3 -m pip install scikit-learn
```

Wait for it to finish.

### Step 5: Check that both work

Run:

```bash
python3 -c "import numpy; import sklearn; print('Everything is installed correctly')"
```

You should see:

```text
Everything is installed correctly
```

If you see that, your laptop is ready.

---

# Part 3 — Understand What You Are Going to Teach the Network

Before running the program, understand the data.

We are going to teach the neural network this pattern:

| Input A | Input B | Correct Answer |
| ------: | ------: | -------------: |
|       0 |       0 |              0 |
|       0 |       1 |              1 |
|       1 |       0 |              1 |
|       1 |       1 |              0 |

This is the **XOR pattern**.

In simple words:

- If both inputs are the same → output `0`
- If the inputs are different → output `1`

So:

```text
0 + 0 → 0
0 + 1 → 1
1 + 0 → 1
1 + 1 → 0
```

You are going to give these examples to the neural network and let it learn the pattern.

---

# Part 4 — Create the Python Program

### Step 6: Go to your activity folder

Run:

```bash
cd /home/ck/Downloads/AIRR-Robotry-Grades-8-10/Grade-9/Activity-04-Deep-Learning
```

### Step 7: Open the folder in VS Code

Run:

```bash
code .
```

VS Code should open the activity folder.

### Step 8: Open `main.py`

Inside VS Code, open:

```text
code/main.py
```

### Step 9: Paste this code

Delete anything currently inside `main.py` and paste:

```python
import numpy as np
from sklearn.neural_network import MLPClassifier

# XOR training data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Correct answers
y = np.array([0, 1, 1, 0])

# Create the neural network
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

# Test the trained model
predictions = model.predict(X)

print("Input    Expected    Predicted")
print("--------------------------------")

for inputs, expected, predicted in zip(X, y, predictions):
    print(f"{inputs}       {expected}           {predicted}")

# Test one new input
new_input = np.array([[1, 0]])
prediction = model.predict(new_input)

print()
print("New Input:", new_input[0])
print("Prediction:", prediction[0])
```

### Step 10: Save the file

Press:

```text
Ctrl + S
```

---

# Part 5 — Understand the Neural Network

Before running it, look at this part:

```python
hidden_layer_sizes=(8, 8)
```

This means the neural network has:

```text
        INPUT
       /     \
      0       0
      |       |
      ↓       ↓
   ┌─────────────┐
   │  8 neurons  │
   └─────────────┘
          ↓
   ┌─────────────┐
   │  8 neurons  │
   └─────────────┘
          ↓
       OUTPUT
```

So conceptually:

```text
2 Inputs
   ↓
8 Neurons
   ↓
8 Neurons
   ↓
1 Output
```

This demonstrates the basic idea of the **input → hidden → output** structure described in the Grade 9 Deep Learning chapter.

---

# Part 6 — Train the Neural Network

### Step 11: Open the terminal in the activity folder

In VS Code you can use:

```text
Terminal → New Terminal
```

Or open a normal terminal and run:

```bash
cd /home/ck/Downloads/AIRR-Robotry-Grades-8-10/Grade-9/Activity-04-Deep-Learning
```

### Step 12: Run the program

```bash
python3 code/main.py
```

Press **Enter**.

---

# Part 7 — Observe the Training

The program first executes:

```python
model.fit(X, y)
```

This is the important part.

It tells the neural network:

> "Here are examples. Learn the relationship between the inputs and the correct answers."

The model processes the training data and adjusts its internal parameters.

After training, you should see:

```text
Neural network trained successfully!
```

---

# Part 8 — Check Whether It Learned

The program now tests all four examples.

You should get results similar to:

```text
Input    Expected    Predicted
--------------------------------
[0 0]       0           0
[0 1]       1           1
[1 0]       1           1
[1 1]       0           0
```

### Check each one

#### Test 1

```text
Input: [0 0]
Expected: 0
Predicted: 0
```

✅ Correct.

#### Test 2

```text
Input: [0 1]
Expected: 1
Predicted: 1
```

✅ Correct.

#### Test 3

```text
Input: [1 0]
Expected: 1
Predicted: 1
```

✅ Correct.

#### Test 4

```text
Input: [1 1]
Expected: 0
Predicted: 0
```

✅ Correct.

The exact output formatting may differ slightly.

---

# Part 9 — Give the Network a New Input

The program contains:

```python
new_input = np.array([[1, 0]])
```

This asks:

> "What do you predict for input 1, 0?"

The program then runs:

```python
prediction = model.predict(new_input)
```

You should see:

```text
New Input: [1 0]
Prediction: 1
```

The model has learned that:

```text
1 XOR 0 = 1
```

---

# Part 10 — Perform Your Own Experiment

Now you should actually experiment with the model.

Change:

```python
new_input = np.array([[1, 0]])
```

to:

```python
new_input = np.array([[0, 0]])
```

Save the file:

```text
Ctrl + S
```

Run:

```bash
python3 code/main.py
```

Look at:

```text
New Input: [0 0]
Prediction: 0
```

---

## Try another input

Change it to:

```python
new_input = np.array([[0, 1]])
```

Run:

```bash
python3 code/main.py
```

Expected:

```text
Prediction: 1
```

---

## Try the final input

Change it to:

```python
new_input = np.array([[1, 1]])
```

Run:

```bash
python3 code/main.py
```

Expected:

```text
Prediction: 0
```

---

# Part 11 — Record Your Results

Create this table in your notebook/report:

| Input   | Expected | Predicted | Correct? |
| ------- | -------: | --------: | -------- |
| `[0,0]` |        0 |    \_\_\_ | \_\_\_   |
| `[0,1]` |        1 |    \_\_\_ | \_\_\_   |
| `[1,0]` |        1 |    \_\_\_ | \_\_\_   |
| `[1,1]` |        0 |    \_\_\_ | \_\_\_   |

Fill it using the **actual output from your computer**.

Don't just copy the expected values.

---

# Part 12 — Do the Challenge

Now change:

```python
hidden_layer_sizes=(8, 8)
```

to:

```python
hidden_layer_sizes=(4, 4)
```

Save and run:

```bash
python3 code/main.py
```

Observe the result.

Then try:

```python
hidden_layer_sizes=(10, 10)
```

Run it again.

Record what happens.

You are now experimenting with the **number of neurons in the hidden layers**.

---

# Part 13 — Take Screenshots

You need evidence for your GitHub documentation.

Take a screenshot of:

### 1. Python program

Show `main.py` in VS Code.

Save as:

```text
program.jpg
```

### 2. Terminal output

Show:

```text
Neural network trained successfully!
```

and the predictions.

Save as:

```text
output.jpg
```

### 3. Experiment

Show the result after changing:

```text
(8, 8)
```

to:

```text
(4, 4)
```

Save as:

```text
experiment.jpg
```

Put these images inside:

```text
Grade-9/Activity-04-Deep-Learning/images/
```

---

# Part 14 — What You Should Understand After Performing It

The main concept you demonstrated is:

```text
Training Examples
       ↓
Neural Network
       ↓
Training
       ↓
Learned Pattern
       ↓
New Input
       ↓
Prediction
```

In this activity:

```text
[0,0] → 0
[0,1] → 1
[1,0] → 1
[1,1] → 0
```

The network learns the relationship from these examples.

This connects to the Grade 9 chapter's explanation that neural networks contain interconnected neurons and that their weights are adjusted during training.

---

# Part 15 — Final Result

After you have actually run the program, write your result based on what happened.

For example:

> The neural network was successfully trained using the XOR dataset. The trained model was able to predict the output for the given input patterns. The activity helped demonstrate the basic working of a neural network with input, hidden and output layers.

Only write this if your actual experiment produced the expected results.

---

# Part 16 — Final Cleanup

Restore your code to:

```python
hidden_layer_sizes=(8, 8)
```

and:

```python
new_input = np.array([[1, 0]])
```

Save it.

Run one final time:

```bash
python3 code/main.py
```

Make sure it works.

---
