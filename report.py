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
        home_btn = tk.Button(nav_bar, text="Home", command=self.home_navigate)
        home_btn.place(x=10, y=10)

        # Export report button
        export_btn = tk.Button(nav_bar, text="Export Report", command=self.export_report)
        export_btn.place(x=62, y=10)

        # Canvas for video display
        self.canvas = tk.Canvas(root, bg="black", width=975, height=300)
        self.canvas.place(x=10, y=80)

        # Future function block
        self.future_function_block = tk.Label(root, text="Heat map", bg="grey", width=139, height=23)
        self.future_function_block.place(x=10, y=390)

    def home_navigate(self):
        pass

    def export_report(self):
        # Functionality to export report
        messagebox.showinfo("Export Report", "Report exported successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoApp(root)
    root.mainloop()