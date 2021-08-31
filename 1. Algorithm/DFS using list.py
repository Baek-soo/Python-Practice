# need_visited에서 추가된 node들 중에서 가장 끝에 있는 것을 뽑아서 검색하는 방식
# -> 스택방식
def dfs(graph, start_node):

    #기본은 항상 두개의 리스트를 별도로 관리해주는것
    need_visited, visited = list(), list()

    #시작 노드를 시정하기
    need_visited.append(start_node)

    #만약 아직도 방문이 필요한 노드가 있다면, 
    while need_visited:
        #그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        #만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            #방문한 목록에 추가하기
            visited.append(node)
            #그 노드에 연결된 노드를
            need_visited.extend(graph[node])

    return visited

#dfs다음에 while문 다음은 리스으틔 가장 끝에 있는 데이터를 기준으로 추출한다.