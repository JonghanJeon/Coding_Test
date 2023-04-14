def timetomin(s):
    h, m = map(int, s.split(':'))
    return h*60 + m

def solution(plans):
    answer = []
    stop = []
    for item in plans:
        item[1] = timetomin(item[1])
        item[2] = int(item[2])
    plans.sort(key = lambda x : x[1])
    for idx in range(len(plans)):
        # 시작, 종료 시간 구하기
        st = plans[idx][1]
        et = plans[idx][1] + plans[idx][2]
        if idx + 1 < len(plans):
            # 다음 시작 시간
            next_st = plans[idx+1][1]
            # 과제 못끝낼때
            if et > next_st:
                plans[idx][2] -= next_st - st
                stop.append([plans[idx][0], plans[idx][2]])
            # 과제 끝낼 수 있을 때
            else:
                answer.append(plans[idx][0])
                # 비는 시간
                rt = next_st - et
                # 대기중인 과제 있고 비는 시간 있으면
                if stop and rt > 0:
                    leng = len(stop)
                    # 대기중인 과제 여러개 일 수있어서 while 문으로 시도 했으나 런타임 에러 발생하여 while문을 for 문으로 대체
                    # 각 조건마다 break문 달아줌.
                    for idx in range(leng):
                        title, play = stop[-1]
                        if play < rt:
                            stop.pop()
                            answer.append(title)
                            rt -= play
                        elif play == rt:
                            stop.pop()
                            answer.append(title)
                            break
                        else:
                            stop[-1][1] -= rt
                            break
            
        else:
            answer.append(plans[idx][0])
    
    n = len(stop)
    for _ in range(n):
        answer.append(stop.pop()[0])
        
    return answer