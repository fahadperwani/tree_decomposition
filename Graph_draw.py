from graphviz import Graph, Digraph


def Draw_Graph(edges, type, color=None, node=None):
    # Directed graph
    G = Graph("graph")
    G.attr("node", shape="circle")
    if node:
        G.attr(root=node)
    colors = ['red', 'green', 'blue']
    if color:
        for key, value in color.items():
            G.node(key, fillcolor=colors[value-1], style='filled')
    for i in edges:
        i = i.replace(" ", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        z = i.split(",")
        s = z[0]
        t = z[1]
        if not t:
            G.node(s)
        else:
            G.edge(s, t)
    # save the graph to file, or you can leave it out.
    if type == 'graph':
        G.render(filename="graph.gy", format="png")
    elif type == 'decomposition':
        G.render(filename="decomposition.gy", format="png")
    elif type == 'nice':
        G.render(filename="nice.gy", format="png")
    # G.view() graph will in adobe displyed
