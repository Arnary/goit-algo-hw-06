from collections import deque

from subway_graph import Subway


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return

    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)

    bfs_recursive(graph, queue, visited)


if __name__ == "__main__":
    dfs_recursive(Subway, "1")
    print("\n")
    bfs_recursive(Subway, deque(["1"]))
