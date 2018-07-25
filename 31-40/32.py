def longestValidParentheses(s):
    num = 0
    if len(s) < 2:
        return num
    match = []
    match.append(['#', 0])

    for c in s:
        if c == '(':
            match.append(['(', 0])
        elif c == ')':
            data = match.pop()
            if data[0] == '#':
                match.append(['#', 0]) 
                num = num if num > data[1] else data[1]
            elif data[0] == '(':
                match[len(match)-1][1] = match[len(match)-1][1] + (data[1] + 1)
    
    while len(match) > 0:
        data = match.pop()
        if data[1] > 0:
            num = num if num > data[1] else data[1]
    return num * 2

def test_longestValidParentheses():
    assert longestValidParentheses('(()') == 2
    assert longestValidParentheses(')()())') == 4
    assert longestValidParentheses('(') == 0
    assert longestValidParentheses('(((((((((') == 0
    assert longestValidParentheses(')') == 0
    assert longestValidParentheses(')))))))))') == 0
    assert longestValidParentheses('())') == 2
    assert longestValidParentheses('())()()') == 4
    assert longestValidParentheses('()())()') == 4
    assert longestValidParentheses('()())))))))()()()') == 6
    assert longestValidParentheses('()()(((((((((()))') == 6
    assert longestValidParentheses('()()()()()()') == 12

if __name__ == '__main__':
    print(longestValidParentheses(')()())'))