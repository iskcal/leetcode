def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else:
        for ch_i in range(len(strs[0])):
            for word in strs:
                if ch_i > len(word)-1:
                    return strs[0][0:ch_i]
                else:
                    if strs[0][ch_i] != word[ch_i]:
                        return strs[0][0:ch_i]
        return strs[0]

if __name__ == '__main__':
    print(longestCommonPrefix(["flowersss","flowers"]))