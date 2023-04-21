def solution(s):
    answer = True
    stack = []
    for item in s:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return len(stack) == 0