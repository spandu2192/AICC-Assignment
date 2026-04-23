import cv2

# Load image
image = cv2.imread("sample.jpg")  # Replace with your image path

if image is None:
    print("Error: Image not found!")
    exit()

# Show original image
cv2.imshow("Original Image", image)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)

# Apply blur
blur = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Blurred Image", blur)

# Edge detection
edges = cv2.Canny(blur, 50, 150)
cv2.imshow("Edge Detection", edges)

# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()