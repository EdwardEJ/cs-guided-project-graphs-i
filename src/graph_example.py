'''
Object representation of a graph
'''
class GraphNode():
    def __init__(self, value=None):
        self.value = value
        self.connections = []

g1 = GraphNode()
g2 = GraphNode()
g3 = GraphNode()
g4 = GraphNode()

g1.connections.append(g2)
g1.connections.append(g3)
g1.connections.append(g4)

# The adjacency list is the most common graph representation
# Used to represent a directed graph
directed_graph = [
    [1, 2], #Node 0
    [3],  #Node 1
    [3],  #Node 2
    [4],  #Node 3
    [],     #Node 4
]

# Write a function to print out each graph node and all its connections
def print_graph(graph):
    '''
    Input: graph represented as an adjacency list
    Output: prints out each graph node with its connections
    '''
    # Iterate with a for loop
    # Since we want access to both the index as well as the value at that # index in the adjacency list, use `enumerate`

    for node, connections in enumerate(graph):
        print(f'Graph node {node} is conencted to {connections}')

print(print_graph(directed_graph))
