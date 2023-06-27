import networkx as nx
import matplotlib.pyplot as plt
import string
import time
import dec1 as d

def create_random_graph(nodes):
    p = 1.0 / num_nodes

# Generate a random graph with the given nodes and edge probability
    G = nx.gnp_random_graph(len(nodes), p)

    # Relabel the nodes with the given labels
    mapping = {i: nodes[i] for i in range(len(nodes))}
    G = nx.relabel_nodes(G, mapping)
    return G

def measure_total_time(nodes):
    g = create_random_graph(nodes)
    print(g)
    result = ['(' + ','.join(t) + ')' for t in g.edges]
    start_time = time.time()
    width, edges, dec = d.decomposition(result)
    node, nice = d.nice_tree(edges)
    d.coloring(result, nice, node, 5)
    d.max_independent_set(nice, result)
    end_time = time.time()
    return end_time - start_time

# Parameters for iteration
start = 10
stop = 150
step = 8

nodes_list = []
time_taken_list = []

alphabet_set = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ڈ', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک',
    'گ', 'ل', 'م', 'ن', 'و', 'ہ', 'ھ', 'ی',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'آ', 'ؤ', 'ئ', 'ء', 'ة', 'ي', 'ى', 'ً', 'ٌ', 'ٍ', 'َ', 'ُ', 'ِ', 'ّ', 'ْ', 'ٰ', 'ٓ', 'ٔ', 'ٕ',
    'あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'
}
characters = list(alphabet_set)

print(len(characters))
# Iterate through the numbers and record time taken
for num_nodes in range(start, stop + 1, step):
    nodes = characters[:num_nodes]
    time_taken = measure_total_time(nodes)
    nodes_list.append(num_nodes)
    time_taken_list.append(time_taken)

# Display the graph of time taken
plt.plot(nodes_list, time_taken_list, 'bo-')
plt.xlabel('Number of Nodes')
plt.ylabel('Time Taken (seconds)')
plt.title('Graph Creation Time')
plt.grid(True)
plt.show()
