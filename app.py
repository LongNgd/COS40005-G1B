import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import cv2

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x750")
        self.root.title("Anomaly detection")
        self.root.resizable(False, False)

        # Navigation bar
        nav_bar = tk.Frame(root, height=50)
        nav_bar.pack(fill=tk.X, side=tk.TOP)

        # Upload video button
        upload_btn = tk.Button(nav_bar, text="Upload Video", command=self.upload_video)
        upload_btn.place(x=10, y=10)

        # Export report button
        export_btn = tk.Button(nav_bar, text="Export Report", command=self.export_report)
        export_btn.place(x=100, y=10)

        # Slicer
        slicer_label = tk.Label(root, text="Switch to")
        slicer_label.place(x=10, y=70)
        self.slicer = ttk.Combobox(root, values=["Cam 1", "Cam 2", "Cam 3"], state="readonly")
        self.slicer.place(x=80, y=70)
        self.slicer.current(0)

        # Canvas for video display
        self.canvas = tk.Canvas(root, bg="black", width=975, height=280)
        self.canvas.place(x=10, y=100)

        # Future function block
        self.future_function_block = tk.Label(root, text="Heat map", bg="grey", width=139, height=23)
        self.future_function_block.place(x=10, y=390)

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.play_video(file_path)

    def play_video(self, file_path):
        cap = cv2.VideoCapture(file_path)
        canvas_height = self.canvas.winfo_height()
        while True:
            ret, frame = cap.read()
            if not ret:
                # Rewind the video to the beginning
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Restart the loop
            # Calculate proportional width based on canvas height
            frame_width = int(frame.shape[1] * (canvas_height / frame.shape[0]))
            # Resize frame
            frame = cv2.resize(frame, (frame_width, canvas_height))
            # Calculate the horizontal offset to center the frame
            x_offset = (self.canvas.winfo_width() - frame_width) // 2
            # Convert BGR to RGB for tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Create a PhotoImage from the frame
            img = tk.PhotoImage(data=cv2.imencode('.png', frame_rgb)[1].tobytes())
            # Display the image on the canvas
            self.canvas.create_image(x_offset, 0, anchor=tk.NW, image=img)
            self.root.update()  # Update the canvas

    def export_report(self):
        # Functionality to export report
        messagebox.showinfo("Export Report", "Report exported successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoApp(root)
    root.mainloop()
