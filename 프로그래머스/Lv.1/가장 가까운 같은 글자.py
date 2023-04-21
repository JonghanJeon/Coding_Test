def solution(s):
    dic = {}
    answer = []
    for idx, spell in enumerate(s):
        if spell not in dic:
            dic[spell] = idx
            answer.append(-1)
        else:
            answer.append(idx - dic[spell])
            dic[spell] = idx
    return answer