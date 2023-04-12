def solution(id_list, report, k):
    re_dic = {}
    answer = [0]*len(id_list)
    dic = {}
    for item in id_list:
        re_dic[item] = 0
        dic[item] = []
    for item in set(report):
        a, b = item.split()
        re_dic[b] += 1
        dic[a].append(b)
    re_li = []
    for key in re_dic:
        if re_dic[key] >= k:
            re_li.append(key)
    for item in re_li:
        for key in dic:
            if item in dic[key]:
                answer[id_list.index(key)] += 1
    return answer