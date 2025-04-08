N = int(input())
students = [list(map(int,input().split())) for _ in range(N**2)]
graph=[[0]*N for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def in_range(x,y):
    return 0<=x<N and 0<=y<N

for student in students:
    total=[]
    for i in range(N):
        for j in range(N):
            if graph[i][j]==0:
                prefer, empty = 0, 0

                for d in range(4):
                    nx, ny=i+dx[d], j+dy[d]

                    if in_range(nx,ny) and graph[nx][ny]==0:
                        empty+=1
                    if in_range(nx,ny) and graph[nx][ny] in student[1:]:
                        prefer+=1
                total.append((prefer,empty,i,j))
    total.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))
    graph[total[0][2]][total[0][3]]=student[0]

answer=0
score=[0,1,10,100,1000]
students.sort()

for i in range(N):
    for j in range(N):
        count=0

        for d in range(4):
            nx,ny=i+dx[d],j+dy[d]

            if in_range(nx,ny) and graph[nx][ny] in students[graph[i][j]-1]:
                count+=1
        answer+=score[count]
print(answer)

