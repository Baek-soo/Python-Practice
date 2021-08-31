#한우물판 파서 탐색 <-> DFS
#핵심 : "방문하고자 하는 노드", "방문 했던 노드"를 나누어서 알고리즘을 구성
# 1단계 : 시작 노드를 방문했던 노드에 삽입
# 2단계 : 방문할 노드에 시작 노드의 child node를 삽입한다.
# 3단계 : child node를 중심으로 1~2단계를 거쳐 탐색

def bfs(graph, start_node):
    need_visited , visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

#while문 다음에는 리스트의 가장 처음에 있는 인자를 받는다