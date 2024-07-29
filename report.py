import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import sys
import webbrowser
import os

video_path = sys.argv[1] if len(sys.argv) > 1 else None
cap = None

def play_video():
    global cap, video_label

    if video_path:
        cap = cv2.VideoCapture(video_path)
        update_frame()

def update_frame():
    global cap, video_label

    if cap:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_height, frame_width, _ = frame.shape
            new_width = int(frame_height * frame_width / frame_height)
            frame = cv2.resize(frame, (new_width, int(frame_height)))

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            video_label.imgtk = imgtk
            video_label.config(image=imgtk)
            video_label.after(10, update_frame)
        else:
            cap.release()

def generate_report():
    pdf_path = os.path.abspath('./COS40005-G1B/Report-Design.pdf')
    if os.path.isfile(pdf_path):
        webbrowser.open_new(f'file://{pdf_path}')
    else:
        messagebox.showerror("Error", f"File not found: {pdf_path}")

def display_heatmap():
    heatmap_path = './COS40005-G1B/heatmap.png'
    if os.path.isfile(heatmap_path):
        heatmap_img = Image.open(heatmap_path)
        heatmap_img = heatmap_img.resize((heatmap_canvas.winfo_width(), heatmap_canvas.winfo_height()))
        heatmap_imgtk = ImageTk.PhotoImage(image=heatmap_img)
        heatmap_canvas.create_image(0, 0, anchor='nw', image=heatmap_imgtk)
        heatmap_canvas.imgtk = heatmap_imgtk
    else:
        messagebox.showerror("Error", f"File not found: {heatmap_path}")

# Initialize the main application window
app = tk.Tk()
app.title("Report Generation")
app.geometry("1000x750")

# Report generation button
report_button = tk.Button(app, text="Generate Report", command=generate_report)
report_button.place(relx=0.5, y=700, anchor='center')

# Canvas for video display
video_canvas = tk.Canvas(app, bg="black", width=977, height=300, highlightthickness=1, highlightbackground="black")
video_canvas.place(x=10, y=10)

# Create a label to display video frames
video_label = tk.Label(video_canvas, bg="black")
video_label.place(relx=0.5, rely=0.5, anchor='center')

# Create a canvas to display the heatmap
heatmap_canvas = tk.Canvas(app, bg="grey", width=970, height=300, highlightthickness=1, highlightbackground="black")
heatmap_canvas.place(x=10, y=320)

# Ensure the canvas height is correct
app.update_idletasks()
play_video()
display_heatmap()

# Run the application
app.mainloop()