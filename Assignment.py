graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)]
}

H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def heuristic_cost(path):
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost, last_node

path = [('S', 0), ('A', 1), ('C', 5)]
print(heuristic_cost(path))

def Greedy_best_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=heuristic_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

solution = Greedy_best_search(graph, 'S', 'G')
print('Solution is', solution)
print('Cost of Solution is', heuristic_cost(solution)[0])
