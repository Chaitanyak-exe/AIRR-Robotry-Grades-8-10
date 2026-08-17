# Procedure – Draw a Neural Network

Follow these steps to complete the drawing activity. Use a sheet of paper or a diagram program.

1. Take a sheet of paper or open a diagramming application.

2. Draw the Input Layer on the left side.

3. Draw 4 neurons (small circles) vertically and label them:
   - Petal length
   - Petal width
   - Sepal length
   - Sepal width

4. Draw Hidden Layer 1 to the right of the input layer.

5. Draw 6 neurons (small circles) in Hidden Layer 1.

6. Connect every input neuron to every Hidden Layer 1 neuron (draw lines between each pair).

7. Calculate the number of connections from Input → Hidden 1:

   4 × 6 = 24

8. Draw Hidden Layer 2 to the right of Hidden Layer 1.

9. Draw 4 neurons in Hidden Layer 2.

10. Connect every Hidden Layer 1 neuron to every Hidden Layer 2 neuron.

11. Calculate the number of connections from Hidden 1 → Hidden 2:

6 × 4 = 24

12. Draw the Output Layer to the right of Hidden Layer 2.

13. Draw 3 output neurons and label them:

- Setosa
- Versicolor
- Virginica

14. Connect every Hidden Layer 2 neuron to every output neuron.

15. Calculate the number of connections from Hidden 2 → Output:

4 × 3 = 12

16. Select one connection line anywhere in the diagram and label it with a weight, for example `w1`.

17. Add all connections:

Total = 24 + 24 + 12 = 60

18. Check that every neuron in each layer is connected to every neuron in the adjacent layer.

19. Finalise the diagram using a pen or colouring to make labels clear.

20. Take clear photographs of your completed diagram from above (well-lit) and save them.

21. Place the photographs in the `images/` folder using the recommended filenames.

## Observation Table

| Connection          | Calculation | Number |
| ------------------- | ----------: | -----: |
| Input → Hidden 1    |       4 × 6 |     24 |
| Hidden 1 → Hidden 2 |       6 × 4 |     24 |
| Hidden 2 → Output   |       4 × 3 |     12 |
| Total               |             |     60 |
