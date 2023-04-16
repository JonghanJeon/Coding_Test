def solution(k, score):
    li = []
    answer = []
    for item in score:
        li.append(item)
        li.sort()
        li = li[::-1]
        if len(li) < k:
            answer.append(li[len(li)-1])
        else:
            answer.append(li[k-1])
    return answer