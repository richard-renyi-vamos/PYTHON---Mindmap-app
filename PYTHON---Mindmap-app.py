import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MindMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind Map App")
        
        self.graph = nx.Graph()
        
        self.label = tk.Label(root, text="Enter node:")
        self.label.pack()
        
        self.node_entry = tk.Entry(root)
        self.node_entry.pack()
        
        self.parent_label = tk.Label(root, text="Enter parent node (optional):")
        self.parent_label.pack()
        
        self.parent_entry = tk.Entry(root)
        self.parent_entry.pack()
        
        self.add_node_btn = tk.Button(root, text="Add Node", command=self.add_node)
        self.add_node_btn.pack()
        
        self.display_map_btn = tk.Button(root, text="Display Mind Map", command=self.display_mind_map)
        self.display_map_btn.pack()
        
    def add_node(self):
        node = self.node_entry.get()
        parent = self.parent_entry.get()
        
        if node:
            self.graph.add_node(node)
            if parent:
                self.graph.add_edge(parent, node)
            self.node_entry.delete(0, tk.END)
            self.parent_entry.delete(0, tk.END)
    
    def display_mind_map(self):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMapApp(root)
    root.mainloop()
