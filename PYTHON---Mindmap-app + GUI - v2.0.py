import tkinter as tk
from tkinter import simpledialog, colorchooser, messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Function to create the mind map
def create_mind_map(title, nodes, connections, color):
    G = nx.Graph()
    
    # Add nodes to the graph
    for node in nodes:
        G.add_node(node)
    
    # Add edges to the graph based on connections
    for conn in connections:
        G.add_edge(conn[0], conn[1])

    # Draw the mind map
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=color, node_size=3000, font_size=10, font_color='white', font_weight='bold')
    plt.title(title)
    plt.show()

# Function to collect user input through GUI
def get_user_input():
    # Fetch title
    title = simpledialog.askstring("Input", "Enter Mind Map Title:")
    
    if not title:
        messagebox.showerror("Error", "Title cannot be empty!")
        return

    # Fetch nodes
    nodes_input = simpledialog.askstring("Input", "Enter nodes (comma-separated):")
    if not nodes_input:
        messagebox.showerror("Error", "You must provide at least one node!")
        return
    nodes = [n.strip() for n in nodes_input.split(',')]

    # Fetch connections
    connections = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if messagebox.askyesno("Connection", f"Do you want to connect {nodes[i]} and {nodes[j]}?"):
                connections.append((nodes[i], nodes[j]))

    # Choose color for nodes
    color = colorchooser.askcolor(title="Choose Node Color")[1]
    if not color:
        messagebox.showerror("Error", "Color selection is required!")
        return

    # Create the mind map
    create_mind_map(title, nodes, connections, color)

# Create GUI window
def create_gui():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Show prompt for mind map creation
    if messagebox.askyesno("Create Mind Map", "Do you want to create a new mind map?"):
        get_user_input()
    else:
        messagebox.showinfo("Exit", "Exiting the program.")
        root.quit()

# Run the GUI
if __name__ == "__main__":
    create_gui()
