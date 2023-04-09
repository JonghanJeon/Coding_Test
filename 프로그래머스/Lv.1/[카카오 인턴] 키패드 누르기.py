def move_right(right, num, answer):
    right = num
    answer += 'R'
    return right, answer

def move_left(left, num, answer):
    left = num
    answer += 'L'
    return left, answer

def solution(numbers, hand):
    answer = ''
    dic = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    }
    left, right = '*', '#'
    for num in numbers:
        if num in [3, 6, 9]:
            right, answer = move_right(right, num, answer)
        elif num in [1, 4, 7]:
            left, answer = move_left(left, num, answer)
        else:
            dif_r = sum([abs(x-y) for x, y in zip(dic[num], dic[right])])
            dif_l = sum([abs(x-y) for x, y in zip(dic[num], dic[left])])
            if dif_r < dif_l:
                right, answer = move_right(right, num, answer)
            elif dif_r > dif_l:
                left, answer = move_left(left, num, answer)
            else:
                if hand == 'right':
                    right, answer = move_right(right, num, answer)
                else:
                    left, answer = move_left(left, num, answer)
    return answer