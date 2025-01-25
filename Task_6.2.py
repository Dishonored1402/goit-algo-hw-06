import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)])

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None

def bfs(graph, start, end):
    visited = set()
    queue = [[start]]
    if start == end:
        return [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == end:
                    return new_path
            visited.add(node)
    return None

start_node = 1
end_node = 6
dfs_path = dfs(G, start_node, end_node)
print(f"Шлях за допомогою DFS: {dfs_path}")

bfs_path = bfs(G, start_node, end_node)
print(f"Шлях за допомогою BFS: {bfs_path}")

nx.draw(G, with_labels=True, node_color='skyblue', font_weight='bold', node_size=500)
plt.show()
