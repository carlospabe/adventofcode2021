def get_input(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.read().splitlines()
        
        entry = {
            'digits': list(),
            'display': list()
        }
        input = list()
        for line in lines:
            digits, display = line.split(' | ')
            entry['digits'] = digits.split(' ')
            entry['display'] = display.split(' ')    
            input.append(entry.copy())
        
        return input
    

def part1(input: list(dict())):
    valid = [2,3,4,7]
    values = 0
    for entry in input:
        for sev_seg_disp in entry['display']:
            if len(sev_seg_disp) in valid:
                values += 1
            
    return values


def part2(input: list(dict())):
    def get_decoder(digits: list()):
        def contains_all(str1, str2):
            return 0 not in [c in str1 for c in str2]
        
        def is_contained(str1, str2):
            return 0 not in [c in str2 for c in str1]
        
        def order_digits(digits):
            ordered = list()
            len2 = [digit for digit in digits if len(digit) == 2]
            len3 = [digit for digit in digits if len(digit) == 3]
            len4 = [digit for digit in digits if len(digit) == 4]
            len7 = [digit for digit in digits if len(digit) == 7]
            len6 = [digit for digit in digits if len(digit) == 6]
            len5 = [digit for digit in digits if len(digit) == 5]
            ordered = ordered + len2 + len3 + len4 + len7 + len6 + len5
            return ordered

        decoding = dict()
        digits = order_digits(digits)
        
        for digit in digits:
            digit = sorted(digit)
            if len(digit) == 2: 
                decoding[1] = digit
            elif len(digit) == 3:
                decoding[7] = digit
            elif len(digit) == 4:
                decoding[4] = digit
            elif len(digit) == 7:
                decoding[8] = digit
            elif len(digit) == 6:
                if contains_all(digit, decoding[4]):
                    decoding[9] = digit
                elif contains_all(digit, decoding[7]):
                    decoding[0] = digit
                else:
                    decoding[6] = digit
            elif len(digit) == 5:
                if contains_all(digit, decoding[7]):
                    decoding[3] = digit
                elif is_contained(digit, decoding[9]):
                    decoding[5] = digit
                else:
                    decoding[2] = digit
        
        decoder = dict()
        for key, value in decoding.items():
            decoder[str(sorted(value))] = str(key)
            
        return decoder
    
    outs = list()
    
    for entry in input:
        decoder = get_decoder(entry['digits'])
        
        out = ""
        for display in entry['display']:
            key = str(sorted(display))
            out = out + decoder[key]
        outs.append(int(out))
        
    return sum(outs)


path = '08/08_input.txt'
input = get_input(path)

print(part1(input))
print(part2(input))
        