import cv2
import json
import numpy as np


# Load the video
cap = cv2.VideoCapture('violence.mp4')
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / int(cap.get(cv2.CAP_PROP_FPS))

# Load the data from frames_id.json
with open('frames_id.json') as f:
    data = json.load(f)

fps = len(data) / video_length

# Loop through each frame in the data
for frame_index in range(len(data)):
    frame_data = data[f"frame {frame_index}"]
    bg_map = np.ones((480, 640, 3), np.uint8) * 255
    
    # Read the current frame from the video
    ret, current_frame = cap.read()
    if not ret:
        break  # Dừng nếu không còn khung hình nào

    # Display the person positions in the image with center points
    for person in frame_data:
        bbox = person["bbox"]
        x1, y1, x2, y2 = map(int, bbox)
        center_x = (x1 + x2) // 2
        center_y = y2
        cv2.rectangle(current_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.circle(current_frame, (center_x, center_y), 5, (0, 255, 0), -1)
        cv2.circle(bg_map, (center_x, center_y), 5, (0, 255, 0), -1)

    # Display the image with person positions and center points
    cv2.imshow('Person Positions with Center Points', current_frame)

    tl = (340, 110)
    bl = (23, 208)
    tr = (600, 170)
    br_bl = (100, 360)
    br_tr = (640, 360)

    # Vector 1: bl + br_bl
    vector1 = (br_bl[0] - bl[0], br_bl[1] - bl[1])

    # Vector 2: tr + br_tr
    vector2 = (br_tr[0] - tr[0], br_tr[1] - tr[1])

    # Calculate the intersection point
    det = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    t = ((tr[0] - bl[0]) * vector2[1] - (tr[1] - bl[1]) * vector2[0]) / det
    br = (int(bl[0] + t * vector1[0]), int(bl[1] + t * vector1[1]))
    # print("Intersection Point:", br)

    # Define the homography matrix
    points_original = np.float32([tl, tr, bl, br])
    points_bird_eye = np.float32([[0, 0], [640, 0], [0, 360], [640, 360]])
    homography_matrix, _ = cv2.findHomography(points_original, points_bird_eye)

    # Convert the image to a 2D map using homography
    bird_eye_view = cv2.warpPerspective(bg_map, homography_matrix, (640, 360))

    # Display the 2D map image
    cv2.imshow('2D Map (Homography Conversion)', bird_eye_view)
    cv2.waitKey(int(1000 / fps))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()