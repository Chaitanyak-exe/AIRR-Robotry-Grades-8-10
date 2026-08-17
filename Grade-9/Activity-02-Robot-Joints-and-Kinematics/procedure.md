# Procedure – 2-Link Robot Arm Kinematics

## Step 1 – Prepare the Links

1. Cut two strips of cardboard or use two ice-cream sticks.
2. Make one strip 20 cm long (Link 1) and the other 15 cm long (Link 2).
3. Draw a small circle near each end of the strips where the joints will be. Make the hole large enough for a paper fastener to turn freely.

## Step 2 – Make Joint 1

1. Place Link 1 on a sheet of paper and mark the base point where the first joint will be.
2. Push a paper fastener through the hole at one end of Link 1 and fix it to the paper or a small cardboard base so Link 1 can rotate.

## Step 3 – Make Joint 2

1. Align the far end of Link 1 and one end of Link 2 so their holes match.
2. Join them with a paper fastener. This is the second joint and it should allow Link 2 to rotate relative to Link 1.

## Step 4 – Mark the Base

1. On the paper base, mark the location of the joint where Link 1 is fixed. This is the origin (0,0) for X and Y measurements.
2. Draw a small coordinate axis if useful: the positive X axis to the right and positive Y axis upwards from the base.

## Step 5 – Set the Joint Angles

1. Use a protractor to set `θ1` at the base joint. Measure from the positive X axis to Link 1 in degrees.
2. Measure `θ2` between Link 1 and Link 2 using the protractor. Note that `θ1 + θ2` is the absolute angle of Link 2 from the X axis.

## Step 6 – Calculate the End-Effector Position

1. Use the formula:

```
X = L1 × cos(θ1) + L2 × cos(θ1 + θ2)
Y = L1 × sin(θ1) + L2 × sin(θ1 + θ2)
```

2. Use `L1 = 20 cm` and `L2 = 15 cm`. Make sure your calculator is in degree mode when using `sin` and `cos`.
3. Write down the calculated `X` and `Y` values.

## Step 7 – Measure the Actual Position

1. Physically move the links to the set angles `θ1` and `θ2`.
2. From the base mark, use the ruler to measure the horizontal distance (X) to the end-effector and the vertical distance (Y).
3. Record the measured values on the paper.

## Step 8 – Compare Results

1. Compare the calculated `X` and `Y` with the measured `X` and `Y`.
2. Note any differences and possible causes (angle measurement, flexible material, loose joints).

## Step 9 – Repeat for Other Angles

1. Repeat the steps for the three test cases in the README (and the challenge). Record results for each test.

Simple diagram to help measurement:

Base (origin)
O─────> +X
|
|
v +Y

Place the arm on the paper base so you can measure X to the right and Y upwards from the base mark.
