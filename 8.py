def myAtoi(str):
    s = str.lstrip(' ')
    r = 0
    sig = 1
    for i in range(len(s)):
        data = ord(s[i])-ord('0') if '0'<=s[i]<='9' else s[i]
        if isinstance(data, int): # 为数字时
            if sig == 1 and (r > 2147483647 // 10 or (r == 2147483647 // 10 and data > 7)):
                return 2147483647
            elif sig == -1 and (r > 2147483648 // 10 or (r == 2147483647 // 10 and data > 8)):
                return -2147483648
            r = r * 10 + data
        elif data in ['+', '-'] and i == 0: # 第一位为正负号时
            sig = -1 if data == '-' else 1
        else:
            break
    return r * sig

if __name__ == '__main__':
    tt = myAtoi("-2147483647")
    print(tt)