# Procedure – Human Neural Network (step-by-step)

This procedure is written for beginners. Read each step aloud and follow carefully.

PART 1 — PREPARE THE CLASSROOM

1. Choose an open area in the classroom where 12 students can stand in rows.
2. Explain that each student will act as one neuron in a small neural network.
3. Prepare paper cards and a marker so each student can wear or hold a label.

PART 2 — ARRANGE THE LAYERS

4. Select 3 students for the Input Layer. Give each an input label:
   - Student Height
   - Student Age
   - Study Hours
   Ask them to stand in a row at the front.

5. Select 4 students for Hidden Layer 1. Label them "Hidden1 – Neuron 1" through "Hidden1 – Neuron 4" and place them behind the input students.

6. Select 3 students for Hidden Layer 2. Label them "Hidden2 – Neuron 1" through "Hidden2 – Neuron 3" and place them behind Hidden Layer 1.

7. Select 2 students for the Output Layer. Label them:
   - Output – Pass
   - Output – Needs More Practice
   Place them at the far end.

PART 3 — CREATE CONNECTIONS

8. Use string, wool, or paper arrows to connect every student in one layer to every student in the next layer. If strings are not available, students can point or pass cards to show the connection.
9. Explain that a Dense (fully connected) layer connects each neuron to every neuron in the next layer. This is a visual demonstration — do not calculate real trained weights.

PART 4 — DEMONSTRATE INFORMATION FLOW

10. Give sample input values to the input students (read them aloud or place number cards):
    - Height = 170 cm
    - Age = 16
    - Study Hours = 3
11. Ask Input students to pass their value (verbally or by card) to each student in Hidden Layer 1 that they are connected to.
12. Hidden Layer 1 students receive the inputs. Explain that in a real neuron they would multiply inputs by weights and sum them, then add a bias and apply an activation function; in this activity they only discuss or vote on a simplified outcome and pass a chosen label/value to the next layer.
13. Hidden Layer 1 students pass their simplified result to all students in Hidden Layer 2.
14. Hidden Layer 2 students repeat the same simple combine-and-pass step and send results to the output students.

PART 5 — OUTPUT AND INTERPRETATION

15. Output students receive the information and decide which class they would pick (for example, "Pass" or "Needs More Practice") based on the received signals.
16. Discuss with students how a real trained network would compute numeric outputs and choose the class using an activation like Softmax; emphasise that this activity only demonstrates flow, not training.

PART 6 — DEMONSTRATE WEIGHTS AND BIAS (CLASSROOM ANALOGIES)

17. Choose one connection and label it "Weight". Show a strong connection (thick string) and a weak connection (thin string) to illustrate the difference in influence.
18. Explain bias by showing a card labelled "Bias" attached to a hidden-layer student; explain that bias is an extra constant added before activation.

PART 7 — DISCUSSION QUESTIONS

19. Ask students:
    - What does the input layer do?
    - What do hidden layers do?
    - What is the role of the output layer?
    - What is a neuron in simple words?
    - What is a weight and how can you show it in class?
    - What is bias?
    - Why do neural networks use activation functions?

PART 8 — OBSERVATIONS

20. Record observations in the observation table in `README.md`. Leave blanks during preparation and fill them after running the demonstration.

PART 9 — TAKE EVIDENCE

21. Take real photographs of the activity (from above, well-lit). Save them in the `images/` folder with the recommended filenames.

Recommended filenames:

- network-overview.jpg
- input-layer.jpg
- hidden-layer-1.jpg
- hidden-layer-2.jpg
- connections.jpg
- output-layer.jpg
- final-activity.jpg

PART 10 — CLEANUP

22. Collect the cards, strings and other materials. Thank the students for participating.
