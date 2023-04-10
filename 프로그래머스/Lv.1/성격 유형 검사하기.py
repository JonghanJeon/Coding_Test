def solution(survey, choices):
    dic={
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    ch_dic = {
        1 : 3,
        2 : 2,
        3 : 1,
        5 : 1,
        6 : 2,
        7 : 3
    }
    li = ["RT", "CF", "JM", "AN"]
    answer = ''
    for idx in range(len(survey)):
        i_1, i_2 = survey[idx][0], survey[idx][1]
        if choices[idx] > 4:
            dic[i_2] = dic[i_2] + ch_dic[choices[idx]]
        elif choices[idx] < 4:
            dic[i_1] = dic[i_1] + ch_dic[choices[idx]]
    for item in li:
        if dic[item[0]] < dic[item[1]]:
            answer += item[1]
        else:
            answer += item[0]
    return answer