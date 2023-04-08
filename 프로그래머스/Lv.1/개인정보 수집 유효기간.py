"""
오늘 날짜를 의미하는 문자열 today, 
약관의 유효기간을 담은 1차원 문자열 배열 terms,
수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다.
today는 "YYYY.MM.DD" 형태로 오늘 날짜를 나타냅니다.
terms의 원소는 "약관 종류 유효기간" 형태의 약관 종류와 유효기간을 공백 하나로 구분한 문자열입니다.
privacies[i]는 i+1번 개인정보의 수집 일자와 약관 종류를 나타냅니다.
privacies의 원소는 "날짜 약관 종류" 형태의 날짜와 약관 종류를 공백 하나로 구분한 문자열 입니다.
privacies의 약관 종류는 항상 terms에 나타난 약관 종류만 주어집니다.
파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return
"""
def solution(today, terms, privacies):
    answer = []
    dic = {}

    for item in terms:
        t_type, t_int = item.split()
        dic[t_type] = int(t_int)

    to_year, to_month, to_date = map(int, today.split('.'))
    to = to_year*12*28 + to_month*28 + to_date

    for idx, item in enumerate(privacies):
        day, d_type = map(str, item.split())
        year, month, date = map(int, day.split('.'))

        month += dic[d_type]
        ef = year*12*28 + month*28 + date-1

        if ef < to:
            answer.append(idx+1)
        
    return answer