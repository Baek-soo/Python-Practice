#list의 형태를 사용한 것과 논리는 거의 동일하지만 성능면에서는 deque가 list보다 더 좋다.

def dfs(graph, start_node):
    #deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()

    #시작 노드 설정해주기
    need_visited.append(start_node)

    #방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        #시작 노드를 지정하고
        node = need_visited.popleft()
        #만약 방문한 리스트에 없다면
        if node not in visited:
            #방문 리스트에 노드를 추가
            visited.append(node)
            #인접한 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
    return visited

#dfs다음에 while문 다음은 리스으틔 가장 끝에 있는 데이터를 기준으로 추출한다.
