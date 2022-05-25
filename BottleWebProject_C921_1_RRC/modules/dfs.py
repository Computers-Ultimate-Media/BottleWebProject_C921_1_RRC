def dfs(graphic, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graphic[start] - visited:
        dfs(graphic, next, visited)
    return visited


graph = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}

dfs(graph, '2')
