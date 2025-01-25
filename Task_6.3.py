import networkx as nx
import heapq

G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 4), (1, 3, 1), (2, 3, 2), (2, 4, 5), (3, 4, 1)])

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

start_node = 1
shortest_paths = dijkstra(G, start_node)

print(f"Найкоротші шляхи від вершини {start_node}:")
for node, distance in shortest_paths.items():
    print(f"До вершини {node}: {distance}")
