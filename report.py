import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import sys
import webbrowser
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

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
    pdf_path = os.path.abspath('./Anomaly_Report.pdf')
    
    # Create a SimpleDocTemplate for the PDF with A4 page size
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()

    # Create a custom style for the header with a larger font size
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Title'],
        fontSize=24,  
        spaceAfter=24,
        textColor=colors.black,
    )

    # Create a custom "Heading 1" style
    heading1_style = ParagraphStyle(
        'Heading1',
        fontSize=12,  
        spaceAfter=8, 
        fontName='Helvetica-Bold'
    )

    # Define the content of the PDF
    content = []

    # Add the header with the custom style
    header = Paragraph("Anomaly Report", header_style)
    content.append(header)

    # Add additional content as needed
    content.append(Paragraph("Summarization:", heading1_style))
    content.append(Paragraph("Video duration:"))
    content.append(Paragraph("Number of anomalies:"))
    content.append(Paragraph("Type of anomalies:"))
    content.append(Paragraph("Most detected type:"))
    content.append(Paragraph("Longest duration of anomaly:"))
    
    content.append(Spacer(1, 16))
    content.append(Paragraph("Details:", heading1_style))
    # Add the table under the "Details" section
    table_data = [
        ['Timestamp', 'Anomaly Type', 'Duration', 'Participants', 'Confidence Level', 'Evidence'],
        ['00:01:15', 'Type A', '00:00:05', '2', '95%', 'Video Clip 1'],
        ['00:01:30', 'Type B', '00:00:10', '2', '89%', 'Video Clip 2'],
        ['00:01:45', 'Type C', '00:00:07', '3', '92%', 'Video Clip 3']
    ]
    col_widths = [70, 80, 70, 70, 95, 120] 
    table = Table(table_data, col_widths)
    # Style the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    content.append(table)

    content.append(Spacer(1, 16))
    content.append(Paragraph("Frequency and distribution of anomalies:", heading1_style))

    content.append(Spacer(1, 16))
    content.append(Paragraph("Suggestions:", heading1_style))
    content.append(Paragraph("- Most anomalies happened during the period of 00:01:00 to 00:02:00."))
    content.append(Paragraph("- More than 50 percent of the anomalies involves only 2 individuals."))

    # Generate the PDF
    doc.build(content)

    # Open the generated PDF file
    if os.path.isfile(pdf_path):
        webbrowser.open_new(f'file://{pdf_path}')
    else:
        messagebox.showerror("Error", f"Failed to generate the report: {pdf_path}")

def display_heatmap():
    heatmap_path = './heatmap.png'
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
