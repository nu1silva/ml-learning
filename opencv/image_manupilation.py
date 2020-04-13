import cv2
import imutils

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread('friends-1.jpg')
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# get pixel and print RGB values
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# Setting ROI
roi = image[360:960, 320:920]
cv2.imshow("ROI", roi)

# Resize image
resized = cv2.resize(image, (200, 200))
cv2.imshow("Resized image", resized)

# resize based on aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)

# calculate aspect ration with imutils
resized = imutils.resize(image, width=500)
cv2.imshow("Aspect Ratio Resize with imutils", resized)

# rotating images
center_image = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center_image, -45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated Image", rotated_image)

# scale and rotate image (since its huge!!!)
rotated = imutils.resize(image, width=500)
rotated = imutils.rotate_bound(rotated, 45)
cv2.imshow("Imutils Bound Rotation", rotated)

# put text on the image
resized = imutils.resize(image, width=700)
output = resized.copy()
cv2.putText(output, "Friends + OpenCV", (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("image with text", output)

cv2.waitKey(0)
