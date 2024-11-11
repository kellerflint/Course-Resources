# pip install pillow

import os
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askstring
from PIL import Image, ImageDraw

class PaintApp:
    def __init__(self, root, canvas_size=(28, 28), scale=10):
        self.root = root
        self.root.title("Simple Paint App")
        
        # Scale settings
        self.canvas_size = canvas_size
        self.scale = scale
        self.display_size = (canvas_size[0] * scale, canvas_size[1] * scale)

        # Default settings
        self.brush_color = "black"
        self.brush_size = 20  # This is the display brush size
 
        # Set up Canvas
        self.canvas = tk.Canvas(root, bg="white", width=self.display_size[0], height=self.display_size[1])
        self.canvas.pack()

        # Set up PIL image to draw on and save later (true 28x28 resolution)
        self.image = Image.new("RGB", self.canvas_size, "white")
        self.draw = ImageDraw.Draw(self.image)

        # Canvas bindings
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)  # Allow single clicks to paint
        
        # Set up UI for color and brush size
        self.setup_ui()

    def setup_ui(self):
        # Label input
        self.label_button = tk.Button(self.root, text="Set Label", command=self.set_label)
        self.label_button.pack(side="left")

        # Color button
        color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        color_button.pack(side="left")

        # Clear button
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        clear_button.pack(side="left")

        # Save button
        save_button = tk.Button(self.root, text="Save", command=self.save_image)
        save_button.pack(side="left")

        # Default label
        self.label = "image"

    def set_label(self):
        label = askstring("Set Label", "Enter label for image filename:")
        if label:
            self.label = label
            print(f"Label set to '{self.label}'")

    def choose_color(self):
        color = askcolor(color=self.brush_color)[1]
        if color:
            self.brush_color = color

    def paint(self, event):
        # Calculate scaled-down coordinates for the 28x28 image
        scaled_x, scaled_y = int(event.x / self.scale), int(event.y / self.scale)

        # Draw on the displayed canvas (scaled-up, with ovals)
        x, y = event.x, event.y
        r = self.brush_size / 2
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.brush_color, outline="")

        # Draw a smaller oval on the 28x28 PIL image to represent the scaled effect
        scaled_r = max(1, int(r / self.scale))  # Ensure the brush size is at least 1 in the 28x28 scale
        self.draw.ellipse([scaled_x - scaled_r, scaled_y - scaled_r, scaled_x + scaled_r, scaled_y + scaled_r], fill=self.brush_color)

    def clear_canvas(self):
        # Clear the tkinter canvas
        self.canvas.delete("all")
        # Clear the 28x28 PIL image
        self.draw.rectangle([0, 0, *self.canvas_size], fill="white")

    def save_image(self):
        # Save the 28x28 image with the specified label
        img_number = 1
        filename = f"data/{self.label}_{img_number}.png"
        
        # Ensure filename is unique
        while os.path.exists(filename):
            img_number += 1
            filename = f"data/{self.label}_{img_number}.png"
        
        # Make directory if it doesn't exist
        os.makedirs("data", exist_ok=True)

        self.image.save(filename)
        print(f"Image saved as {filename}")

        self.clear_canvas()

# Run the application
root = tk.Tk()
app = PaintApp(root)
root.mainloop()
