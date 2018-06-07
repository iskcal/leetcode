def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if __name__ == '__main__':
    print(strStr('aaaaa', 'bba'))