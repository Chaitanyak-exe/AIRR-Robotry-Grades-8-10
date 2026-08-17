#!/usr/bin/env python3
"""
Simple image-processing demo for Grade 9 students.

Usage:
  python3 code/main.py            # uses input/input.jpg
  python3 code/main.py myphoto.jpg

The program loads an input image, applies greyscale, several Gaussian blurs,
Canny edge detection, simple/adaptive/Otsu thresholding, displays results,
and saves output images to the output/ folder.
"""

import sys
import os
import cv2


def ensure_dirs():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)


def load_image(path):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Could not load image '{path}'. Please place a valid image in the input/ folder.")
        sys.exit(1)
    return img


def save_and_show(name, img, outname=None):
    if outname:
        cv2.imwrite(outname, img)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyWindow(name)


def main():
    ensure_dirs()

    input_path = "input/input.jpg"
    if len(sys.argv) > 1:
        input_path = sys.argv[1]

    img = load_image(input_path)

    # Save and show original
    save_and_show("Original", img, os.path.join("output", "original.jpg"))

    # Greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    save_and_show("Greyscale", grey, os.path.join("output", "greyscale.jpg"))

    # Gaussian blurs with different kernel sizes
    for k in (3, 9, 21):
        blur = cv2.GaussianBlur(grey, (k, k), 0)
        outname = os.path.join("output", f"blur_{k}.jpg")
        save_and_show(f"Gaussian Blur {k}x{k}", blur, outname)

    # Canny edge detection
    # Use thresholds 100 and 200 for demonstration
    edges = cv2.Canny(grey, 100, 200)
    save_and_show("Canny Edges", edges, os.path.join("output", "canny.jpg"))

    # Simple thresholding (fixed threshold 127)
    _, thresh_simple = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)
    save_and_show("Simple Threshold (127)", thresh_simple, os.path.join("output", "threshold_simple.jpg"))

    # Adaptive thresholding (mean)
    thresh_adaptive = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 11, 2)
    save_and_show("Adaptive Threshold (mean)", thresh_adaptive, os.path.join("output", "threshold_adaptive.jpg"))

    # Otsu's thresholding
    _, thresh_otsu = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    save_and_show("Otsu Threshold", thresh_otsu, os.path.join("output", "threshold_otsu.jpg"))

    print("Processing complete. Processed images saved in the output/ folder.")


if __name__ == "__main__":
    main()
