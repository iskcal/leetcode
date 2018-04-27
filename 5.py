def longestPalindrome(s):
    t = '#' +  '#'.join(list(s)) + '#'
    p = createP(t) # 获得P数组

    p_max = max(p)  # 获取P数组最大值
    p_index = p.index(p_max)    # 获取相对应的索引

    return t[p_index-p_max+2:p_index+p_max-2+1:2] # 加1是因为切片时候是不包含后端的

def createP(s):
    p = [1] * len(s)
    id = 0
    mx = 0
    for i in range(len(s)):
        p[i] = min(p[2*id-i], mx-i) if mx > i else 1
        while i+p[i]<len(s) and i-p[i] >= 0 and s[i+p[i]] == s[i-p[i]]: # 继续寻找
            p[i] += 1
        if i+p[i] > mx:
            id = i
            mx = i+p[i]
    return p

if __name__ == '__main__':
    ar = longestPalindrome('12212321')
    print(ar)