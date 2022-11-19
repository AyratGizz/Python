## Задача 1
def add(lst):
    return sum(lst)


def diff(lst):
    res = lst[0]
    for i in lst[1:]:
        res -= i
    return res


def mult(lst):
    res = lst[0]
    for i in lst[1:]:
        res *= i
    return res


def delim(lst):
    res = lst[0]
    for i in lst[1:]:
        res /= i
    return res


def app(txt):
    if '(' in txt:
        start = 0
        for i in range(len(txt)):
            if txt[i] == '(':
                start = i
        fin = start + txt[start:].index(')')
        tmp = txt[start + 1:fin]
        result = app(tmp)
        return app(f'{txt[:start]}{result}{txt[fin + 1:]}')
    sign = ''
    for s in '+-*/':
        if s in txt:
            sign = s
            break
    if sign == '':
        return float(txt)
    else:
        lst = list(map(app, txt.split(sign)))
        if sign == '*':
            return mult(lst)
        elif sign == '/':
            return delim(lst)
        elif sign == '+':
            return add(lst)
        elif sign == '-':
            return diff(lst)


print(app('11+7*4-4/2+3*10'))
print(app('11+7+3'))

## Задача 2
