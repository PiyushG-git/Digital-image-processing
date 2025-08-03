\# 🧪 Lab 1 – Basic Image Processing



This lab demonstrates basic operations in Digital Image Processing using Python and OpenCV.



---



\## 🔍 Implemented Tasks



\- ✅ Extract blue color plane from an image

\- ✅ Convert RGB image to Grayscale

\- ✅ Convert RGB image to Black \& White (binary)



---



\## 📂 Folder Structure





---



\## 🖼️ Sample Results



| Original        | Black \& White     | Grayscale          | Blue Channel Only      |

|-----------------|-------------------|--------------------|------------------------|

| !\[](input/sample.jpg) | !\[](output/output\_bw.jpg) | !\[](output/output\_gray.jpg) | !\[](output/output\_OnlyBluePlane.jpg) |



---



\## 🐍 Python Scripts



\- \*\*OnlyBluePlane.py\*\*  

&nbsp; Extracts only the blue channel by zeroing out red and green.



\- \*\*rgbToGray.py\*\*  

&nbsp; Converts the image to grayscale using `cv2.cvtColor`.



\- \*\*rgbToBlackWhite.py\*\*  

&nbsp; Applies binary thresholding to convert to black \& white.



---



\## ⚙️ Requirements



Install required libraries using:



```bash

pip install -r ../requirements.txt



