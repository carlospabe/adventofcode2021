def get_report():
    with open("03/03_input.txt", 'r', encoding='utf-8-sig') as f:
        return f.read().splitlines()


def part_1(report):
    len_r = len(report[0])
    counting = [0, 0]
    counted = list()
    for i in range(len_r):
        counted.append(counting.copy())
        
    for r in report:
        for i in range(len_r):
            counted[i][int(r[i])] += 1
            
    gamma_bin = ''
    epsilon_bin = ''
    for c in counted:
        if c[0] > c[1]:
            gamma_bin += '0'
            epsilon_bin += '1'
        else:
            gamma_bin += '1'
            epsilon_bin += '0'
            
    gamma_dec = int(gamma_bin, 2)
    epsilon_dec = int(epsilon_bin, 2)
    return gamma_dec * epsilon_dec


def part_2(report):
    def get_o2_rating(report):
        len_r = len(report[0])
        
        o2_rating = report.copy()
        i = 0
        while len(o2_rating) > 1 and i < len_r:
            count = [0, 0]
            for r in o2_rating:
                count[int(r[i])] += 1
            
            if count[0] > count[1]:
                bit = 0
            else:
                bit = 1
            
            new_o2_rating = list()
            for r in o2_rating:
                if int(r[i]) == bit:
                    new_o2_rating.append(r)
            
            o2_rating = new_o2_rating.copy()
                    
            i += 1
            
        return int(o2_rating[0], 2)
    
    def get_co2_rating(report):
        len_r = len(report[0])
        
        co2_rating = report.copy()
        i = 0
        while len(co2_rating) > 1 and i < len_r:
            count = [0, 0]
            for r in co2_rating:
                count[int(r[i])] += 1
            
            if count[0] <= count[1]:
                bit = 0
            else:
                bit = 1
            
            new_co2_rating = list()
            for r in co2_rating:
                if int(r[i]) == bit:
                    new_co2_rating.append(r)
            
            co2_rating = new_co2_rating.copy()
                    
            i += 1
        
        return int(co2_rating[0], 2)
    
    o2_rating = get_o2_rating(report)
    co2_rating = get_co2_rating(report)
    return o2_rating * co2_rating
    

report = get_report()

print(part_1(report))
print(part_2(report))