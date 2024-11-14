# Importing necessary libraries
import numpy as np
import cv2

# Function to calculate the average pixel intensity around each detected circle
def av_pix(img, circles, size):
    av_value = []
    for coords in circles[0, :]:
        # Calculate the mean pixel value around each detected circle (within a square of side 2*size centered on the circle)
        col = np.mean(img[coords[1] - size:coords[1] + size, coords[0] - size:coords[0] + size])
        av_value.append(col)
    return av_value

# Function to retrieve the radius of each detected circle
def get_radius(circles):
    radius = []
    for coords in circles[0, :]:
        # Append the radius of each detected circle to the radius list
        radius.append(coords[2])
    return radius

# Read the image in grayscale mode
img = cv2.imread('Coins_Picture.png', cv2.IMREAD_GRAYSCALE)
# Read the original image in color mode
original_image = cv2.imread('Coins_Picture.png', 1)
# Apply Gaussian Blur to reduce noise and improve circle detection
img = cv2.GaussianBlur(img, (5, 5), 0)

# Detect circles in the image using Hough Circle Transform
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 0.9, 120, param1=50, param2=27, minRadius=60, maxRadius=120)
print(circles)  # Print the detected circles for verification

# Round the detected circle coordinates to integer values
circles = np.uint16(np.around(circles))
count = 1  # Counter to label each detected circle if needed

# Loop through each detected circle to draw them on the original image
for i in circles[0, :]:
    # Draw the outer circle in green
    cv2.circle(original_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # Draw the center of the circle in red
    cv2.circle(original_image, (i[0], i[1]), 2, (0, 0, 255), 3)
    count += 1

# Calculate radii and average brightness values for each circle
radii = get_radius(circles)
print(radii)  # Print the radii for verification
bright_values = av_pix(img, circles, 20)
print(bright_values)  # Print brightness values for verification

# Determine coin values based on brightness and radius thresholds
values = []
for a, b in zip(bright_values, radii):
    if a > 150 and b > 110:
        values.append(10)
    elif a > 150 and b <= 110:
        values.append(5)
    elif a < 150 and b > 110:
        values.append(2)
    elif a < 150 and b < 110:
        values.append(1)
print(values)  # Print values assigned to each detected coin

# Display the value of each coin near its center on the image
count_2 = 0
for i in circles[0, :]:
    cv2.putText(original_image, str(values[count_2]) + 'p', (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    count_2 += 1

# Display the estimated total value of all detected coins on the image
cv2.putText(original_image, 'ESTIMATED TOTAL VALUE: ' + str(sum(values)) + 'p', (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.3, 255)

# Resize the image to make it smaller before displaying
scale_percent = 50  # Percentage of the original size
width = int(original_image.shape[1] * scale_percent / 100)
height = int(original_image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(original_image, dim, interpolation=cv2.INTER_AREA)

# Show the final resized image with annotated values
cv2.imshow('Detected Coins', resized_image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows