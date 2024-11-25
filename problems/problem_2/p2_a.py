from collections import defaultdict, deque

def find_paths(n, paths):
    graph = defaultdict(lambda: defaultdict(int))
    for a, b in paths:
        graph[a][b] += 1
        graph[b][a] += 1

    def bfs_find_path(source, target, route_map):
        visited = {source}
        queue = deque([source])
        
        while queue:
            current_node = queue.popleft()
            for adjacent_node in graph[current_node]:
                if adjacent_node not in visited and graph[current_node][adjacent_node] > 0:
                    route_map[adjacent_node] = current_node
                    if adjacent_node == target:
                        return True
                    visited.add(adjacent_node)
                    queue.append(adjacent_node)
        return False

    def calculate_max_flow(source, target):
        total_flow = 0

        while True:
            route_map = {}
            if not bfs_find_path(source, target, route_map):
                break
            
            path_flow = float('Inf')
            node = target
            while node != source:
                prev_node = route_map[node]
                path_flow = min(path_flow, graph[prev_node][node])
                node = prev_node

            node = target
            while node != source:
                prev_node = route_map[node]
                graph[prev_node][node] -= path_flow
                graph[node][prev_node] += path_flow
                node = prev_node

            total_flow += path_flow

        return total_flow

    return calculate_max_flow(1, n)
