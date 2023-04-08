def solution(s):
    sam_cnt = 0 # 같은 글자 개수
    dif_cnt = 0 # 다른 글자 개수
    answer = 0 # 정답
    first_s = s[0] # 첫글자 설정
    for idx, item in enumerate(s):
        if item == first_s: # 같으면 같은 글자수 count
            sam_cnt += 1
        else: # 다르면 다른 글자수 count
            dif_cnt += 1
        if sam_cnt == dif_cnt: # 같은 글자수와 다른 글자수가 같을때
            answer += 1 # 정답 개수 추가
            sam_cnt, dif_cnt = 0, 0 # 같은 글자수, 다른 글자수 초기화
            if idx < len(s)-1:
                first_s = s[idx+1] # 첫글자는 그 다음 글자
        if idx == (len(s-1)) and sam_cnt != dif_cnt: # 문장의 끝에서 같은 글자수와 다른 글자수가 같을 경우
            answer += 1 # 정답 추가하고 끝
    return answer