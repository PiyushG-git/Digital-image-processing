import cv2
import numpy as np
# Correct usage of raw string
image = cv2.imread(r'C:\Users\LOQ\Desktop\Sem5\Dip\Lab_1\SampleImage.jpeg')  

if image is None:
    print(" Failed to load image.")
else:
    blue_only = image.copy()
    # Green channel set to 0
    blue_only[:, :, 1] = 0  
    # Red channel set to 0
    blue_only[:, :, 2] = 0  

    cv2.imshow("Only Blue Plane", blue_only)  
    cv2.imwrite(r'C:\Users\LOQ\Desktop\Sem5\Dip\Lab_1\output_OnlyBluePlane.jpg', blue_only)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()
