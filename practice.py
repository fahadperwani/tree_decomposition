import networkx as nx
from itertools import combinations

o = ['(a,b)', '(b,c)', '(c,d)', '(d,e)', '(e,f)', '(b,f)', '(f,g)', '(f,a)']
edges = ['(feb,feb1)', '(feb,feb2)', '(ebd,bd1)', '(fab,ab1)', '(fg,g1)', '(dcb,cb1)', '(feb1,feb3)', '(feb1,feb4)', '(feb2,eb1)', '(feb3,fb1)', '(feb4,fb2)', '(fb1,f1)', '(f1,fg)', '(fb2,fab)', '(ab1,b1)', '(eb1,ebd)', '(bd1,dcb)', '(cb1,b2)']

def remove_integers(string):
    return ''.join(char for char in string if not char.isdigit())


def find_key(dictionary, target_key):
    sorted_target_key = ''.join(sorted(target_key))
    for key in dictionary:
        sorted_key = ''.join(sorted(key))
        if sorted_key == sorted_target_key:
            return dictionary[key]
    return None

def subsets(s):
    subsets = []
    for r in range(len(s) + 1):
        subsets.extend(combinations(s, r))
    return subsets

def inorder(g, node):
    visited = set()
    stack = [node]
    index = 0
    indices = dict()

    while stack:
        current = stack.pop()
        visited.add(current)
        indices[current] = index
        index+=1
        neighbors = list(g.neighbors(current))
        for i in range(len(neighbors), 0, -1):
            stack.append(neighbors[i-1])
    return (indices)

def postorder(graph, node, g: nx.Graph):
    visited = set()
    stack = [node]
    c = dict()

    while stack:
        current_node = stack[-1]
        neighbors = list(graph[current_node])

        if len(neighbors) == 0 or all(n in visited for n in neighbors):
            node = stack.pop()
            visited.add(node)
            print(node)  # or do whatever you want with the node
            neighbors = list(graph[current_node])
            if len(neighbors) == 0:
                id = 'c'+str(indices[node])
                # c[node] = {id: {'': 0 , node[1]: 1}}
                c[node] = {'': 0 , node[0]: 1}
            elif len(neighbors) == 1:
                isForget = True
                for i in remove_integers(node):
                    if i not in neighbors[0]:
                        isForget = False
                        break
                if not isForget:
                    i = set(remove_integers(node))
                    j = set(remove_integers(neighbors[0]))
                    v = ''.join(i.intersection(j))
                    u = remove_integers(node)
                    for k in v:
                        if k in u:
                            u = u.replace(k, '')
                    s = subsets(j)
                    for st in s:
                        if len(st) == 0:
                            val = c[neighbors[0]]['']
                            c[node] = {'': val, u: val+1}
                        else:
                            inf = False
                            for k in st:
                                if k in list(g.neighbors(u)):
                                    inf = True
                                    break
                            st = ''.join(st)
                            # val = c[neighbors[0]][st]
                            val = find_key(c[neighbors[0]], st)
                            c[node][st] = val
                            if inf:
                                c[node][u+st] = float('-inf')
                            else:
                                c[node][u+st] = val+1
                else:
                    i = set(remove_integers(node))
                    j = set(remove_integers(neighbors[0]))
                    v = ''.join(i.symmetric_difference(j))
                    u = remove_integers(node).replace(v, '')
                    s = subsets(i)
                    neighbor = c[neighbors[0]]
                    
                    for st in s:
                        if len(st) == 0:
                            val = find_key(neighbor, v)
                            c[node] = {'': max(neighbor[''], neighbor[v])}
                        else:
                            st = ''.join(st)
                            v1 = find_key(neighbor, st)
                            v2 = find_key(neighbor, st+v)
                            c[node][st] = max(v1, v2)
            else:
                i = set(remove_integers(node))
                s = subsets(i)
                c[node] = dict()
                for st in s:
                    st = ''.join(st)
                    c[node][st] = find_key(c[neighbors[0]], st) + find_key(c[neighbors[1]], st) - len(st)
                    print(find_key(c[neighbors[0]], st) + find_key(c[neighbors[1]], st) - len(st))
        else:
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    break
    return c

n = nx.DiGraph()
for e in edges:
    e = e.replace('(', '').replace(')', '')
    e = e.split(',')
    n.add_edge(e[0].strip(), e[1].strip())

g = nx.Graph()
for e in o:
    e = e.replace('(', '').replace(')', '')
    e = e.split(',')
    g.add_edge(e[0], e[1])

def max_in_dict(c):
    max = float('-inf')
    nodes = ''
    for key,value in c.items():
        if value > max:
            max = value
    for key,value in c.items():
        if value == max and key != '':
            nodes+=key
    return (max, nodes)

def max_ind(graph, node, c, g):
    visited = set()
    stack = [node]
    max = float('-inf')
    max_set = set()

    while stack:
        node = stack.pop()
        visited.add(node)
        neighbors = list(graph.neighbors(node))

        val, nodes = max_in_dict(c[node])
        if nodes:
            if val > max:
                max = val
            for i in nodes:
                valid = True
                for j in max_set:
                    if i in list(g.neighbors(j)):
                        valid = False
                        break
                if i not in max_set and valid:
                    max_set.add(i)

        
        stack+=neighbors[::-1]
    return max_set

node = list(n.nodes())[0]
indices = inorder(n, node)
c = postorder(n, node, g)
for k, v in c.items():
    print('\n')
    print(k,":", v)
print("Max: ",max_ind(n, node, c, g))