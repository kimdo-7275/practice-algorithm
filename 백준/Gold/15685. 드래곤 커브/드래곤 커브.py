n=int(input())
arr=[[0]*101 for _ in range(101)]

di=[0,-1,0,1]
dj=[1,0,-1,0]

def rotate_dragon(si,sj,points):
    new_points=set()
    for i,j in points:
        ti=si-sj+j
        tj=si+sj-i
        arr[ti][tj]=1
        new_points.add((ti,tj))
        if i==y and j==x:
            ni,nj=ti,tj
    points.update(new_points)
    return ni,nj,points

for _ in range(n):
    x,y,d,g=map(int,input().split())
    points=set()
    points.add((y,x))
    arr[y][x]=1
    points.add((y+di[d],x+dj[d]))
    arr[y+di[d]][x+dj[d]]=1
    si,sj=y+di[d],x+dj[d]
    for _ in range(g):
        si,sj,points=rotate_dragon(si,sj,points)

answer=0
for i in range(100):
    for j in range(100):
        if arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]==4:
            answer+=1
print(answer)