import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.utils import parse_files_in_folder

def draw_matplotlib_graph(parent_frame):
    """
    Function to draw a matplotlib graph in the provided tkinter frame.
    It reads data from files in the "output_data" directory with filenames containing "queens",
    parses the data, and plots it.
    """
    # Parse the data from the specified folder and files
    read_data = parse_files_in_folder("output_data", "queens", ":")

    # Clear the contents of the parent frame
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Create a new Matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(15, 7))

    # Iterate over the parsed data to plot each dataset
    for key, value in read_data.items():
        data_x = []
        data_y = []
        for data in value:
            try:
                # Convert the first element to int and the second element to float
                data_x.append(int(data[0]))
                data_y.append(float(data[1]))
            except (ValueError, IndexError) as e:
                # Handle possible conversion errors or missing data
                print(f"Error processing data from file {key}: {e}")
                continue
        
        # Plot the data with labels
        ax.plot(data_x, data_y, label=key.replace("solve", "").replace("results", "").replace("_", " ").strip())

    # Set the labels and title for the plot
    ax.set_xlabel('Board Size')
    ax.set_ylabel('Time (s)')
    ax.set_title('Queen Algorithms Performance')

    # Enable grid on the plot
    ax.grid(True)

    # Add a legend to the plot
    ax.legend()

    # Create a FigureCanvasTkAgg object to embed the plot in the tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()

    # Pack the canvas into the parent frame and allow it to expand
    canvas.get_tk_widget().pack(expand=True)

