n,k = map(int,input().split())
st=list(input())

ran=[]
for i in range(1,k+1):
    ran.append(-i)
    ran.append(i)
ran.sort()

count=0

for i in range(n):
    if st[i]=='H' or st[i]=='0':
        continue
    if st[i]=='P':
        for j in ran:
            if 0<=i+j<n and st[i+j]=='H':
                count+=1
                st[i+j]='0'
                break
print(count)