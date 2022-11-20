def operation(lst: list):
    if '(' in lst:
        start = 0
        for ind in range(len(lst)):
            if lst[ind] == '(':
                start = ind
        fin = start + lst[start:].index(')')
        tmp = operation(lst[start + 1:fin])
        return operation(lst[:start] + [tmp] + lst[fin + 1:])
    if '-' in lst:
        if lst[0] == '-':
            lst[1] *= -1
            lst.pop(0)
        for ind in range(len(lst) - 1, 0, -1):
            if (type(lst[ind - 1]) == str) and (lst[ind - 1] in '+-*/') and (lst[ind] == '-'):
                lst[ind + 1] *= -1
                lst = lst[:ind] + lst[ind + 1:]
    if len(lst) == 1:
        return lst[0]
    for ind in range(len(lst)):
        if type(lst[ind]) == str:
            if lst[ind] in '*/':
                if lst[ind] == '*':
                    tmp = lst[ind - 1] * lst[ind + 1]
                    return operation(lst[:ind - 1] + [tmp] + lst[ind + 2:])
                elif lst[ind] == '/':
                    tmp = lst[ind - 1] / float(lst[ind + 1])
                    return operation(lst[:ind - 1] + [tmp] + lst[ind + 2:])
            elif '*' not in lst and '/' not in lst:
                if lst[ind] in '+-':
                    if lst[ind] == '+':
                        tmp = lst[ind - 1] + lst[ind + 1]
                        return operation(lst[:ind - 1] + [tmp] + lst[ind + 2:])
                    elif lst[ind] == '-':
                        tmp = lst[ind - 1] - lst[ind + 1]
                        return operation(lst[:ind - 1] + [tmp] + lst[ind + 2:])


def app(txt):
    lst = []
    tmp = ''
    for ch in txt.strip():
        if not ch.isdigit():
            if tmp != '':
                lst.append(int(tmp))
                tmp = ''
            lst.append(ch)
        else:
            tmp += ch
    if tmp != '':
        lst.append(int(tmp))
    return operation(lst)


print(app('(-11+(-7))*4-4/(2+3)'))
print(app('11/7/3'))
print(app('-11/7/3'))
print(app('7*-1'))
print(app('-11+7*4-4/-2+3*10'))
print(app('-7*-1'))
