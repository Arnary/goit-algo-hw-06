from subway_graph import Subway


Subway["1"]["2"]["weight"] = 1
Subway["2"]["3"]["weight"] = 1
Subway["3"]["4"]["weight"] = 4
Subway["4"]["5"]["weight"] = 1
Subway["5"]["6"]["weight"] = 2
Subway["8"]["9"]["weight"] = 1
Subway["9"]["10"]["weight"] = 2
Subway["10"]["11"]["weight"] = 4
Subway["11"]["12"]["weight"] = 3
Subway["12"]["13"]["weight"] = 5
Subway["13"]["14"]["weight"] = 2
Subway["14"]["15"]["weight"] = 4
Subway["16"]["17"]["weight"] = 3
Subway["17"]["3"]["weight"] = 1
Subway["3"]["18"]["weight"] = 3
Subway["18"]["19"]["weight"] = 2
Subway["19"]["20"]["weight"] = 5
Subway["20"]["13"]["weight"] = 3
Subway["13"]["21"]["weight"] = 2
Subway["21"]["22"]["weight"] = 3
Subway["27"]["9"]["weight"] = 2
Subway["9"]["26"]["weight"] = 3
Subway["26"]["25"]["weight"] = 2
Subway["25"]["3"]["weight"] = 1
Subway["3"]["24"]["weight"] = 2
Subway["24"]["23"]["weight"] = 1


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_node = min((v for v in set(distances.keys()) - visited), key=lambda x: distances[x])
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


start = "11"
shortest_distances = dijkstra(Subway, start)

print(f"Найкоротші відстані від вершини {start}: {shortest_distances}")
