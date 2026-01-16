n=int(input())
lst=[input() for _ in range(n)]
answers=[]
keys=[]
def find_key(option):
    # 1. 단어 첫 글자인 경우
    for i in range(len(option)):
        if i==0 or option[i-1]==' ':
            if option[i].lower() not in keys:
                keys.append(option[i].lower())
                append_answer(i,option)
                return
    # 2. 단어 첫 글자 아닌 경우
    for i in range(len(option)):
        if option[i]!=' ' and option[i].lower() not in keys:
            keys.append(option[i].lower())
            append_answer(i,option)
            return
    answers.append(option)
def append_answer(idx,option):
    answer=''
    for i in range(len(option)):
        if i==idx:
            answer+='['
            answer+=option[i]
            answer+=']'
        else:
            answer+=option[i]
    answers.append(answer)
for option in lst:
    find_key(option)
for i in answers:
    print(i)
