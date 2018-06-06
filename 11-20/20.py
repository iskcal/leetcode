def isValid(s):
    st = []
    for c in s:
        if c in ['(', '[', '{']:
            st.append(c)
        elif c == ')':
            if len(st) == 0 or st.pop() != '(':
                return False
        elif c == ']':
            if len(st) == 0 or st.pop() != '[':
                return False
        elif c == '}':
            if len(st) == 0 or st.pop() != '{':
                return False
        else:
            return False
    if len(st) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isValid('{[]}'))