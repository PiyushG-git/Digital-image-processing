import cv2

src = cv2.imread(r'C:\Users\LOQ\Desktop\Sem5\Dip\Lab_1\SampleImage.jpeg')

if src is None:
    print("Failed to load image.")
else:
    gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_img)
    cv2.imwrite(r'C:\Users\LOQ\Desktop\Sem5\Dip\Lab_1\output_gray.jpg', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
