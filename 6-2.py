def convert(s, numRows):
    if len(s) == 0 or numRows == 1:
        return s
    
    period = 2 * (numRows - 1)

    t = ''
    for i in range(numRows):
        for j in range(i, len(s), period):
            t += s[j]
            other_j = j + period - 2 * i
            if i != 0 and i != numRows-1 and other_j < len(s):
                t += s[other_j]
    
    return t

if __name__=='__main__':
    tt = convert("PAYPALISHIRING", 3)