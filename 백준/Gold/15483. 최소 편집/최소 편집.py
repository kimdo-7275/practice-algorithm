str1=input()
str2=input()
str1, str2 = str1.lower(), str2.lower()
l_str1,l_str2 = len(str1),len(str2)
lst=[[0] * (l_str2+1) for _ in range(l_str1+1)]
for i in range(l_str2+1): lst[0][i]=i
for i in range(l_str1+1): lst[i][0]=i
for i in range(l_str1):
    for j in range(l_str2):
        if str1[i]==str2[j]:
            lst[i+1][j+1]=lst[i][j]
        else:
            lst[i+1][j+1]=min(1+min(lst[i+1][j],lst[i][j+1]),1+lst[i][j])
print(lst[l_str1][l_str2])