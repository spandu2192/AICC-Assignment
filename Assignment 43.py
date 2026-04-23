import cv2
import numpy as np

# Load image
image = cv2.imread("sample.jpg")

# Check if image loaded properly
if image is None:
    print("Error: Image not found!")
    exit()

# -------------------------------
# 1. Print Image Shape
# -------------------------------
print("Image Shape (Height, Width, Channels):", image.shape)

# -------------------------------
# 2. Print Number of Channels
# -------------------------------
if len(image.shape) == 3:
    print("Number of Channels:", image.shape[2])
else:
    print("Grayscale Image (1 channel)")

# -------------------------------
# 3. Print Pixel Values
# -------------------------------
print("\nSample Pixel Values (Top-left 5x5 area):\n")
print(image[0:5, 0:5])   # First 5x5 pixels

# -------------------------------
# 4. Access Individual Pixel
# -------------------------------
x, y = 0, 0
pixel = image[x, y]
print(f"\nPixel at position (0,0): {pixel}")

# -------------------------------
# 5. Split Channels
# -------------------------------
blue, green, red = cv2.split(image)

print("\nBlue Channel Sample:\n", blue[0:5, 0:5])
print("\nGreen Channel Sample:\n", green[0:5, 0:5])
print("\nRed Channel Sample:\n", red[0:5, 0:5])

# -------------------------------
# 6. Display Image
# -------------------------------
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()