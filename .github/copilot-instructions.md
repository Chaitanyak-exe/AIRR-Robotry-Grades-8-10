# AIRR Robotry Grades 8–10 — Copilot Instructions

You are helping me document hands-on robotics activities for the AIRR Robotry curriculum for Grades 8, 9 and 10.

The purpose of this repository is to provide simple, practical and beginner-friendly documentation containing:

- Activity information
- Theory
- Components
- Connections
- Procedure
- Circuit diagrams
- Source code
- Code explanation
- Images
- Expected output
- Results
- Challenges
- Troubleshooting

## IMPORTANT: SOURCE OF TRUTH

The activity titles and activity content supplied by me are the source of truth.

Do NOT:
- Invent activities.
- Rename activities.
- Combine activities.
- Remove activities.
- Add activities that I did not provide.
- Change official activity titles.
- Invent hardware connections.
- Invent pin numbers.
- Invent test results.
- Invent measurements.
- Claim that something worked unless I have confirmed it.

If information is missing, write:

[TO BE VERIFIED]

instead of guessing.

---

# WRITING STYLE

Use:

- Simple English
- Short sentences
- Beginner-friendly explanations
- Natural student-friendly language
- Clear technical terminology
- Practical explanations

The documentation should be understandable to a Grade 8–10 student.

Avoid unnecessarily complicated language.

Do NOT make the writing sound like:
- An AI-generated article
- A research paper
- Marketing material
- A university thesis

Avoid unnecessary words such as:
"revolutionary", "cutting-edge", "seamless", "state-of-the-art", etc.

---

# ACTIVITY README FORMAT

Every activity must use this structure:

# Activity Title

## Objective

Explain what the student will learn or build.

## Description

Give a short explanation of the activity.

## Components Required

List all hardware components actually used.

## Software Required

List the software, libraries and tools actually required.

## Theory

Explain the basic concept in simple language.

Keep this section short and relevant to the activity.

## Circuit Diagram

Add the circuit diagram using:

![Circuit Diagram](circuit/circuit.png)

If the diagram does not exist yet, write:

[TO BE ADDED]

## Connections

Use a table whenever possible.

Example:

| Component | Pin | Arduino/ESP32 Pin |
|---|---|---|
| LED | Anode | D13 |
| LED | Cathode | GND |

Only use verified connections.

## Procedure

Write numbered steps.

Keep each step simple.

Example:

1. Connect the components.
2. Connect the Arduino to the laptop.
3. Open Arduino IDE.
4. Select the correct board.
5. Upload the program.
6. Observe the output.

## Code

Include the actual tested code.

Do NOT create replacement code unless I specifically ask for code.

If code is stored in the `code/` folder, link to it.

## Working

Explain what happens when the activity runs.

## Expected Output

Describe the expected output.

Do not invent measurements or accuracy values.

## Result

Use the actual result I provide.

If I have not provided a result:

[TO BE VERIFIED]

## Small Challenge

Give one simple extension challenge suitable for the grade.

## Troubleshooting

Give common problems related to the actual activity.

## References

Include relevant references if provided.

---

# FILE STRUCTURE

Each activity should normally use:

Activity-Name/
│
├── README.md
├── components.md
├── connections.md
├── procedure.md
│
├── code/
│   ├── main.ino
│   ├── main.py
│   └── requirements.txt
│
├── circuit/
│   ├── circuit.png
│   └── circuit.pdf
│
└── images/
    ├── components.jpg
    ├── setup.jpg
    ├── working.jpg
    └── output.jpg

Only create files that are actually useful for the activity.

Do not create empty or unnecessary files.

---

# COMPONENT DOCUMENTATION

components.md should contain:

# Components Required

| Component | Quantity | Purpose |
|---|---:|---|
| Arduino Uno | 1 | Main controller |
| LED | 1 | Output |
| 220Ω Resistor | 1 | Limits LED current |

Do not add components that are not used.

---

# CONNECTION DOCUMENTATION

connections.md should contain:

# Connections

| Component | Component Pin | Controller Pin |
|---|---|---|
| HC-SR04 | TRIG | D9 |
| HC-SR04 | ECHO | D10 |
| HC-SR04 | VCC | 5V |
| HC-SR04 | GND | GND |

Only use verified connections.

---

# CODE RULES

For Arduino:

- Use `.ino`
- Keep code simple
- Add useful comments
- Avoid unnecessary libraries
- Explain important sections

For Python:

- Use `.py`
- Include required libraries
- Create `requirements.txt` when useful
- Keep code beginner-friendly

For ESP32:

- Clearly identify ESP32-specific pins
- Mention Wi-Fi requirements when applicable
- Never assume the user's board pinout if it has not been confirmed

---

# IMAGES

Images should be organized as:

images/
├── components.jpg
├── setup.jpg
├── working.jpg
└── output.jpg

Use descriptive filenames.

When an image exists, include it in README.md.

Example:

![Working Setup](images/working.jpg)

Do not create fake image references.

---

# GITHUB MARKDOWN

Use clean Markdown.

Use:
- Headings
- Tables
- Bullet points
- Numbered procedures
- Code blocks
- Images

Do not create excessively long paragraphs.

---

# GRADES

The repository contains:

Grade-8/
Grade-9/
Grade-10/

Do not create Grade 1–7 folders unless I specifically request them.

---

# HARDWARE AVAILABLE

Use the following hardware when applicable:

- Arduino Uno
- ESP32
- Breadboard
- LEDs
- 220Ω resistors
- 10kΩ resistors
- Push buttons
- Potentiometer
- HC-SR04 Ultrasonic Distance Sensor
- IR Sensor
- Servo motors
- DC motors
- Motor driver
- Jumper wires
- USB cables
- Laptop webcam
- Laptop microphone

I do NOT have an LDR sensor.

Therefore:

DO NOT create activities or connections that require an LDR.

Use the HC-SR04 Ultrasonic Distance Sensor or IR Sensor where appropriate.

---

# DOCUMENTATION WORKFLOW

When I give you an activity, follow this workflow:

1. Identify the activity.
2. Check the provided information.
3. Create/update the activity folder.
4. Create README.md.
5. Create components.md.
6. Create connections.md.
7. Create procedure.md if useful.
8. Organize code.
9. Add circuit diagram references.
10. Add image references.
11. Check all Markdown links.
12. Check that no information has been invented.
13. Report what files were created or modified.

Do NOT automatically run `git commit` or `git push` unless I specifically ask you to.

---

# FINAL QUALITY CHECK

Before completing a documentation task, verify:

- Activity title is unchanged.
- Components are accurate.
- Connections are accurate.
- Code is accurate.
- Procedure matches the actual activity.
- No LDR is included.
- No unsupported claims are made.
- No fake results are included.
- No broken image links are created.
- Markdown formatting is correct.
- Documentation is easy for students to understand.
