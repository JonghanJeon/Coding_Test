def solution(board, moves):
    basket = {}
    lev = 0
    answer = 0
    for order in moves:
        for idx, line in enumerate(board):
            if line[order-1] == 0:
                continue
            else:
                if lev == 0:
                    basket[lev] = line[order-1]
                    line[order-1] = 0
                    lev += 1
                    break
                else:
                    basket[lev] = line[order-1]
                    line[order-1] = 0
                    if basket[lev] == basket[lev-1]:
                        del basket[lev]
                        del basket[lev-1]
                        lev -= 1
                        answer += 2
                        break
                    else:
                        lev += 1
                        break
    return answer