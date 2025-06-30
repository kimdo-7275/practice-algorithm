from collections import deque

def one_alphabet(w1,w2):
    dif_alpha = 0
    for i in range(len(w1)):
        if w1[i]!=w2[i]:
            dif_alpha+=1
        if dif_alpha>=2:
            return False    
    return True
    
    

def solution(begin, target, words):
    answer = 0
    if target not in words : return 0
    v = [0] * len(words)
    q=deque()
    q.append((begin,0))
    while q:
        word,dis = q.popleft()
        for i,w in enumerate(words):
            if one_alphabet(word,w) and v[i]==0:
                q.append((w,dis+1))
                v[i]=dis+1
    for i,w in enumerate(words):
        if w==target:
            answer = v[i]
    
    
    return answer
    