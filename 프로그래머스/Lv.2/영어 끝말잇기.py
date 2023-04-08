def solution(n, words):
    answer = [0, 0]
    # 스택을 활용하여 풀이
    # 스택에 첫 단어 넣기
    stack = [words[0]] 
    # 두 번째 글자부터 인덱스 받아오기
    for idx in range(1, len(words)):
        # 마지막 단어의 끝 글자와 새 단어의 첫글자가 같을경우.
        # 이미 나온 단어가 아닐경우
        if stack[-1][-1] == words[idx][0] and words[idx] not in stack:
            # 스택에 삽입
            stack.append(words[idx])
        # 끝말잇기 규칙에 위반하는 경우.
        else:
            # 틀린 사람 번호
            answer[0] = idx % n + 1
            # 틀린 사람이 말한 단어의 개수
            answer[1] = idx // n + 1
            break
    return answer