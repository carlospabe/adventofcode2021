def get_input():
    with open("04/04_input.txt", 'r', encoding='utf-8-sig') as f:
        numbers = list(map(int, f.readline().split(',')))
        
        cardboards = list()
        cb_checker = list()
        lines = f.read().split('\n')
        for i in range(0, len(lines)-1, 6):
            cb = list()
            for j in range(1, 6):
                cb.append(list(map(int, lines[i+j].split())))
            cardboards.append(cb)
            
            cb_chk_line = [0] * 5
            cb_chk = list()
            for i in range(5):
                cb_chk.append(cb_chk_line.copy())
            cb_checker.append(cb_chk.copy())
    
    return numbers, cardboards, cb_checker


def mark_cardboard(cb_count, n, cardboards, cb_checker):
    for i in range(5):
        for j in range(5):
            if cardboards[cb_count][i][j] == n:
                cb_checker[cb_count][i][j] = 1
    
    
def is_win(cb_count, cb_checker):
    try:
        is_win = False
        
        for i in range(5):
            cl = [ln[i] for ln in cb_checker[cb_count]]
            if all(cb_checker[cb_count][i]) or all(cl):
                is_win = True
                break
            
        return is_win
    except Exception as e:
        print('weeee')


def count_unmarked(cb_count, cardboards, cb_checker):
    unmarked = 0
    for i in range(5):
        for j in range(5):
            if not cb_checker[cb_count][i][j]:
                unmarked += cardboards[cb_count][i][j]
    return unmarked
    
    
def part_1(numbers, cardboards, cb_checker):    
    won = False
    for n in numbers:
        for cb_count in range(100):
            mark_cardboard(cb_count, n, cardboards, cb_checker)
            if is_win(cb_count, cb_checker):
                won = True
                break
        if won:
            break
        
    res = count_unmarked(cb_count, cardboards, cb_checker) * n
    return res


def part_2(numbers, cardboards, cb_checker):
    for n in numbers:
        for cb_count in range(len(cardboards)):
            mark_cardboard(cb_count, n, cardboards, cb_checker)
            
        cb_copy = cardboards.copy()
        cb_chk_copy = cb_checker.copy()
        n_del = 0
        for cb_count in range(len(cardboards)):
            if is_win(cb_count, cb_checker):
                if len(cardboards) != 1:
                    del cb_copy[cb_count - n_del]
                    del cb_chk_copy[cb_count - n_del]
                    n_del += 1
                    
        cardboards = cb_copy.copy()
        cb_checker = cb_chk_copy.copy()
        # if len(cardboards) == 1:
        #     print('polla')

        if is_win(0, cb_checker) and len(cardboards) == 1:
            break
        
    res = count_unmarked(0, cardboards, cb_checker) * n
    return res
    


numbers, cardboards, cb_checker = get_input()

print(part_1(numbers, cardboards, cb_checker))
print(part_2(numbers, cardboards.copy(), cb_checker.copy()))