import networkx as nx
import matplotlib.pyplot as plt
from uniform_cost_search import UcsTraverser

G = nx.Graph()
nodes = ["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC",
         "J1","Mada","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
print(G.nodes)

G.add_edge("SportsComplex","Siwaka",weight="450")

G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")

G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")

G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("Ph.1B","STC",weight="50")

G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase2","STC",weight="50")

G.add_edge("J1","Mada",weight="200")

G.add_edge("Phase3","ParkingLot",weight="350")

G.add_edge("STC","Phase2",weight="50")
G.add_edge("STC","ParkingLot",weight="250")

G.add_edge("Mada","ParkingLot",weight="700")

G.nodes["SportsComplex"]['pos'] = (-6,2)
G.nodes["Siwaka"]['pos'] = (-4,2)
G.nodes["Ph.1A"]['pos'] = (-2,2)
G.nodes["Ph.1B"]['pos'] = (-2,0)
G.nodes["Phase2"]['pos'] = (0,0)
G.nodes["STC"]['pos'] = (-2,-2)
G.nodes["J1"]['pos'] = (2,0)
G.nodes["Mada"]['pos'] = (4,0)
G.nodes["Phase3"]['pos'] = (2,-2)
G.nodes["ParkingLot"]['pos'] = (2,-4)

node_pos = nx.get_node_attributes(G,'pos')

route_ucs = UcsTraverser()
visited_set = route_ucs.UCS(G, "SportsComplex", "ParkingLot")
print(visited_set)
visited_list = list(visited_set)


node_col = ['pink' if not node in visited_list else 'purple' for node in G.nodes()]
green_colored_edges = list(zip(visited_list, visited_list[1:]))

edge_col = ["pink" if not edge in green_colored_edges else 'purple' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G,node_pos,node_color=node_col,node_size=3500)
nx.draw_networkx_edges(G,node_pos,edge_color=edge_col,width=2)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)

plt.axis('off')
plt.show()
