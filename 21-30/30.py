def findSubstring(s, words):
    items = [words[i]+words[j] for i in range(len(words)) for j in range(len(words)) if i != j]
    record = []
    for item in items:
        index = s.find(item)
        if index != -1:
            record.append(index)
    return record

if __name__ == '__main__':
    print(findSubstring("barfoothefoobarman", ["foo","bar"]))