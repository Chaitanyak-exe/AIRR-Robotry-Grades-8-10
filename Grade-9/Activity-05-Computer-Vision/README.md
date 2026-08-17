# Activity 05 – Computer Vision: Live Greyscale Webcam

## Objective

To use Python and OpenCV to access a webcam, display a live colour video, and convert the video into greyscale in real time.

## Description

Computer Vision is a field of Artificial Intelligence that allows computers to work with visual information such as images and videos.

In this activity, the laptop webcam is used as the source of live visual information.

Python and OpenCV are used to:

1. Open the webcam.
2. Capture video frames.
3. Convert each colour frame into greyscale.
4. Display the original colour video.
5. Display the greyscale video at the same time.

The activity is based on the Grade 9 AIRR Robotry practical:

**"PRACTICAL — Live Greyscale Webcam"**

The book instructs students to install OpenCV, enter the webcam program, run it, observe the colour and greyscale webcam feeds, and press Q to close the windows.

---

# What is Computer Vision?

Computer Vision is a field of Artificial Intelligence that enables computers to extract meaningful information from images and videos.

A digital image can be considered as a grid of pixels.

Each pixel contains information about a small part of the image.

A colour image normally contains three colour channels:

- Red
- Green
- Blue

A greyscale image uses a single value for each pixel.

The value represents the brightness of the pixel.

---

# What is OpenCV?

OpenCV stands for **Open Source Computer Vision Library**.

It is a computer vision library that can be used with Python for image and video processing.

In this activity, OpenCV is used to:

- Access the webcam
- Capture video frames
- Convert colour frames to greyscale
- Display video windows
- Close the webcam safely

---

# How the Activity Works

The activity follows this process:

```text
Webcam
   ↓
Capture Video Frame
   ↓
Colour Frame
   ↓
Convert to Greyscale
   ↓
Display Both Frames
```

## Requirements

### Hardware

- Laptop or desktop computer with a built-in webcam or a USB webcam

### Software

- Python 3
- OpenCV (`opencv-python`)
- VS Code or any text editor
- Terminal

## Installation

Install OpenCV with:

```bash
python3 -m pip install opencv-python
```

Verify installation:

```bash
python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
```

## Procedure

Follow the detailed steps in `procedure.md`. In short:

1. Prepare the laptop and webcam.
2. Install OpenCV.
3. Open `code/main.py`.
4. Run `python3 code/main.py` to start the colour and greyscale windows.
5. Press `q` while a window is focused to exit.

## Source Code

See `code/main.py` for the full program. The program opens the default webcam, captures frames, converts them to greyscale, and displays both the colour and greyscale frames side by side in separate windows.

## Expected Output

When you run the program two windows should appear:

- `Colour Camera` — shows the live colour webcam feed.
- `Greyscale Camera` — shows the same feed converted to greyscale in real time.

Both windows should update in real time. Press `q` to close the windows and stop the program.

## Experiments (from the book)

The book suggests three simple experiments you can try by editing the program:

### Experiment 1 – Mirror Mode

Add the line:

```python
frame = cv2.flip(frame, 1)
```

Place it after reading `frame` and before converting to greyscale. This will mirror the image horizontally.

### Experiment 2 – Add Text

Use `cv2.putText()` to add text onto the frame. Example:

```python
cv2.putText(
    frame,
    "YourName",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)
```

Replace `"YourName"` with your own name.

### Experiment 3 – Draw a Rectangle

Use `cv2.rectangle()` to draw a rectangle. Example:

```python
cv2.rectangle(
    frame,
    (200, 150),
    (440, 330),
    (0, 255, 0),
    2
)
```

Place these lines before `cv2.imshow()` so they appear in the displayed frame.

## Observation

| Test             | Observation |
| ---------------- | ----------- |
| Colour Camera    |             |
| Greyscale Camera |             |
| Mirror Mode      |             |
| Text Overlay     |             |
| Rectangle        |             |

Fill these fields after you perform the activity.

## Result

Template result (update after performing the activity):

"The webcam was successfully accessed using Python and OpenCV, and the live colour video was converted into greyscale."

Do not claim the activity was performed unless you ran the program yourself and updated the observations.

## Small Challenge

Combine mirror mode, text overlay and rectangle drawing into a single program and run it. Save a screenshot showing all three features.

## Troubleshooting

- Webcam not opening: close other camera apps and try again.
- OpenCV not installed: run the install command above.
- Camera already being used: close applications that may use the camera.
- Camera permissions: grant camera access to the terminal or application if your OS asks.
- Multiple webcams: change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` to use the other camera.

## Learning Outcomes

- Understand what computer vision is and how images are represented as pixels.
- Use OpenCV to access a webcam and read video frames.
- Convert colour frames to greyscale.
- Display live video windows and safely release the webcam.

## Conclusion

This practical demonstrates how Python and OpenCV can access a webcam and perform simple image processing in real time. It is suitable for Grade 9 students to try with minimal setup.

## References

- AIRR Robotry Grade 9 – Programming Robots and Artificial Intelligence, Chapter 9 – Introduction to Computer Vision
- OpenCV documentation
