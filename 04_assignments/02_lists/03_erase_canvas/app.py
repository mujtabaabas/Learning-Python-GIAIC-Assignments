import tkinter as tk
from tkinter import colorchooser

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()

        self.cells = []
        self.paint_color = 'blue'
        self.mode = 'erase'  # Options: 'erase', 'paint'
        self.eraser = None

        self.draw_grid()
        self.create_controls()

        self.canvas.bind("<Button-1>", self.start_tool)
        self.canvas.bind("<Motion>", self.use_tool)

        root.bind("e", self.set_erase_mode)
        root.bind("p", self.set_paint_mode)
        root.bind("c", self.clear_canvas)

    def draw_grid(self):
        self.cells.clear()
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill='blue', outline='black'
                )
                self.cells.append(cell)

    def create_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        self.mode_label = tk.Label(control_frame, text="Mode: Erase", font=('Arial', 12))
        self.mode_label.pack(side=tk.LEFT, padx=10)

        color_btn = tk.Button(control_frame, text="🎨 Pick Color", command=self.pick_color)
        color_btn.pack(side=tk.LEFT)

        clear_btn = tk.Button(control_frame, text="🧹 Clear Canvas", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT)

    def pick_color(self):
        color = colorchooser.askcolor(title="Choose a color")[1]
        if color:
            self.paint_color = color
            self.mode = 'paint'
            self.update_mode_label()

    def update_mode_label(self):
        self.mode_label.config(text=f"Mode: {'Paint' if self.mode == 'paint' else 'Erase'}")

    def set_erase_mode(self, event=None):
        self.mode = 'erase'
        self.update_mode_label()

    def set_paint_mode(self, event=None):
        self.mode = 'paint'
        self.update_mode_label()

    def start_tool(self, event):
        if self.eraser is None:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE,
                fill='pink', outline='black'
            )

    def use_tool(self, event):
        if self.eraser:
            x1, y1 = event.x, event.y
            x2, y2 = x1 + ERASER_SIZE, y1 + ERASER_SIZE
            self.canvas.coords(self.eraser, x1, y1, x2, y2)

            overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
            for item in overlapping:
                if item != self.eraser:
                    new_color = 'white' if self.mode == 'erase' else self.paint_color
                    self.canvas.itemconfig(item, fill=new_color)

    def clear_canvas(self, event=None):
        for cell in self.cells:
            self.canvas.itemconfig(cell, fill='blue')

def main():
    root = tk.Tk()
    root.title("🎮 Canvas Paint & Eraser")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
