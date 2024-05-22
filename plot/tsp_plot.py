import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.utils import parse_files_in_folder

def draw_matplotlib_graph(parent_frame):
    """
    Function to draw matplotlib graphs in the provided tkinter frame.
    It reads data from files in the "output_data" directory with filenames containing specific keywords,
    parses the data, and plots them.
    """
    # Parse the data from the specified folder and files for both keywords
    data_backtracking = parse_files_in_folder("output_data", "tsp_backtracking", ":")
    data_nearest = parse_files_in_folder("output_data", "tsp_nearest", ":")

    # Clear the contents of the parent frame
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Create a new Matplotlib figure and two subplots (one for each data set)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Helper function to plot data
    def plot_data(ax, data, title):
        for key, value in data.items():
            data_x = []
            data_y = []
            for line in value:
                try:
                    # Convert the first element to int and the second element to float
                    data_x.append(int(line[0]))
                    data_y.append(float(line[1]))
                except (ValueError, IndexError) as e:
                    # Handle possible conversion errors or missing data
                    print(f"Error processing data from file {key}: {e}")
                    continue
            # Plot the data with labels
            ax.plot(data_x, data_y, label=key)
        
        # Set the labels and title for the plot
        ax.set_xlabel('Board Size')
        ax.set_ylabel('Time (s)')
        ax.set_title(title)

        # Enable grid on the plot
        ax.grid(True)

        # Add a legend to the plot
        ax.legend()

    # Plot data for tsp_backtracking
    plot_data(ax1, data_backtracking, 'TSP Backtracking Algorithms Performance')

    # Plot data for tsp_nearest
    plot_data(ax2, data_nearest, 'TSP Nearest Neighbor Algorithms Performance')

    # Create a FigureCanvasTkAgg object to embed the plot in the tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()

    # Pack the canvas into the parent frame and allow it to expand
    canvas.get_tk_widget().pack(expand=True)

