#DFS와BFS
#from collections import deque

N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=0 #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(V)
print()
bfs(V)

# def dfs(graph, v, visited):
# #현재 노드를 방문 처리
# visited[v] = True
# print(v, end=' ')
# #현재 노드와 연결된 다른 노드를 재귀적으로 방문
# for i in graph[v]:
#   if not visited[i]:
#     dfs(graph, i, visited)

# #각 노드가 연결된 정보를 표현 (2차원 리스트)
# gragh = [[], [2,3,8],[1,7] ....]
# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# # 방문 처리를 위해 1차원 리스트 사용 index 0 은 사용하지 않게 맵핑하기 쉽게하기 위함
# visited = [False]*9
# #정의된 dfs 함수 호출
# dfs(graph, 1, visited)

# # def bfs(graph, start, visited):
# #  #큐 구현을 위해 deque 라이브러리 사용
# # queue = deque([start])

# # #현재 노드를 방문 처리
# # visited[start] = True
# # #큐가 빌 때 까지 반복
# # while queue:
# # #큐에서 하나의 원소를 뽑아 출력
# # v = queue.popleft()
# # print(v, end=' ')
# # #아직 방문하지 않은 인접한 원소들을 큐에 삽입
# # for i in graph[v]:
# #   if not visited[i]:
# #    queue.append(i)
# #    visited[i] = True

