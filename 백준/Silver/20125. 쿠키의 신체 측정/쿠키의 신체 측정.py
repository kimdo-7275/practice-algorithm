n=int(input())
lst = list(input() for _ in range(n))

# 심장 찾기(출력할 때만 +1 하기)
h_i=-1
for i in range(n):
    for j in range(n):
        if lst[i][j]=='*':
            h_i, h_j = i+1, j
            break
    if h_i!=-1:
        break

l_a, r_a, w, l_l, r_l = 0,0,0,0,0
while h_j-l_a>0:
    if lst[h_i][h_j-(l_a+1)]=='*':
        l_a+=1
    else:
        break
while h_j+r_a<n-1:
    if lst[h_i][h_j+(r_a+1)]=='*':
        r_a+=1
    else:
        break
while h_i+w<n:
    if lst[h_i+(w+1)][h_j]=='*':
        w+=1
    else:
        break
while h_i+w+l_l<n-1:
    if lst[h_i+w+l_l+1][h_j-1]=='*':
        l_l+=1
    else:
        break
while h_i+w+r_l<n-1:
    if lst[h_i+w+r_l+1][h_j+1]=='*':
        r_l+=1
    else:
        break
print(h_i+1, h_j+1)
print(l_a, r_a, w, l_l, r_l)