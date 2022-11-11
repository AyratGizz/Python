# x = 0
# y = 0

# def init(a, b):
#     global x
#     global y
#     x = a
#     y = b

def div(x, y):
    try: 
        return x / y
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

def mult(x, y):
    return x * y

def summ(x, y):
    return x + y

def subtr(x, y):
    return x - y



