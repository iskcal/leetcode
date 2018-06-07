def generateParenthesis(n):
    if n == 0:
        return []   
    result = []
    for i in range(1, n+1):
        if i == 1:
            result = ['()']
        else:
            last_r = result
            result = []
            for ps in last_r:
                j = 0
                while j <= len(ps):
                    compo = list(ps)
                    compo.insert(j, '(')
                    compo.append(')')
                    compo = ''.join(compo)
                    if compo not in result:
                        result.append(compo) 
                    while j < len(ps) and ps[j] == '(':
                        j += 1
                    j += 1
    return result
                    
if __name__ == '__main__':
    print(generateParenthesis(3))