import cv2

# Load image
image = cv2.imread("sample2.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# -------------------------------
# 1. Convert to Grayscale
# -------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -------------------------------
# 2. Apply Blur
# -------------------------------
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# -------------------------------
# 3. Edge Detection
# -------------------------------
edges = cv2.Canny(blur, 50, 150)

# -------------------------------
# 4. Show Results
# -------------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Edge Detection", edges)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()