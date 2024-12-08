import matplotlib.pyplot as plt
import networkx as nx
from load_graph import load_graph_from_csv

def display_shortest_path(path, source, target, distance, weight):
    G = load_graph_from_csv("metro_stations.csv")
    path_edges = list(zip(path, path[1:]))
    details = f"Shortest path from {source} to {target}: " + "->".join(path) + f"\nTotal {weight.capitalize()}: {distance}"
    print(details)

    fig, ax = plt.subplots(figsize = (8, 6))
    pos = nx.spring_layout(G, seed = 160, k = 0.1)
    nx.draw(G, pos, with_labels = True, node_size = 30, node_color = "lightblue", font_size = 5)
    nx.draw_networkx_edges(G, pos, edgelist = path_edges, edge_color= "red", width= 2, ax = ax)
    
    plt.show()



