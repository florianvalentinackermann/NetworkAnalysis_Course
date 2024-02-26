# Importing the libraries
import networkx as nx
import numpy as np
import matplotlib

# Checking the version
print("NetworkX version:", nx.__version__)
print("NumPy version:", np.__version__)

# Initializing an empty  graph
G = nx.Graph()

# Adding the nodes
G.add_node("Genf")
G.add_node("Lausanne")
G.add_node("Brig")
G.add_node("Yverdon")
G.add_node("Biel")
G.add_node("Basel")
G.add_node("Olten")
G.add_node("Bern")
G.add_node("Spiez")
G.add_node("Interlaken")
G.add_node("Luzern")
G.add_node("Zürich")
G.add_node("Arth-Goldau")
G.add_node("Lugano")
G.add_node("Chur")
G.add_node("St.Gallen")
G.add_node("St.Margrethen")
G.add_node("Frauenfeld")
G.add_node("Weinfelden")
G.add_node("Romanshorn")
G.add_node("Konstanz")

# Adding the weighted edges
G.add_edge("Genf","Lausanne", weight=6)
G.add_edge("Lausanne","Brig", weight=2)
G.add_edge("Genf","Yverdon", weight=1)
G.add_edge("Yverdon","Biel", weight=3)
G.add_edge("Biel","Basel", weight=2)
G.add_edge("Biel","Olten", weight=2)
G.add_edge("Lausanne","Yverdon", weight=2)
G.add_edge("Lausanne","Bern", weight=2)
G.add_edge("Bern","Spiez", weight=4)
G.add_edge("Spiez","Interlaken", weight=2)
G.add_edge("Spiez","Brig", weight=2)
G.add_edge("Bern","Luzern", weight=2)
G.add_edge("Bern","Olten", weight=2)
G.add_edge("Olten","Basel", weight=3)
G.add_edge("Olten","Luzern", weight=1)
G.add_edge("Olten","Zürich", weight=2)
G.add_edge("Zürich","Basel", weight=2)
G.add_edge("Zürich","Bern", weight=4)
G.add_edge("Zürich","Arth-Goldau", weight=1)
G.add_edge("Luzern","Arth-Goldau", weight=1)
G.add_edge("Arth-Goldau","Lugano", weight=2)
G.add_edge("Zürich","Chur", weight=2)
G.add_edge("Zürich","St.Gallen", weight=2)
G.add_edge("St.Gallen","St.Margrethen", weight=1)
G.add_edge("Zürich","Frauenfeld", weight=4)
G.add_edge("Frauenfeld","Weinfelden", weight=2)
G.add_edge("Weinfelden","Romanshorn", weight=1)
G.add_edge("Weinfelden","Konstanz", weight=1)

# Plot the graph with matplotlib
pos=nx.random_layout(G)
plt.figure(figsize=(10,7))
nx.draw(G, node_size=90, node_color="cyan", with_labels=True)
plt.show()

# Plot with edge thickness
pos = nx.spring_layout(G)
edges = G.edges()
weights = [G[u][v]['weight'] for u,v in edges]
nx.draw(G, pos, with_labels=True, width=weights)  # Plot the graph with edge thickness representing their weight
plt.show()

# Create an adjacency matrix
adjmatrix=nx.adjacency_matrix(G)
print(adjmatrix.todense())

# Create a numpy array
G_array=nx.to_numpy_array(G)
# Save the matrix to a file for further investigation with Gephi
np.savetxt( "C:\\Users\\flori\\OneDrive\\Desktop\\HS 2023\\Data Science and network analysis\\SBB_IC.txt", G_array, fmt="%d",delimiter=";")

# Get the node degrees
c = G.degree()

# Calculate degree distribution
degree_sequence = [degree for node, degree in G.degree()]
degree_count = nx.degree_histogram(G)

# Plot degree distribution
degrees = range((len(degree_count))//21)
plt.bar(degrees, degree_count)
plt.title("")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# Calculate centrality
print(nx.betweenness_centrality(G))
print(nx.closeness_centrality(G))
# Clustering coefficient
print(nx.clustering(G))
# Graph density
print("graph density: ", nx.density(G))

# Calculate the average clustering coefficient for the whole network
avg_clustering = nx.average_clustering(G)
print(f"The average clustering coefficient is: {avg_clustering}")

# Save the file
nx.write_graphml(G,"C:\\Users\\flori\\OneDrive\\Desktop\\HS 2023\\Data Science and network analysis\\graph_no1.graphml")


