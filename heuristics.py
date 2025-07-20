# heuristics.py
from math import hypot

def euclidean(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

# search_algorithms.py
import heapq
from heuristics import euclidean

def a_star(start, goal, env):
    open_set = []
    heapq.heappush(open_set, (0 + euclidean(start, goal), 0, start, [start]))
    visited = {start: 0}
    nodes_expanded = 0

    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        nodes_expanded += 1
        if node == goal:
            return path, g, nodes_expanded
        for (nbr, cost) in env.get_neighbors(node):
            ng = g + cost
            if nbr not in visited or ng < visited[nbr]:
                visited[nbr] = ng
                heapq.heappush(open_set, (ng + euclidean(nbr, goal), ng, nbr, path + [nbr]))
    return None, float('inf'), nodes_expanded

# Recursive Best-First Search (RBFS)
def rbfs(start, goal, env):
    nodes_expanded = 0
    def recursive(node, goal, f_limit, g, path):
        nonlocal nodes_expanded
        nodes_expanded += 1
        h = euclidean(node, goal)
        f = max(g + h, f_limit)
        if node == goal:
            return path, g, f, nodes_expanded
        successors = []
        for (nbr, cost) in env.get_neighbors(node):
            successors.append((nbr, cost))
        if not successors:
            return None, float('inf'), float('inf'), nodes_expanded
        res_list = []
        for nbr, cost in successors:
            g2 = g + cost
            h2 = euclidean(nbr, goal)
            res_list.append([nbr, cost, g2 + h2])
        while res_list:
            res_list.sort(key=lambda x: x[2])
            best = res_list[0]
            if best[2] > f_limit:
                return None, float('inf'), best[2], nodes_expanded
            alt = res_list[1][2] if len(res_list) > 1 else float('inf')
            result, cost, new_f, _ = recursive(best[0], goal, min(f_limit, alt), g + best[1], path + [best[0]])
            best[2] = new_f
            if result is not None:
                return result, cost, new_f, nodes_expanded
        return None, float('inf'), float('inf'), nodes_expanded
    path, cost, f, nodes_expanded = recursive(start, goal, float('inf'), 0, [start])
    return path, cost, nodes_expanded
