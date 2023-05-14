import networkx as nx

# from networkx.algorithms.approximation import treewidth_min_degree
from algorithm import treewidth_min_degree


def decomposition(edges):
    G = nx.Graph()
    e = []
    for edge in edges:
        edge = edge.replace(",", "").replace("'", "")
        print("edge", tuple(edge))
        edge = edge[1:3]
        e.append(tuple(edge))
    print("e", e)
    G.add_edges_from(e)
    # Get the tree decompositiong
    bags = treewidth_min_degree(G)
    arr = []
    idxes = {}
    for i, bag in enumerate(bags[1].edges()):
        edges = [tuple(x) for x in bag]
        for edge in edges:
            if idxes.get(edge):
                idxes[edge].append(edges)
            else:
                idxes[edge] = [edges]

        arr.append(edges)
    print(arr)
    for edges in arr:
        if "".join(sorted(edges[0])) in "".join(sorted(edges[1])):
            arr.remove(edges)
            for e in arr:
                if edges[0] in e:
                    t = list(e)
                    t[t.index(edges[0])] = edges[1]
                    arr[arr.index(e)] = tuple(t)
        if "".join(sorted(edges[1])) in "".join(sorted(edges[0])):
            arr.remove(edges)
            for e in arr:
                if edges[1] in e:
                    t = list(e)
                    t[t.index(edges[1])] = edges[0]
                    arr[arr.index(e)] = tuple(t)
    converted_list = [
        ",".join("".join(subitem) for subitem in sublist) for sublist in arr
    ]
    converted_list = [f"({item})" for item in converted_list]
    print(converted_list)
    return (bags[0], converted_list)
