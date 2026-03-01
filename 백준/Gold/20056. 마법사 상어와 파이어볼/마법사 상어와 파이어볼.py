N,M,K = map(int,input().split())
main_dict={}
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    main_dict[(r-1,c-1)]=[[m,s,d]]
def move_ball(main_dict):
    new_dict={}
    for r,c in main_dict:
        for m,s,d in main_dict[(r,c)]:
            nr,nc=(r+dx[d]*s)%N,(c+dy[d]*s)%N
            if (nr,nc) not in new_dict:
                new_dict[(nr,nc)]=[[m,s,d]]
            else:
                new_dict[(nr,nc)].append([m,s,d])
    return new_dict
def sum_divide(main_dict):
    new_dict={}
    for r,c in main_dict:
        if len(main_dict[(r,c)])==1:
            new_dict[(r, c)] = [x[:] for x in main_dict[(r,c)]]
            continue
        hol,jjak=0,0
        sum_m,sum_s=0,0
        l=len(main_dict[(r,c)])
        for m,s,d in main_dict[(r,c)]:
            sum_m+=m
            sum_s+=s
            if d%2==0:
                jjak+=1
            else:
                hol+=1
        new_m=sum_m//5
        new_s=sum_s//l
        if new_m==0:
            continue
        if hol==l or jjak==l:
            for d in (0,2,4,6):
                if (r,c) in new_dict:
                    new_dict[(r,c)].append([new_m,new_s,d])
                else:
                    new_dict[(r, c)]=[[new_m,new_s,d]]
        else:
            for d in (1,3,5,7):
                if (r, c) in new_dict:
                    new_dict[(r, c)].append([new_m, new_s, d])
                else:
                    new_dict[(r, c)] = [[new_m,new_s,d]]
    return new_dict
for _ in range(K):
    main_dict=move_ball(main_dict)
    main_dict=sum_divide(main_dict)
answer=0
for r,c in main_dict:
    for m,s,d in main_dict[(r,c)]:
        answer+=m
print(answer)

