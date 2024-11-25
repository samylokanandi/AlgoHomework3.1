# Problem 1b

def maximal_bipartite_match(g):
    num_u = len(g)
    num_v = len(g[0]) if g else 0
    match_v = [-1] * num_v

    def dfs(u, visited, match_v):
        for v in range(num_v):
            if g[u][v] and not visited[v]:
                visited[v] = True
                if match_v[v] == -1 or dfs(match_v[v], visited, match_v):
                    match_v[v] = u
                    return True
        return False

    max_matching = 0
    for u in range(num_u):
        visited = [False] * num_v
        if dfs(u, visited, match_v):
            max_matching += 1

    return max_matching
