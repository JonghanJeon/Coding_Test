def solution(wallpaper):
    answer = [50, 50, 0, 0]
    
    for r, row in enumerate(wallpaper):
        for c, letter in enumerate(row):
            if letter == '#':
                answer = [
                    min(answer[0], r), min(answer[1], c),
                    max(answer[2], (r+1)), max(answer[3], (c+1))
                ]
                
    return answer