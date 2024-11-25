from collections import deque

def is_bipartite(g_l):
    n = len(g_l)
    colors = [None] * n

    for start in range(n):
        if colors[start] is None:
            colors[start] = 0
            
            for neighbor in g_l[start]:
                if colors[neighbor] is not None:
                    colors[start] = 1 - colors[neighbor]
                    break
            
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in g_l[node]:
                    if colors[neighbor] is None:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
    return True
