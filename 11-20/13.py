def romanToInt(s):
        alphabet = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        num = 0
        i = 0
        while i < len(s):
            if i==len(s)-1 or alphabet[s[i]] >= alphabet[s[i+1]]:
                num += alphabet[s[i]]
                i += 1
            else:
                num += (alphabet[s[i+1]] - alphabet[s[i]])
                i += 2
        return num

if __name__ == '__main__':
    print(romanToInt('MCMXCIV')) 
