def convert(s, numRows):
        p = []
        if len(s) == 0 or numRows == 1:  # 如果为空字符串，或者不分行
            return s
        for i in range(2*(numRows-1)): # 按照|/方式切分成2*(nuwRows-1)行
            p.append(s[i::2*(numRows-1)])
            
        t = ''
        for i in range(numRows):
            if i > 0 and i < numRows-1: # 当不为竖线的头尾两行时，需要对相应的双行合并成新一行
                p[i] = merge(p[i], p[2 * numRows - 2 - i])
            t = t + p[i]
        return t

def merge(p, s):
    t = [kv for r in zip(p, s) for kv in r]
    pl = len(p)
    sl = len(s)

    if pl > sl:
        t.extend(p[sl:])
    elif sl > pl:
        t.extend(s[pl:])
    return ''.join(t)

if __name__=='__main__':
    tt = convert("A", 1)