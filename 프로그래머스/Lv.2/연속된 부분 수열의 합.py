def solution(sequence, k):
    answer = []
    # 누적합 저장할 0으로 채워진 리스트 생성
    li_sum = [0 for x in range(0,len(sequence)+1)]
    # 인덱싱 변수
    left, right = 0, 0
    # 길이 확인용 변수
    ln = len(sequence)
    
    # for문을 통하여 누적 합 구함.
    for idx in range(0, len(sequence)):
        li_sum[idx+1] = li_sum[idx] + sequence[idx]
    
    # 인덱스 조건으로
    while left <= right < len(li_sum):
        # 합을 구하고
        check = li_sum[right] - li_sum[left]
        #합을 체크했을때
        if check < k:
            # 작다면 끝 인덱스 1 증가
            right += 1
        elif check == k:
            # 같다면
            if ln > (right-1) - left:
                # 시작 인덱스가 작은 수열을 출력해야 하므로 >= 가 아닌 >
                ln = (right-1) - left
                answer = [left, right-1]
            # 끝 인덱스 증가
            left += 1
        else: # check > k
            # 크다면 시작 인덱스 증가
            left += 1
    
    return answer