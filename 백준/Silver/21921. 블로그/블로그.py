N, X = map(int, input().split())
visit_lst = list(map(int, input().split()))
mx_visit = 0
mx_day_cnt = 1
s = 0
e = s + X - 1
for i in range(X):
    mx_visit += visit_lst[i]
tmp_visit = mx_visit - visit_lst[s]
s += 1
e += 1
while e < N:
    tmp_visit += visit_lst[e]
    if mx_visit > tmp_visit:
        pass
    elif mx_visit < tmp_visit:
        mx_visit = tmp_visit
        mx_day_cnt = 1
    elif mx_visit == tmp_visit:
        mx_day_cnt+=1
    tmp_visit-=visit_lst[s]
    s+=1
    e+=1
if mx_visit==0:
    print('SAD')
else:
    print(mx_visit)
    print(mx_day_cnt)