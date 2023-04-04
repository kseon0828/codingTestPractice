from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, -1, 1] #상하좌우
dy = [-1, 1, 0, 0]

queue = deque()

def bfs(graph, x, y):
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1 #각 단지의 첫 번째 집(탐색 첫 start!)

    while queue:
        #queue가 없을 때 까지 진행하는 것으로
        #각 단지 탐색
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny<0 or ny>= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt+= 1
    return cnt

home_num = []

for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            home_num.append(bfs(graph, i, j))

home_num.sort()
print(len(home_num))

for i in range(len(home_num)):
    print(home_num[i])