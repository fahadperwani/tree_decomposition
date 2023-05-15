from graphviz import Graph


def Draw_Graph(edges):
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
    G.render(filename="graph.gy", format="png")
    # G.view() graph will in adobe displyed
