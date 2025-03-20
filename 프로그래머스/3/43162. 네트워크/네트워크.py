from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i]==False:
            BFS(n, computers, i, visited)
            answer+=1
            
    return answer

def BFS(n, computers, i, visited):
    visited[i]=True
    queue = deque()
    queue.append(i)
    
    while len(queue)>0:
        com = queue.pop()
        visited[com]=True
        for i in range(n):
            if i!=com and visited[i]==False and computers[i][com]:
                queue.append(i)
    
    
    