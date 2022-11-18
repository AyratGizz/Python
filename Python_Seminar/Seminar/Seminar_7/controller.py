from model_mult import *
from log import *
from Python_Seminar.Seminar.Seminar_8 import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_operand = view.operacia()
    if value_operand == '/':
        result = div(value_a, value_b)
    elif value_operand == '*':
        result = mult(value_a, value_b)
    elif value_operand == '+':
        result = summ(value_a, value_b)
    elif value_operand == '-':
        result = subtr(value_a, value_b)
    else:
        result = 'Такой операции не существует!'

    view.view_data(result, "Результат: ")
    save_log()
