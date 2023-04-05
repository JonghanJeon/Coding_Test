def solution(keymap, targets):
    answer = []
    
    for item in targets:
        result = 0
        no_search = False
        for spell in item:
            no_spell = 0
            MIN = 101
            # 얼마나 눌러야 하는지 계산
            for key in keymap:
                if spell in key:
                    if(key.index(spell)+1 < MIN):
                        MIN = key.index(spell)+1
                elif spell not in key:
                    no_spell += 1
            if no_spell == len(keymap):
                no_search = True
            result += MIN
        #answer에 집어넣기
        if no_search:
            answer.append(-1)
        else:
            answer.append(result)
                
    return answer