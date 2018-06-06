def intToRoman(num):
    return intToRomanCore(num, [1000, 500, 100, 50, 10, 5, 1], ['M', 'D', 'C', 'L', 'X', 'V', 'I'])

def intToRomanCore(num, num_list, alpha_list):
    for i in range(0, len(num_list)):
        if num // num_list[i] > 0:  # 表示在该位上
            if i % 2 == 0 and num // num_list[i] == 4: # 差额为4
                s = alpha_list[i]+alpha_list[i-1]
                num = num - num_list[i] * 4
            elif i % 2 == 1 and num // num_list[i+1] == 9: # 9
                s = alpha_list[i+1]+alpha_list[i-1]
                num = num - num_list[i+1] * 9
            else:
                s = alpha_list[i]
                num = num - num_list[i]
            break
    
    if num == 0:
        return s
    else:
        return s + intToRomanCore(num, num_list, alpha_list)

if __name__ == '__main__':
    print(intToRoman(4))