import networkx as nx
import matplotlib.pyplot as plt


Subway = nx.Graph()
Subway.add_edges_from([("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("5", "6")])
Subway.add_edges_from([("8", "9"), ("9", "10"), ("10", "11"), ("11", "12"), ("12", "13"), ("13", "14"), ("14", "15")])
Subway.add_edges_from([("16", "17"), ("17", "3"), ("3", "18"), ("18", "19"), ("19", "20"), ("20", "13"), ("13", "21"), ("21", "22")])
Subway.add_edges_from([("23", "24"), ("24", "3"), ("3", "25"), ("25", "26"), ("26", "9"), ("9", "27")])

color_map = []
for node in Subway:
    if node in ["1", "2", "3", "4", "5", "6"]:
        color_map.append('green')
    elif node in ["8", "9", "10", "11", "12", "13", "14", "15"]:
        color_map.append('red')
    elif node in ["16", "17", "18", "19", "20", "21", "22"]:
        color_map.append('yellow')
    elif node in ["23", "24", "25", "26", "27"]:
        color_map.append('purple')        
    else: 
        color_map.append('blue')      

pos = nx.spring_layout(Subway, seed=81)

num_nodes = Subway.number_of_nodes()
num_edges = Subway.number_of_edges()


if __name__ == "__main__":
    plt.figure(3,figsize=(10,10)) 
    nx.draw(Subway, pos, node_color=color_map, node_size=400, with_labels=True)
    labels = nx.get_edge_attributes(Subway, 'weight')
    nx.draw_networkx_edge_labels(Subway, pos, edge_labels=labels)
    plt.show()
    print(f"Кількість вершин графа: {num_nodes}")
    print(f"Кількість ребер графа: {num_edges}")