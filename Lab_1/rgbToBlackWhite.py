import cv2

img = cv2.imread(r'C:\Users\LOQ\Desktop\Sem5\Dip\Lab_1\SampleImage.jpeg')

if img is None:
    print("Failed to load image.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Black and White", bw)
    cv2.imwrite(r'C:\Users\LOQ\Desktop\Sem5\Dip\Lab_1\output_bw.jpg', bw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
