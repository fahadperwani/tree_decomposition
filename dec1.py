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
        elif l == 1:
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
        elif l >= 2:
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
    result = ['(' + ','.join(t) + ')' for t in tree.edges]
    print(result)
    return (node, result)


def fetch_columns(data, column_indices):
    result = []
    for row in data:
        selected_columns = [row[i] for i in column_indices]
        result.append(selected_columns)
    return result

def find_common_elements(list1, list2):
    common_elements = []
    for sublist1 in list1:
        if sublist1 in list2:
            common_elements.append(sublist1)
    return common_elements

def suitable_node(graph):
    max_length = 0
    max_node = None

    for node in graph.nodes():
        length = len(remove_integers(node))  # Assuming the length of the string is the length of the node itself
        if length > max_length:
            max_length = length
            max_node = node

    return max_node

def inorder_traversal(graph, node, g: nx.Graph):
    visited = set()
    stack = [node]
    comb = {}

    while stack:
        current_node = stack[-1]
        neighbors = list(graph[current_node])

        if len(neighbors) == 0 or all(n in visited for n in neighbors):
            node = stack.pop()
            visited.add(node)
            print(node)  # or do whatever you want with the node
            neighbors = list(graph[node])
            if len(neighbors) == 0:
                comb[node] = [[1], [2], [3]]
            elif len(neighbors) == 1:
                isForget = True
                for i in remove_integers(node):
                    if i not in neighbors[0]:
                        isForget = False
                        break
                print(''.join(sorted(remove_integers(node))))
                print(''.join(sorted(remove_integers(neighbors[0]))))
                print(''.join(sorted(remove_integers(node))) in ''.join(sorted(remove_integers(neighbors[0]))))
                comb[node] = []
                temp = comb[neighbors[0]]
                if not isForget:
                    common = remove_integers(neighbors[0])
                    n = remove_integers(node)
                    for i in common:
                        n = n.replace(i, '')
                    adjacent = list(g.neighbors(n))
                    idxes = node.index(n)
                    ad_list = []
                    for i in remove_integers(node).replace(n, ''):
                        if i in adjacent:
                            ad_list.append(neighbors[0].index(i))
                    columns = fetch_columns(temp, ad_list)
                    for i in range(len(temp)):
                        for j in range(3):
                            if columns and j+1 in columns[i]:
                                continue
                            k = temp[i].copy()
                            k.insert(idxes, j+1)
                            comb[node].append(k)
                else:
                    idxes = []
                    for i in remove_integers(node):
                        idxes.append(neighbors[0].index(i))
                    arr = (fetch_columns(temp, idxes))
                    arr = [list(t) for t in set(tuple(sublist) for sublist in arr)]
                    comb[node] = arr
            elif len(neighbors) == 2:
                common = (find_common_elements(comb[neighbors[0]], comb[neighbors[1]]))
                comb[node] = common              
        else:
            for neighbor in neighbors[::-1]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    break
    return comb

def pre_order(graph, node, comb):
    stack = [node]
    visited = set()
    colors = dict()
    c = comb[node][0]
    while stack:
        n = stack.pop()
        exist = True
        for i in remove_integers(n):
            if i not in colors:
                exist = False
                break
        if remove_integers(n) in visited or exist:
            visited.add(remove_integers(n))
            neighbors = graph.neighbors(n)
            for i in neighbors:
                stack.append(i)
            continue
        if n!=node:
            val = []
            col = []
            for i in range(len(remove_integers(n))):
                if n[i] in colors:
                    col.append(i)
                    val.append(colors[n[i]])
            columns = fetch_columns(comb[n], col)
            for i in range(len(columns)):
                contain = True
                for k, j in enumerate(col):
                    if columns[i][k] != val[k]:
                        contain = False
                        break
                if contain:
                    c = comb[n][i]
                    break
        for i in range(len(remove_integers(n))):
            if n[i] not in colors:
                colors[n[i]] = c[i]
        neighbors = graph.neighbors(n)
        for i in neighbors:
            stack.append(i)
    return colors

def coloring(o_edges, n_edges, node):
    g = nx.Graph()
    for e in o_edges:
        e = e.replace('(', '').replace(')', '')
        r = e.split(',')
        g.add_edge(r[0], r[1])

    n = nx.Graph()
    for e in n_edges:
        e = e.replace('(', '').replace(')', '').split(',')
        n.add_edge(e[0], e[1])

    # node = suitable_node(n)
    g1 = nx.dfs_tree(n, node)
    comb = inorder_traversal(g1, node, g)
    for key, value in comb.items():
        print(key, ':', value)
    if comb[list(g1.nodes())[0]]:
        return (pre_order(g1, node,comb))
    else:
        return None
