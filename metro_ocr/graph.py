import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
'''
df = pd.read_csv("metro_stations.csv")

G = nx.Graph()

for i, row in df.iterrows():
    G.add_edge(row['From'], row['To'], Time = row['Time'], Price = row['Price'])

pos = nx.spring_layout(G, seed=100, k=0.1)
nx.draw(G, pos, with_labels = True, node_size = 30, node_color = 'lightblue', font_size = 3)
labels = nx.get_edge_attributes(G, 'Time')

#nx.draw_networkx_edge_labels(G, pos, edge_labels= labels, label_pos=0.5, font_size = 6)
plt.title("Metro Station Graph")
plt.show()
'''

def load_graph_from_csv(file_path):
    df = pd.read_csv(file_path)  # Load the CSV file as a DataFrame
    graph = nx.Graph()  # Create an empty graph
    for _, row in df.iterrows():  # Loop through each row of the CSV file
        graph.add_edge(
            row['from'], 
            row['to'], 
            time=row['time'], 
            price=row['price']
        )  # Create an edge with weights (time and price)
    return graph

