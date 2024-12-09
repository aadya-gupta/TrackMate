from load_graph import load_graph_from_csv
from dijkstra import shortest_path
from display import display_shortest_path

def main():
    G = load_graph_from_csv("metro_stations.csv")
    station_list = list(G.nodes)
    welcome = f"Welcome to TrackMate! Let me ease your travel planning today."
    print(welcome)

    while True:
        source = input("\nEnter the starting station: ").strip().lower()
        target = input("Enter the destination station: ").strip().lower()
        weight = input("Find the shortest path based on (time/price): ").strip().lower()

        if source not in G.nodes or target not in G.nodes:
            print("\nInvalid source or target station. Please try again.")
            continue

        if weight not in ['time', 'price']:
            print("\nInvalid weight type. Please enter 'time' or 'price'.")
            continue

        try:
            path, distance = shortest_path(G, source, target, weight)
            display_shortest_path(path, source, target, distance, weight)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

        choice = input("\nDo you want to find another path? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nThank you for using the Metro Shortest Path Finder! Goodbye.")
            break

if __name__ == "__main__":
    main()
