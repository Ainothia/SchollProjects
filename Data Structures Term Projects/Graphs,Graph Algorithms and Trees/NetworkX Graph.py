import networkx as nx
import matplotlib.pyplot as plt
graph = nx.DiGraph()
nodes = [0,1,2,3,4]
graph.add_nodes_from(nodes)
weigted_edges = [(0,1,5),(0,4,2),(0,2,3),(1,3,6),(2,1,1),(2,3,2),(4,1,6),(4,3,4),(4,2,10),(1,2,2)]
graph.add_weighted_edges_from(weigted_edges)
arc_weight=nx.get_edge_attributes(graph,'weight')
graph.nodes[0]['pos'] = (0,0)
graph.nodes[1]['pos'] = (2,2)
graph.nodes[2]['pos'] = (2,-2)
graph.nodes[3]['pos'] = (5,2)
graph.nodes[4]['pos'] = (5,-2)
node_pos=nx.get_node_attributes(graph,'pos')
pos=nx.spring_layout(graph)
nx.draw_networkx_edge_labels(graph, node_pos, edge_labels=arc_weight)
nx.draw(graph, node_pos, node_size=300, with_labels=True)

print("Before Removing Node 3")
for x in range(0,5):
    try:
        sp = nx.dijkstra_path_length(graph,source = 4,target=x)
        print( "{} to {} shortest length: {}".format(4,x,sp))
    except nx.exception.NetworkXNoPath:
        print("{} to {} shortest length: 0".format(4,x))
plt.show()
print("\n")

graph.remove_node(3)
arc_weight=nx.get_edge_attributes(graph,'weight')
pos=nx.spring_layout(graph)
nx.draw_networkx_edge_labels(graph, node_pos, edge_labels=arc_weight)
nx.draw(graph, node_pos, node_size=300, with_labels=True)

print("After Removing Node 3")
for x in range(0,5):
    try:
        if(x ==3):
            continue
        sp = nx.dijkstra_path_length(graph,source = 4,target=x)
        print( "{} to {} shortest length: {}".format(4,x,sp))
    except nx.exception.NetworkXNoPath:
        print("{} to {} shortest length: 0".format(4,x))
plt.show()