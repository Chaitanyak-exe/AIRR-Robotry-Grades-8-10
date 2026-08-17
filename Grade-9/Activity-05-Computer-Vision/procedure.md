# Procedure – Live Greyscale Webcam

## Aim

To access a live webcam using Python and OpenCV and convert the live colour video into greyscale in real time.

---

# Part 1 – Prepare the Hardware

## Step 1 – Get the Laptop

Take a laptop or desktop computer.

## Step 2 – Check the Webcam

If your laptop has a built-in webcam, make sure it is available.

If you are using an external webcam, connect it to the computer using USB.

## Step 3 – Close Other Camera Applications

Close applications such as:

- Camera
- Zoom
- Google Meet
- Microsoft Teams
- Other applications currently using the webcam

This prevents the camera from being occupied by another application.

---

# Part 2 – Check Python

## Step 4 – Open the Terminal

Open the terminal.

## Step 5 – Check Python

Run:

```bash
python3 --version
```

## Part 3 – Open Activity Folder

### Step 6 – Change to activity folder

Run:

```bash
cd /home/ck/Downloads/AIRR-Robotry-Grades-8-10/Grade-9/Activity-05-Computer-Vision
```

## Part 4 – Install OpenCV

### Step 7 – Install OpenCV

Run:

```bash
python3 -m pip install opencv-python
```

### Step 8 – Verify OpenCV

Run:

```bash
python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
```

## Part 5 – Prepare the Python Program

### Step 9 – Open `code/main.py`

Open `code/main.py` in your editor. The complete code is shown below — you can copy it into that file if it is not present.

```python
import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
	print("Error: Could not open webcam.")
	exit()

while True:

	# Capture a frame
	ret, frame = cap.read()

	if not ret:
		print("Error: Could not read frame.")
		break

	# Convert the colour frame to greyscale
	grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display the original colour video
	cv2.imshow("Colour Camera", frame)

	# Display the greyscale video
	cv2.imshow("Greyscale Camera", grey_frame)

	# Press Q to quit
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
```

### Step 10 – Save the file

Save `code/main.py` and close the editor if you wish.

## Part 6 – Run the Program

### Step 11 – Run the program

From the activity folder run:

```bash
python3 code/main.py
```

### Step 12 – Observe Colour Camera

Look at the `Colour Camera` window. It should show live colour video from the webcam. Move your hand or an object in front of the camera to see motion.

### Step 13 – Observe Greyscale Camera

Look at the `Greyscale Camera` window. It should show the same view in greyscale (shades of grey). Note how colour becomes brightness values.

## Part 7 – Test Objects

Place the following objects in front of the camera one by one and observe both windows:

- Hand
- Pen
- Book
- Cup
- Mobile phone

Move the objects and see how they appear in both colour and greyscale windows.

## Part 8 – Stop the Program

Click on any OpenCV window and press the `q` key to stop the program. The webcam will be released and windows closed.

## Part 9 – Experiment 1: Mirror Mode

Edit `code/main.py` and after reading the frame add:

```python
frame = cv2.flip(frame, 1)
```

Save and re-run `python3 code/main.py`. Observe that left and right are swapped (mirror image).

## Part 10 – Experiment 2: Add Text

Edit `code/main.py` and before `cv2.imshow()` add:

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

Replace `"YourName"` with your name, save and run the program.

## Part 11 – Experiment 3: Draw Rectangle

Edit `code/main.py` and before `cv2.imshow()` add:

```python
cv2.rectangle(
	frame,
	(200, 150),
	(440, 330),
	(0, 255, 0),
	2
)
```

Save and run the program to see a rectangle overlay on the video.

## Part 12 – Combine Experiments

Try adding mirror mode, text overlay and rectangle drawing together in the same loop (place them before `cv2.imshow()`) and run the program. Observe the combined effect.

## Part 13 – Record Observations

Use the observation table in `README.md` to record what you saw for each test.

## Part 14 – Take Evidence

Take real screenshots or photos during the activity and save them in the `images/` folder with these names:

- program.jpg
- colour-camera.jpg
- greyscale-camera.jpg
- mirror-mode.jpg
- text-overlay.jpg
- rectangle.jpg

## Part 15 – Final Test

Run the basic program again and verify:

- Webcam opens
- Colour window appears
- Greyscale window appears
- Video updates in real time
- Pressing `q` closes the windows and releases the webcam
