# Machine Learning

## Source inspection

I searched the repository for the Grade 9 AIRR Robotry book and its "Machine Learning" chapter but could not find a copy of the book or the chapter pages in this project. Because the book is not present in the workspace, the activity below is a simple, beginner-friendly machine-learning practical that demonstrates the basic concepts commonly taught at Grade 9 level: data, training, model, and prediction. If you provide the book chapter, I will update the activity to follow it exactly.

## Objective

Learn the basic idea of supervised Machine Learning by training a simple classifier on a small dataset and using it to make predictions.

## Description

This activity uses Python and the laptop to teach how a computer can learn from example data. The student will:

- Prepare the software environment.
- Load a small dataset that comes with the Python library.
- Train a simple classification model.
- Test the model and see how well it predicts.

This is not about writing rules by hand. Instead the computer finds patterns in the data during training and uses them to make predictions.

## What is Machine Learning?

- Data: examples with inputs and known answers (labels).
- Training: the process of giving data to an algorithm so it can learn a pattern.
- Model: the result of training; it can make predictions on new data.
- Prediction: using the model to guess the label for new inputs.
- Classification: a type of prediction where the model chooses a category (for example, flower species).

## How the Activity Works

Data
↓
Training (build a model)
↓
Model
↓
New input
↓
Prediction

We use the small built-in Iris dataset and a simple k-nearest-neighbour (k-NN) classifier to keep the activity easy and fast.

## Components / Requirements

- Laptop with Python 3 (python3)
- Internet access to install Python libraries (only if they are not already installed)
- Optional: a text editor or IDE

Software libraries used:

- `scikit-learn` (for dataset and classifier)
- `numpy` (used by scikit-learn)

Do not need Arduino, sensors, or other hardware for this activity.

## Software Installation

Install required libraries with:

```bash
python3 -m pip install --user scikit-learn numpy
```

If `python3` is not on the PATH, use the appropriate command for your system.

## Procedure

Follow the detailed steps in `procedure.md`. In short:

1. Install the required Python libraries.
2. Open the file `code/main.py` in a text editor.
3. Run the program: `python3 code/main.py`.
4. Observe training output, accuracy, and example predictions printed by the program.
5. Try the small interactive input option to make your own prediction.

## Source Code

See `code/main.py` for the full beginner-friendly implementation.

### What the program does

- Loads the Iris dataset from scikit-learn.
- Splits the data into training and test sets.
- Trains a k-nearest-neighbour classifier (k=3).
- Prints the accuracy on the test set and shows a few example predictions.
- Offers an optional interactive mode where the student can type feature values to get a prediction.

## Expected Output

When you run `python3 code/main.py` you should see:

- A message showing training and test sizes.
- The classifier accuracy (for example around 90% on the Iris dataset).
- A small table of example predictions showing predicted and actual labels.

Exact accuracy may vary because the data is split randomly.

## Result

After running the script you should be able to say: "I trained a simple ML model and it can predict labels for new inputs." Leave a note of the accuracy you observed.

## Small Challenge

Try changing the `k` value in `code/main.py` from 3 to 1 and 5. Observe how the accuracy changes. Which `k` gives the best result for your run?

## Troubleshooting

- If `ModuleNotFoundError` appears, install the missing library using the install command above.
- If `python3` is not found, check your Python installation.
- If the program crashes due to wrong input in interactive mode, restart and enter numeric feature values separated by spaces.

## Learning Outcomes

- Understand the difference between rule-based programming and learning from data.
- Know the terms: data, training, model, prediction, classification.
- Train and evaluate a simple ML model using Python.
- Observe how model choices (for example `k`) affect performance.

## Conclusion

This activity gives a hands-on introduction to supervised Machine Learning using a small dataset and a very simple classifier. It is suitable for Grade 9 students to try on a laptop.
