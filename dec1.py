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
    print(arr)
    converted_list = [
        ",".join("".join(subitem) for subitem in sublist) for sublist in arr
    ]
    converted_list = [f"({item})" for item in converted_list]
    print(converted_list)
    return (bags[0], converted_list, bags[1].edges())

def remove_integers(string):
    return ''.join(char for char in string if not char.isdigit())

def nice_tree(edges):
    G = nx.Graph()
    e = []
    for edge in edges:
        edge = edge.replace(")", "").replace("'", "").replace('(', '')
        print("edge", tuple(edge.split(',')))
        edge = edge.split(',')
        e.append(tuple(edge))
    G.add_edges_from(e)
    tree: nx.DiGraph = nx.bfs_tree(G, list(G.nodes())[0])
    node = list(tree.nodes())[0]
    copies = {n: 1 for n in tree.nodes()}

    stack = [node]
    visited = set()
    # tree.remove_edge(("c", "f"), ("m", "f"))
    while stack:
        print(tree.edges())
        print()
        n = stack.pop()
        visited.add(n)

        neighbors = [u for u in tree.neighbors(n) if u not in visited]
        l = len(neighbors)
        if l == 0:
            for v in remove_integers(n):
                bag = remove_integers(n).replace(v, '')
                if len(bag)>0:
                    if bag not in copies:
                        copies[bag] = 0
                    copies[bag] = copies[bag] + 1
                    bag+=str(copies[bag])
                    tree.add_edge(n, bag)
                    stack.append(bag)
                    break
        # if l == 1:
        #     if remove_integers(n) == remove_integers(neighbors[0]):
        #         continue
        #     common = set(n).intersection(neighbors[0]).pop()
        #     u = remove_integers(n).replace(common, '')
        #     # u.replace(common, '')
        #     if len(u) > 0:
        #         bag = remove_integers(n).replace(u[0], '')
        #         # for i in u:
        #         #     temp = bag.copy()
        #         #     if temp.remove(i) not in visited:
        #         #         bag.remove(i)
        #         #         break
        #         # bag.replace(u[0], '')
        #         if bag not in copies:
        #             copies[bag] = 0
        #         copies[bag] = copies[bag] + 1
        #         bag+=str(copies[bag])
        #         tree.remove_edge(n, neighbors[0])
        #         tree.add_edge(bag, n)
        #         tree.add_edge(bag, neighbors[0])
        #         stack.append(bag)
        #     else:
        #         stack.append(neighbors[0])
        if l == 1:
            if remove_integers(n) == remove_integers(neighbors[0]):
                continue
            bag = None
            delta = remove_integers(n)
            for v in neighbors[0]:
                if v in n:
                    delta = delta.replace(v, '')
            if len(delta) > 0:
                bag = remove_integers(n).replace(delta[0], '')
            else:
                delta = remove_integers(neighbors[0])
                for v in n:
                    if v in neighbors[0]:
                        delta = delta.replace(v, '')
                bag = remove_integers(n)+delta[0]
            if ''.join(sorted(remove_integers(bag))) == ''.join(sorted(remove_integers(neighbors[0]))): 
                stack.append(neighbors[0])
                continue
            if bag not in copies:
                copies[bag] = 0
            copies[bag] = copies[bag] + 1
            bag+=str(copies[bag])
            tree.remove_edge(n, neighbors[0])
            tree.add_edge(bag, n)
            tree.add_edge(bag, neighbors[0])
            stack.append(bag)
        if l >= 2:
            left = remove_integers(n) + str(copies[remove_integers(n)])

            copies[remove_integers(n)] = copies[remove_integers(n)] + 1

            right = remove_integers(n) + str(copies[remove_integers(n)])

            copies[remove_integers(n)] = copies[remove_integers(n)] + 1
            for u in neighbors:
                tree.remove_edge(n, u)
            tree.add_edge(n, left)
            tree.add_edge(n, right)
            for i, u in enumerate(neighbors):
                if i == 0:
                    tree.add_edge(right, u)
                else:
                    tree.add_edge(left, u)
            stack.append(right)
            stack.append(left)
        # stack += neighbors
    arr = [list(x) for x in tree.edges()]
    result = [
        f"({''.join(map(str, t[0]))}),({''.join(map(str, t[1][:3]))}{t[1][3] if len(t[1]) > 3 else ''})"
        for t in tree.edges()
    ]
    return result
