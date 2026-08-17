# Activity 06 – Image Processing with Python

## Objective

Use Python and OpenCV to apply basic image-processing techniques to a single input photograph and observe how each technique changes the image.

## Description

Image processing applies operations to pictures to improve them, remove noise, or extract useful information. In this activity a single input photo is processed using several techniques from Chapter 10 of the Grade 9 AIRR Robotry book so students can compare results visually.

The same input image will be converted to greyscale, blurred with several Gaussian kernels, processed with Canny edge detection, and thresholded using simple, adaptive and Otsu methods.

## Techniques Used

### 1. Greyscale

Convert a colour image into a single-channel greyscale image (brightness only).

### 2. Gaussian Blur

Reduce noise and small details using Gaussian blur. This activity demonstrates kernel sizes used in the book: `3×3`, `9×9`, and `21×21`. Larger kernels produce stronger blur.

### 3. Canny Edge Detection

Detect boundaries or edges in the image. Edges help identify object outlines.

### 4. Simple Thresholding

Convert a greyscale image into a binary image using a fixed threshold. Pixels above the threshold become white; below become black. Use threshold `127` as in the book.

### 5. Adaptive Thresholding

Calculate a different threshold for each small region of the image. Useful when lighting is uneven.

### 6. Otsu's Method

Automatically determine a suitable global threshold from the image histogram.

## How the Activity Works

```
Input Photo
    ↓
Load Image
    ↓
Greyscale
    ↓
Gaussian Blur (3×3, 9×9, 21×21)
    ↓
Canny Edge Detection
    ↓
Simple Threshold (127)
    ↓
Adaptive Threshold
    ↓
Otsu's Threshold
    ↓
Save Results to output/
```

## Files

- `code/main.py` — the Python program to run the processing.
- `input/` — place your input image here (for example `input/input.jpg`).
- `output/` — processed images will be saved here by the program.
- `procedure.md` — step-by-step instructions to run the activity.

## Expected Output

The program will write processed images to the `output/` folder with names indicating the technique (for example `output/greyscale.jpg`, `output/blur_3.jpg`, `output/canny.jpg`, `output/threshold_simple.jpg`, `output/threshold_adaptive.jpg`, `output/threshold_otsu.jpg`). It will also display the images one by one so students can compare them on screen.

## Safety and Notes

- Use images that you are allowed to use (your own photos or public-domain images).
- Do not include personal data or faces if you do not have permission to share them.

## References

- AIRR Robotry Grade 9 — Chapter 10: Image Processing with Python (concepts used as the basis for this activity)
- OpenCV documentation
