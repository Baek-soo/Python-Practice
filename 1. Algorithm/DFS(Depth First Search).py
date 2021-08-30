#여러우물 동시에 파면서 탐색 <-> BFS
def DFS(graph, root):
    visited = []
    stack = [root]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited