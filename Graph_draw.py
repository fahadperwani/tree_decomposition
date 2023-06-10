from graphviz import Graph


def Draw_Graph(edges, type):
    # Directed graph
    G = Graph("graph")
    G.attr("node", shape="circle")
    for i in edges:
        i = i.replace(" ", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        z = i.split(",")
        s = z[0]
        t = z[1]
        G.edge(s, t)
    # save the graph to file, or you can leave it out.
    if type == 'graph':
        G.render(filename="graph.gy", format="png")
    elif type == 'decomposition':
        G.render(filename="decomposition.gy", format="png")
    elif type == 'nice':
        G.render(filename="nice.gy", format="png")
    # G.view() graph will in adobe displyed
