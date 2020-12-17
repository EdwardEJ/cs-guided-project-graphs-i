def csFindAllPathsFromAToB(graph):
    result = []
    dft(graph, 0, [0], result)
    return result
    
def dft(graph, current_node, current_path, result):
    if current_node == len(graph) - 1:
        result.append(current_path[:])
        
    connections = graph[current_node]
    
    for connection in connections:
        current_path.append(connection)
        dft(graph, connection, current_path, result)
        current_path.pop()
