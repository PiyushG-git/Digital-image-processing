

# 🧪 Lab 1 – Basic Image Processing

This lab demonstrates fundamental operations in Digital Image Processing (DIP) using Python and OpenCV. It includes color space transformations and basic image conversions.

---

## 📌 Implemented Scripts

- **OnlyBluePlane.py**  
  Extracts only the blue channel from a color image by setting the red and green channels to zero.

- **rgbToGray.py**  
  Converts an RGB image to grayscale using OpenCV's `cv2.cvtColor()` method.

- **rgbToBlackWhite.py**  
  Converts an RGB image to a binary (black & white) format using thresholding.

---

## 🗂️ Folder Structure
```
Lab_1
├── input
│ └── sample.jpg
├── output/
│ ├── output_OnlyBluePlane.jpg
│ ├── output_gray.jpg
│ └── output_bw.jpg
├── OnlyBluePlane.py
├── rgbToGray.py
├── rgbToBlackWhite.py
└── README.md
```

---

## ⚙️ Requirements

Make sure Python is installed. Then install the required libraries:

```bash
pip install -r ../requirements.txt
