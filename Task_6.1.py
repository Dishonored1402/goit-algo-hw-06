import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Alice", "Bob", "Charlie", "David", "Eve"])

G.add_edges_from([("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "Eve")])

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold")
plt.title("Соціальна мережа")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degrees}")