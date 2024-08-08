import cv2
import json
import numpy as np

# Load the image
image = cv2.imread('violence_frame.jpg')

# Load the data from frames_id.json
with open('frames_id.json') as f:
    data = json.load(f)

# Extract the data for frame 0
frame_data = data["frame 0"]
bg_map = np.ones((480, 640, 3), np.uint8) * 255

# Display the person positions in the image with center points
for person in frame_data:
    bbox = person["bbox"]
    x1, y1, x2, y2 = map(int, bbox)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.circle(image, (center_x, center_y), 5, (0, 255, 0), -1)
    cv2.circle(bg_map, (center_x, center_y), 5, (0, 255, 0), -1)

# Display the image with person positions and center points
cv2.imshow('Person Positions with Center Points', image)

tl = (302, 102)
bl = (23, 208)
tr = (600, 170)
br = (325, 360)
extra = ()

cv2.circle(image, tl, 5, (0, 0, 255), cv2.FILLED)
cv2.circle(image, bl, 5, (0, 0, 255), cv2.FILLED)
cv2.circle(image, tr, 5, (0, 0, 255), cv2.FILLED)
cv2.circle(image, br, 5, (0, 0, 255), cv2.FILLED)

# Define the homography matrix
points_original = np.float32([tl, tr, bl, br])
points_bird_eye = np.float32([[0, 0], [640, 0], [0, 360], [640, 360]])
homography_matrix, _ = cv2.findHomography(points_original, points_bird_eye)

# Convert the image to a 2D map using homography
bird_eye_view = cv2.warpPerspective(bg_map, homography_matrix, (640, 360))

# Display the 2D map image
cv2.imshow('2D Map (Homography Conversion)', bird_eye_view)

cv2.waitKey(0)
cv2.destroyAllWindows()