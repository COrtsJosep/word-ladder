import tqdm
import networkx as nx
from pathlib import Path

graph_filename = Path('G.graphml')
G = nx.read_graphml(graph_filename)
            
ccs = list(nx.connected_components(G))
ccs.sort(key = len, reverse = True)

longest_path = []
len_longest_path = 0
for cci, cc in enumerate(ccs):
    if len(cc) > len_longest_path:
        for starting_node in tqdm.tqdm(cc, desc = f'{cci + 1} / {len(ccs)}'):
            current_path = [starting_node]
            visited_nodes = [set()]
            while current_path:          
                neighbors = set(G.neighbors(current_path[-1])) - set(current_path) - visited_nodes[-1]               
                if neighbors:
                    next_node = neighbors.pop()
                    
                    visited_nodes[-1].add(next_node)
                    visited_nodes.append(set())
                    
                    current_path.append(next_node)
                    
                    if len(current_path) > len_longest_path:
                        longest_path = current_path.copy()
                        len_longest_path = len(longest_path)
                        
                else:
                    _ = current_path.pop()
                    _ = visited_nodes.pop()
                    
with open('longest_ladder.txt', 'w') as f:
    f.write(
        '\n'.join(longest_path)
    )
