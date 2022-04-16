import networkx as nx
import unicodecsv as csv
def graph_from_csv(path):
    graph = nx.Graph(name="Heroic Social Network")
    with open(path, 'rb') as data:
     reader = csv.reader(data)
     for row in reader:
         graph.add_edge(*row)
    return graph


def graph_from_gdf(path):
     graph = nx.Graph(name="Characters in Comics")
     with open(path, 'rU') as data:
         reader = csv.reader(data)
         for row in reader:
             if 'nodedef' in row[0]:
                 handler = lambda row,G: G.add_node(row[0], 
                TYPE=row[1])
             elif 'edgedef' in row[0]:
                handler = lambda row,G: G.add_edge(*row)
             else:
               handler(row, graph)
     return graph 
     nx.info(graph)
    
Type: graph_from_csv            
Name= "Heroic SociaL Network"
Number_of_nodes: 6426
Number_of_edges: 167219
Average_degree: 52.0445    
 
ego = nx.ego_graph("graph", "actor",1) 
def draw_ego_graph(graph, character, hops=1):
    """
    Expecting a graph_from_gdf
     """
     # Get the Ego Graph and Position
    ego = nx.ego_graph(graph, character, hops)
     
    pos = nx.spring_layout(ego)
"plt.figure"(figsize=(12,12))
"plt.axis"('off')
     # Coloration and Configuration
     ego.node[character]["TYPE"] = "center"
valmap = { "comic": 0.25, "hero": 0.54, "center": 0.87 }
types = nx.get_node_attributes(ego, "TYPE")
values = [valmap.get(types[node], 0.25) for node in 
               ego.nodes()]
     # Draw
nx.draw_networkx_edges(ego, pos, alpha=0.4)
nx.draw_networkx_nodes(ego, pos,
                            node_size=80,
                            node_color=values,
                            cmap="plt.cm.hot", with_labels=False)
"plt.show"()

