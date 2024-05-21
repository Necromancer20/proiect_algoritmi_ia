import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_matplotlib_graph(parent_frame):
    # Clear the contents of the window
    for widget in parent_frame.winfo_children():
        widget.destroy()
    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot your data with legends
    x = [1, 2, 3, 4, 5]
    y1 = [10, 20, 25, 30, 35]
    y2 = [8, 18, 22, 28, 32]
    ax.plot(x, y1, label='Data 1')
    ax.plot(x, y2, label='Data 2')

    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sample Graph')

    # Add grid
    ax.grid(True)

    # Add legend
    ax.legend()

    # Create a FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()

    # Pack the canvas into the parent frame
    canvas.get_tk_widget().pack(expand=True)