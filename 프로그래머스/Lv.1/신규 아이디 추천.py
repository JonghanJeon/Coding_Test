# 아이디 길이 3자 이상 15자 이하
# 아이디는 소문자, 숫자, 바, 언더바, 마침표 문자만 사용 가능
# 마침표는 처음과 끝에 사용할 수 없으며 연속으로 사용 불가


def solution(new_id):
    leng = len(new_id)
    # 1단계
    new_id = new_id.lower()
    # 2단계
    es_li = [126, 33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 61, 43, 91, 123, 93, 125, 58, 63, 44, 60, 62, 47]
    for item in es_li:
        new_id = new_id.replace(chr(item), "").strip()
    # 3단계, 4단계
    li = [x for x in new_id.split('.') if x]
    new_id = '.'.join(li)
    new_id = new_id.strip('.')
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 7단계
    if len(new_id) <= 2:
        for _ in range(3-len(new_id)):
            new_id += new_id[-1]
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    new_id = new_id.strip('.')
    return new_id