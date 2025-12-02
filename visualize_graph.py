from graph_tool.all import *

g = load_graph('G.graphml')
pos = sfdp_layout(g)

graph_draw(
    g,
    pos = pos,
    output = 'network.png',
    bg_color = 'white',
)
