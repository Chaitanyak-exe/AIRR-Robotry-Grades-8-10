# Robot Joints and Kinematics

## Objective

Understand a simple 2-link robot arm and calculate the position of its end effector using forward kinematics.

## Description

- A robot joint is a point where two parts (links) can move relative to each other.
- A robot link is a rigid part of the arm between two joints.
- The end effector is the point or tool at the end of the robot arm. In this activity the end of Link 2 is the end effector.
- A 2-joint planar robot arm has two links joined by two rotary joints and moves in a flat plane.
- Forward kinematics means using known joint angles and link lengths to calculate the end-effector position.

This activity uses simple cardboard or wooden strips to build a 2-link model and practise the forward-kinematics formula.

## Components Required

1. Cardboard strips or ice-cream sticks × 2
2. Paper fasteners / split pins × 2
3. Ruler
4. Protractor
5. Pencil
6. Paper
7. Scissors
8. Tape or glue
9. Calculator

Link 1 = 20 cm
Link 2 = 15 cm

## Theory

### Robot Joint

A joint allows movement between two links. Here we use a simple rotating joint made with a paper fastener.

### Robot Link

A link is a rigid part of the robot arm between two joints.

### End Effector

The end effector is the point at the end of the second link. We will use the tip of Link 2 as the end effector.

### Forward Kinematics

Forward kinematics takes the joint angles and link lengths as input and gives the end-effector position (X, Y) as output.

Input: joint angles (θ1, θ2) and link lengths (L1, L2)

Output: end-effector position (X, Y)

Angles must be set on the protractor and calculators should be in degree mode when using sin/cos with degrees.

## Formula

Use the 2D two-joint forward-kinematics equations:

```
X = L1 × cos(θ1) + L2 × cos(θ1 + θ2)
Y = L1 × sin(θ1) + L2 × sin(θ1 + θ2)
```

Variables:

- `L1` = first link length (20 cm)
- `L2` = second link length (15 cm)
- `θ1` = first joint angle (degrees)
- `θ2` = second joint angle (degrees)
- `X` = horizontal end-effector position (cm)
- `Y` = vertical end-effector position (cm)

Make sure the calculator is set to degrees, or convert degrees to radians when using radian-mode functions.

## Physical Model

How to build the simple robot arm:

1. Cut two strips of cardboard or prepare two ice-cream sticks.
2. Make them approximately 20 cm and 15 cm long (Link 1 = 20 cm, Link 2 = 15 cm).
3. Make small holes near the ends where the links join and at the base.
4. Fix Link 1 to the base with a paper fastener so it can rotate.
5. Connect Link 2 to the far end of Link 1 with a paper fastener.
6. Use a protractor at each joint to set joint angles `θ1` and `θ2`.
7. Mark the base position on paper so you can measure X and Y from the base.
8. Use the end of Link 2 as the end-effector point.

Simple ASCII diagram:

Base
O──────────── Link 1 ────────────O
\
 \
 \ Link 2
\
 O
End Effector

## Procedure

Follow the steps in `procedure.md` to prepare the links, set angles, calculate X and Y, and compare with measurements.

## Activity Tests

Use `L1 = 20 cm` and `L2 = 15 cm` for all tests.

Test 1:
θ1 = 0°
θ2 = 0°

Test 2:
θ1 = 90°
θ2 = 0°

Test 3:
θ1 = 45°
θ2 = 45°

## Observation Table

| Test | L1 (cm) | L2 (cm) | θ1 (°) | θ2 (°) | Calculated X (cm) | Calculated Y (cm) |     Measured X |     Measured Y |
| ---- | ------: | ------: | :----: | :----: | ----------------: | ----------------: | -------------: | -------------: |
| 1    |      20 |      15 |   0    |   0    |             35.00 |              0.00 | To be measured | To be measured |
| 2    |      20 |      15 |   90   |   0    |              0.00 |             35.00 | To be measured | To be measured |
| 3    |      20 |      15 |   45   |   45   |             14.14 |             29.14 | To be measured | To be measured |

Note: Measured values should be recorded after physically performing the tests. Calculated values are shown above.

## Expected Result

The measured position of the end effector should be reasonably close to the calculated position. Small differences can occur because of:

- inaccurate angle measurement
- flexible cardboard or slightly bent sticks
- small play in the paper fasteners
- measurement error when reading X and Y

## Small Challenge

Try `θ1 = 30°` and `θ2 = 60°`. Calculate `X` and `Y` using the forward-kinematics formula, then position the arm physically and check the result.

Do not write the answer here — calculate it yourself as a challenge.

## Learning Outcomes

- Understand what robot joints are
- Understand what robot links are
- Identify the end effector
- Use forward kinematics to calculate `X` and `Y`
- See how joint angles affect the arm position
- Compare calculated and measured positions

## Safety

- Be careful while using scissors.
- Do not use sharp tools unnecessarily.
- Do not force the paper fasteners; make the holes large enough.
- Keep the work area clean.

## Conclusion

This activity shows how joint angles determine the position of the end effector. By using the forward-kinematics formula you can predict where the tip of the arm will be for given joint angles.
