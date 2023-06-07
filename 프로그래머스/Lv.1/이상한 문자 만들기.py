def solution(s):
    # 문자열을 배열로 만들어 주기
    s = list(s)
    # 단어안에 문자 순서 카운트할 변수.
    cnt = 0
    for idx in range(len(s)):
        # 공백 발견시 cnt 0으로 초기화
        if s[idx] == ' ':
            cnt = 0 
            continue
        # 공백이 아닌 경우 짝수일 경우 대문자로, 홀수일 경우 소문자로 만들어 주기
        s[idx] = s[idx].upper() if cnt % 2 == 0 else s[idx].lower()
        # cnt 1 추가
        cnt += 1
    # 리스트 를 join 으로 이어 붙여 문자열로 변환.
    return ''.join(s)