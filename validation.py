import networkx as nx
from itertools import combinations

edges = [
    ("a", "c"),
    ("a", "b"),
    ("c", "d"),
    ("b", "e"),
    ("d", "e"),
    ("e", "f"),
    ("f", "g"),
    ("f", "h"),
]
tree_edges = ["(bed,bdc)", "(bed,ef)", "(bdc,bac)", "(fe,hf)", "(fe,gf)"]
import networkx as nx


class TreeDecomposition:
    def __init__(self, graph_edges, tree_edges):
        g = nx.Graph()
        e = []
        for edge in graph_edges:
            edge = edge.replace(",", "").replace("'", "")
            edge = edge[1:3]
            e.append(tuple(edge))
        g.add_edges_from(e)
        self.graph = g
        # self.tree = self.construct_tree(tree_edges)
        tree = []
        neighbors = {}
        for i in tree_edges:
            i = i.replace("(", "").replace(")", "").split(",")
            i[0] = "".join(sorted(i[0]))
            i[1] = "".join(sorted(i[1]))
            if not neighbors.get(i[1]):
                neighbors[i[1]] = set()
            if not neighbors.get(i[0]):
                neighbors[i[0]] = set()
            neighbors[i[1]].add(i[0])
            neighbors[i[0]].add(i[1])
            for j in i:
                tree.append(set(j))
        self.tree = tree
        self.neighbors = neighbors

    def construct_tree(self, tree_edges):
        tree = []
        for node in self.graph.nodes():
            neighbors = [n for n in self.graph.neighbors(node)]
            bag = set()
            bag.add(node)
            for neighbor in neighbors:
                bag.add(neighbor)
                if (node, neighbor) in tree_edges:
                    self.graph.remove_edge(node, neighbor)
            tree.append(bag)
        print("tree", tree)
        return tree

    def is_valid(self):
        valid = True

        # Property 1: every vertex is in a bag
        for e in self.graph.nodes():
            contained = False
            for bag in self.tree:
                if e in bag:
                    contained = True
                    break
            if not contained:
                valid = False
                print("Vertex", e, "not contained in any bag!")

        # Property 2: every edge is in a bag
        for e in self.graph.edges():
            e, w = e
            if e >= w:
                continue
            contained = False
            for bag in self.tree:
                if e in bag and w in bag:
                    contained = True
                    break
            if not contained:
                valid = False
                print("Edge {", e, w, "} not contained in any bag!")

        for v in self.graph.nodes:
            connected = {}
            contained = set()
            for e in self.tree:
                e = "".join(sorted("".join(str(x) for x in e)))
                if v in e:
                    connected[e] = False
                    contained.add(e)
            contained = list(contained)
            if len(contained) == 1:
                continue
            for i in range(len(contained) - 1):
                for j in range(i + 1, len(contained)):
                    if (contained[j]) in self.neighbors[contained[i]]:
                        connected[contained[i]] = True
                        connected[contained[j]] = True
            for k in contained:
                if not connected[k]:
                    valid = False
                    print("Tree containing vertex", v, "is not connected!")
                    break

        # Property 3: subtrees connected
        # for v in self.graph.nodes():
        #     S = self.is_subtree(v)
        #     print(S, v)
        #     if len(S) != 1:
        #         valid = False
        #         print("Tree containing vertex", v, "is not connected!")

        # for bag in self.tree:
        #     combs = combinations(bag, 2)
        #     contained = False
        #     for c in combs:
        #         v, w = c
        #         for e in self.graph.edges():
        #             if v in e and w in e:
        #                 contained = True
        #                 break
        #     if not contained:
        #         valid = False
        #         print("Tree containing bag", bag, "has not connected edges!")

        # done
        return valid

        # def connected_components(self, v):
        #     visited = set()
        #     S = []
        #     stack = [v]
        #     # while stack:
        #     #     node = stack.pop()
        #     #     if node not in visited:
        #     #         visited.add(node)
        #     #         S.append(node)
        #     #         stack.extend(
        #             [n for n in self.graph.neighbors(node) if n not in visited]
        #         )
        for e in self.tree:
            if e in e:
                S.append(e)

        return S

    # def is_subtree(self, vertex):
    #     bags = set()
    #     for i, vertices in enumerate(self.tree):
    #         if vertex in vertices:
    #             bags.add(i)
    #     while bags:
    #         leaves = set()
    #         for bag in bags:
    #             if len(self.tree[bag]) == 1:
    #                 leaves.add(bag)
    #         bags -= leaves
    #         for bag in bags:
    #             for leaf in leaves:
    #                 if leaf in self.tree[bag]:
    #                     self.tree[bag].remove(leaf)
    #                     if len(self.tree[bag]) == 0:
    #                         return False
    #         bags -= set(bag for bag in bags if len(self.tree[bag]) == 0)
    #     return True

    # def validate_tree_decomp(graph, tree):
    """
    Validate whether the bags in a tree decomposition of a graph form a subtree.
    The tree should contain only edges like [{a,b}, {b,c}] etc.

    Parameters:
    - graph: a NetworkX graph object
    - tree: a list of edges representing the tree decomposition

    Returns:
    - True if the bags in the tree decomposition form a subtree of the graph, False otherwise
    """

    # Create a dictionary to store the bags for each node
    # bags = {}
    # for edge in tree:
    #     for node in edge:
    #         if node not in bags:
    #             bags[node] = set()
    #     edge = list(edge)
    #     # bags[edge[0]].add(edge[1])
    #     # bags[edge[1]].add(edge[0])
    #     for i in range(len(edge) - 1):
    #         for j in range(i + 1, len(edge)):
    #             bags[edge[i]].add(edge[j])
    #             bags[edge[j]].add(edge[i])

    # # Check if the bags form a subtree
    # visited = set()
    # stack = [next(iter(bags))]
    # while stack:
    #     node = stack.pop()
    #     visited.add(node)
    #     for neighbor in bags[node]:
    #         if neighbor not in visited:
    #             stack.append(neighbor)

    # return visited == set(graph.nodes())


# dec = TreeDecomposition(edges, tree_edges)
# print(dec.is_valid())
# print(validate_tree_decomp(dec.graph, dec.tree))
