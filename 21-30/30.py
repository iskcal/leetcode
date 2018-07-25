def findSubstring(s, words):
    res = []
    if len(s) == 0 or len(words) == 0:
        return res
    word_num = len(words)
    word_len = len(words[0])
    s_len = len(s)
    w_dict = {}
    for word in words:
        w_dict[word] = w_dict.get(word, 0) + 1
    for start in range(0, word_len):
        count = 0
        silde_window = {}
        for i in range(start, s_len, word_len):
            word = s[i:i+word_len]
            if word not in w_dict:
                silde_window = {}
                count = 0 
            else:
                silde_window[word] = silde_window.get(word, 0) + 1
                count += 1
                while silde_window[word] > w_dict[word]:
                    remove_word = s[i-(count - 1)*word_len:i-(count - 1)*word_len+word_len]
                    silde_window[remove_word] -= 1
                    count -= 1
            if count == word_num:
                res.append(i - (count - 1) * word_len)
    
    return res


if __name__ == '__main__':
    print(findSubstring("barfoothefoobarman", ["foo","bar"]))