import networkx as nx
import pandas as pd


def load_graph_from_csv(file):
    df = pd.read_csv(file)
    df['From'] = df['From'].str.strip().str.lower()
    df['To'] = df['To'].str.strip().str.lower()
    graph = nx.Graph()
    for _, row in df.iterrows():
        graph.add_edge(
            row['From'].lower(),
            row['To'].lower(),
            time = row['Time'],
            price = row['Price']
        )
    return graph