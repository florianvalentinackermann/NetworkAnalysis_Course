#importing the libraries
import networkx as nx
import numpy as np
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import osmnx as ox #for saving network to a shapefile
import geopandas as gpd
from shapely.geometry import Point, LineString
import momepy
import pandas as pd

#initializing an empty (here undirected) graph
N = nx.Graph()
# add nodes
N.add_node("Genf", y=46.188956, x=6.135104)
N.add_node("Lausanne", y=46.527564, x=6.618360)
N.add_node("Yverdon", y=46.788984, x=6.636190)
# add edges
N.add_edge("Genf","Lausanne", weight=6)
N.add_edge("Genf","Yverdon", weight=1)
N.add_edge("Lausanne","Yverdon", weight=2)





# Create a directed graph
L = nx.DiGraph()

# Add nodes with coordinates
nodes_with_coordinates = {
    1: {'x': 0, 'y': 0},
    2: {'x': 1, 'y': 0},
    3: {'x': 1, 'y': 1},
    4: {'x': 0, 'y': 1},
}
L.add_nodes_from(nodes_with_coordinates)


# Add weighted edges
edges = [(1, 2, {'weight': 0.5}), (2, 3, {'weight': 0.8}), (3, 4, {'weight': 1.2}), (4, 1, {'weight': 0.7})]
L.add_edges_from(edges)

# Extract node and edge information
nodes_data = L.nodes(data=True)
edges_data = L.edges(data=True)

# Create DataFrames for nodes and edges
nodes_df = pd.DataFrame(nodes_data, columns=['Node', 'Node_Data'])
edges_df = pd.DataFrame(edges_data, columns=['Source', 'Target', 'Edge_Data'])

# Extract weight from Edge_Data and add it as a separate column
edges_df['Weight'] = edges_df['Edge_Data'].apply(lambda x: x['weight'])

# Display DataFrames
print("Nodes DataFrame:")
print(nodes_df)

print("\nEdges DataFrame:")
print(edges_df)

# Save DataFrames to CSV files
nodes_df.to_csv('nodes.csv', index=False)
edges_df.to_csv('edges.csv', index=False)

import os

print("Current Working Directory:", os.getcwd())