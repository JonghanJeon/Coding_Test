def solution(cards1, cards2, goal):
    search = False
    idx1, idx2 = 0, 0
    for item in goal:
        if item == cards1[idx1]:
            if idx1 < (len(cards1)-1):
                idx1 += 1
            search = True
        elif item == cards2[idx2]:
            if idx2 < (len(cards2)-1):
                idx2 += 1
            search = True
        else:
            return 'No'
    if search:
        return 'Yes'