def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    li1 = []
    li2 = []
    # 공백과 특수문자가 포함되지 않은 원소 list 에 할당.
    for idx in range(len(str1)-1):
        if str1[idx].isalpha() and str1[idx+1].isalpha():
            if str1[idx] != " " and str1[idx+1] != " ":
                li1.append(str1[idx]+str1[idx+1])
    for idx in range(len(str2)-1):
        if str2[idx].isalpha() and str2[idx+1].isalpha():
            if str2[idx] != " " and str2[idx+1] != " ":
                li2.append(str2[idx]+str2[idx+1])
    # 두 집합의 교집합과 합집합 구하기
    union = list(set(li1) | set(li2))
    intersection = list(set(li1) & set(li2))
    # 교집합과 합집합에서 교집합은 min 으로, 합집합은 max 로 개수 count
    cnt_g, cnt_h = 0, 0
    for item in union:
        cnt_h += max(li1.count(item), li2.count(item))
    for item in intersection:
        cnt_g += min(li1.count(item), li2.count(item))
    # 출력
    if cnt_g == 0 and cnt_h == 0:
        return 65536
    else:
        return int((cnt_g/cnt_h)*65536)