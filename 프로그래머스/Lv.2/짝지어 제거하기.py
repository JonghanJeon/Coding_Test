def solution(s):
    stack = []
    for item in s:
        if not stack:
            stack.append(item)
        else:
            if item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)
    
    if stack:
        return 0
    else:
        return 1