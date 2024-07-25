import tkinter as tk
from tkinter import font, filedialog

# Initialize the main application window
app = tk.Tk()
app.title("Anomaly Detection")
app.geometry("1000x750")
app.resizable(False, False)

# Define a larger font
heading_font = font.Font(size=14, weight="normal")
label_font = font.Font(size=12, weight="bold")

# Function to upload a video
def upload_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    if file_path:
        # Placeholder for video handling logic
        print(f"Selected video: {file_path}")

# Function to upload JSON
def upload_JSON():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        # Placeholder for video handling logic
        print(f"Selected JSON: {file_path}")

# 1. Main Settings
main_settings_frame = tk.Frame(app, width=333, height=750, bg="lightgray")
main_settings_frame.pack(side="left", fill="y")
main_settings_label = tk.Label(main_settings_frame, text="MAIN SETTINGS", bg="lightgray", font=heading_font)
main_settings_label.place(relx=0.5, rely=0.05, anchor='n')

# Video upload
video_upload_label = tk.Label(main_settings_frame, bg="lightgray", text="Video upload", font=label_font)
video_upload_label.place(x=15, y=140)
video_upload_canvas = tk.Canvas(main_settings_frame, width=300, height=170, bg="white", bd=2, highlightthickness=1, highlightbackground="black")
video_upload_canvas.place(relx=0.5, y=170, anchor='n')
video_upload_button = tk.Button(main_settings_frame, text="Browse File", command=upload_video)
video_upload_button.place(x=20, y=315,)

# JSON upload
JSON_upload_label = tk.Label(main_settings_frame, bg="lightgray", text="JSON upload", font=label_font)
JSON_upload_label.place(x=15, y=360)
JSON_upload_canvas = tk.Canvas(main_settings_frame, width=300, height=170, bg="white", bd=2, highlightthickness=1, highlightbackground="black")
JSON_upload_canvas.place(relx=0.5, y=390, anchor='n')
JSON_upload_button = tk.Button(main_settings_frame, text="Browse File", command=upload_JSON)
JSON_upload_button.place(x=20, y=535,)

# Create the upload button at the bottom
upload_button = tk.Button(main_settings_frame, width= 10, text="Upload")
upload_button.place(relx=1.0, rely=1.0, x=-120, y=-20, anchor='se')

# Create the clear button at the bottom
clear_button = tk.Button(main_settings_frame, width= 10, text="Clear")
clear_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor='se')

# 2. Video Configuration
video_config_frame = tk.Frame(app, width=667, height=750, bg="white")
video_config_frame.pack(side="right", fill="both", expand=True)
video_config_label = tk.Label(video_config_frame, text="VIDEO CONFIGURATION", bg="white", font=heading_font)
video_config_label.place(relx=0.5, rely=0.05, anchor='n')

# Video canvas
video_canvas = tk.Canvas(video_config_frame, width=620, height=200, bg="lightgrey", bd=2, highlightthickness=1, highlightbackground="black")
video_canvas.place(relx=0.5, y=140, anchor='n')
video_canvas.create_text(300, 100, text="VIDEO HERE", fill="black")

# Homography canvas
homography_canvas = tk.Canvas(video_config_frame, width=300, height=40, bg="white", bd=2, highlightthickness=1, highlightbackground="black")
homography_canvas.place(x=21, y=360, anchor='nw')
homography_canvas.create_text(150, 23, text="HOMOGRAPHY CONVERSION", fill="black")

# Create the Start button
start_button = tk.Button(video_config_frame, width= 10, text="Start")
start_button.place(x=21, y=420, anchor='nw')

# Create the Stop button
stop_button = tk.Button(video_config_frame, width= 10, text="Stop")
stop_button.place(x=126, y=420, anchor='nw')

# Create the Reset button
reset_button = tk.Button(video_config_frame, width= 10, text="Reset")
reset_button.place(x=231, y=420, anchor='nw')

# Advanced configuration canvas
advanced_config_canvas = tk.Canvas(video_config_frame, width=300, height=40, bg="white", bd=2, highlightthickness=1, highlightbackground="black")
advanced_config_canvas.place(x=21, y=465, anchor='nw')
advanced_config_canvas.create_text(150, 23, text="ADVANCED CONFIGURATION", fill="black")

# Assume configuration canvas
assume_config_canvas = tk.Canvas(video_config_frame, width=620, height=160, bg="lightgrey", bd=2, highlightthickness=1, highlightbackground="black")
assume_config_canvas.place(relx=0.5, y=525, anchor='n')
assume_config_canvas.create_text(300, 90, text="ASSUME CONFIGURATION SECTIONS", fill="black")

# Create the Execute button at the bottom right
execute_button = tk.Button(video_config_frame, width= 10, text="Execute")
execute_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor='se')

# Run the application
app.mainloop()
