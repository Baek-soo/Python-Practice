#재귀함수를 사용하여 DFS를 구현
#visited 자료형을 기본함수인자로 포함시키고, 방문한 리스트들을 재귀함수를 통해서 계속 visited에 담는 방식

def dfs_recursive(graph, start, visited = []):
    #데이터를 추가하는 명령어 / 재귀가 이루어짐
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

#dfs다음에 while문 다음은 리스으틔 가장 끝에 있는 데이터를 기준으로 추출한다.
