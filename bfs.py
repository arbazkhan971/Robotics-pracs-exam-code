graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


visited = set()
def bfs(visited,graph, start):
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(visited)
            print(queue)
            queue.extend(set(graph[vertex]) - visited)
    return visited
print(bfs(visited,graph, 'A'))