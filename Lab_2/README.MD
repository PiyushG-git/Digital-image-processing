# Lab 2 - Digital Image Processing

This lab covers two fundamental image processing techniques:

## 1. Bit Plane Slicing
**Objective:**  
To decompose a grayscale image into its constituent bit planes to analyze the contribution of each bit to the overall image.

**Steps:**
- Load the image in grayscale mode.
- Extract each bit plane (0–7) using bitwise operations.
- Display the original image and all bit planes in a grid using Matplotlib.

**Python Code:** [`bit_slicing.py`](bit_slicing.py)

---

## 2. Histogram Equalization
**Objective:**  
To enhance the contrast of an image by redistributing pixel intensity values.

**Steps:**
- Load the image in grayscale mode.
- Apply OpenCV's `equalizeHist()` method.
- Display the original and histogram-equalized images side by side.

**Python Code:** [`histogram_equilaziation.py`](histogram_equilaziation.py)

---

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
