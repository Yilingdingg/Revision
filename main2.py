import cv2

new_rgb_rainbow=cv2.imread("RGB_rainbow.jpg")
new_hsl_rainbow=cv2.imread("HSL_rainbow.jpg")

convertion=cv2.cvtColor(new_rgb_rainbow, cv2.COLOR_RGB2HSV)
cv2.imshow("Convertion", convertion)
cv2.imwrite("RGB_rainbow_2.jpg", convertion)

cv2.waitKey(0)
cv2.destroyAllWindows()

convertion_2=cv2.cvtColor(new_hsl_rainbow, cv2.COLOR_HLS2RGB)
cv2.imshow("ConvertiOn", convertion_2)
cv2.imwrite("HSL_rainbow_2.jpg", convertion_2)

cv2.waitKey(0)
cv2.destroyAllWindows()

rotation_image=cv2.rotate(new_hsl_rainbow, cv2.ROTATE_180)
cv2.imshow("Rotation", rotation_image)

cv2.waitKey(0)
cv2.destroyAllWindows()