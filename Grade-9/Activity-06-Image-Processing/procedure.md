# Procedure – Live Image Processing

Follow these steps to run the image-processing activity using Python and OpenCV.

## Part 1 — Prepare your computer

1. Use a laptop or desktop with Python 3 installed.
2. Open a terminal.

## Part 2 — Check Python

Run:

```bash
python3 --version
```

## Part 3 — Change to the activity folder

Run:

```bash
cd /home/ck/Downloads/AIRR-Robotry-Grades-8-10/Grade-9/Activity-06-Image-Processing
```

## Part 4 — Install OpenCV

Run:

```bash
python3 -m pip install opencv-python
```

Verify:

```bash
python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
```

## Part 5 — Prepare an input image

1. Put a photo file into the `input/` folder. Name it `input.jpg` or pass the filename as an argument when running the script.
2. Use a normal colour photo with clear objects so the effects are visible.

## Part 6 — Open the Python program

Open `code/main.py` in your editor. The program loads the input image, applies the techniques shown in Chapter 10, displays each result briefly, and saves processed images to `output/`.

## Part 7 — Run the program

Run with the default input filename:

```bash
python3 code/main.py
```

Or specify an input file:

```bash
python3 code/main.py input/myphoto.jpg
```

The program will:

- Load the image
- Create and save `output/greyscale.jpg`
- Create and save `output/blur_3.jpg`, `output/blur_9.jpg`, `output/blur_21.jpg`
- Create and save `output/canny.jpg`
- Create and save `output/threshold_simple.jpg`
- Create and save `output/threshold_adaptive.jpg`
- Create and save `output/threshold_otsu.jpg`

The program will also display each processed image in a window. Press any key while a window is focused to move to the next image. After the last image the program will exit.

## Part 8 — Observe and Record

Compare the saved images in the `output/` folder and note how each technique changes the image (noise reduction, edges, binary masks, etc.). Record your observations in a notebook or photo captions.

## Part 9 — Take Evidence

Take screenshots or photos of the original and processed images and add them to the `images/` folder. Use filenames recommended in `images/README.md`.

## Notes

- If the input image is large, processing and display may be slower. Use a moderate-sized image (for example 800×600) for quicker results.
