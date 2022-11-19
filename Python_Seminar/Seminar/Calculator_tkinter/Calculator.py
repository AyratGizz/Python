from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"
# Создание рабочего окна
window = customtkinter.CTk()
window.title('Калькулятор от Айрата')
window.geometry('239x265+1000+300')

# Создание поля ввода/вывода данных
frame_1 = customtkinter.CTkFrame(master=window)
frame_1.pack(pady=13, padx=13, fill="both", expand=True)
entry = customtkinter.CTkEntry(master=frame_1, width=210, placeholder_text="")
entry.pack(pady=13, padx=13)
entry.place(x=1, y=1)


# entry = Entry(window, width=15, bg='black', fg='white', font=('', '20'))
# entry.place(x=13, y=60)
# Функция вывода данных в поле ввода/вывода
def input_into_entry(symbol):
    entry.insert(END, symbol)


# Функция очистки поля ввода/вывода данных
def clear():
    entry.delete(0, END)


# -----------------------------------------------------------------------------------
# Функции арифметических операций
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
    try:
        res = lst[0]
        for i in lst[1:]:
            res /= i
        return res
    except ZeroDivisionError:
        return "Нельзя делить на '0'"


# -------------------------------------------------------------------------------------
# Функция, которая принимает на вход текст, разбивает его по алгебраическим действиям и
# вызывает арифметические функции по приоритету
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
        return int(txt)
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


# -------------------------------------------------------------------------
# Функция для вызова функции app и вывода полученного решения в поле ввода/вывода
def count_result():
    txt = entry.get()
    result = app(txt)
    clear()
    entry.insert(0, result)


# ---------------------------------------------------------------------------
# Создание кнопок
btn1 = Button(window, font=('', '14'), bg='black', fg='white',
              text='(', command=lambda: input_into_entry('('))
btn1.place(x=10, y=70, width=70, height=50)

btn_clear = Button(window, font=('', '14'), bg='black', fg='white',
                   text=')', command=lambda: input_into_entry(')'))
btn_clear.place(x=80, y=70, width=70, height=50)

btn_clear_2 = Button(window, font=('', '14'), bg='black', fg='white', text='CE', command=clear)
btn_clear_2.place(x=150, y=70, width=70, height=50)

btn4 = Button(window, font=('', '25'), bg='black', fg='white',
              text='/', command=lambda: input_into_entry('/'))
btn4.place(x=220, y=70, width=70, height=50)

btn5 = Button(window, font=('', '16'), bg='black', fg='white',
              text='7', command=lambda: input_into_entry('7'))
btn5.place(x=10, y=120, width=70, height=50)

btn6 = Button(window, font=('', '16'), bg='black', fg='white',
              text='8', command=lambda: input_into_entry('8'))
btn6.place(x=80, y=120, width=70, height=50)

btn7 = Button(window, font=('', '16'), bg='black', fg='white',
              text='9', command=lambda: input_into_entry('9'))
btn7.place(x=150, y=120, width=70, height=50)

btn8 = Button(window, font=('', '25'), bg='black', fg='white',
              text='*', command=lambda: input_into_entry('*'))
btn8.place(x=220, y=120, width=70, height=50)

btn9 = Button(window, font=('', '16'), bg='black', fg='white',
              text='4', command=lambda: input_into_entry('4'))
btn9.place(x=10, y=170, width=70, height=50)

btn10 = Button(window, font=('', '16'), bg='black', fg='white',
               text='5', command=lambda: input_into_entry('5'))
btn10.place(x=80, y=170, width=70, height=50)

btn11 = Button(window, font=('', '16'), bg='black', fg='white',
               text='6', command=lambda: input_into_entry('6'))
btn11.place(x=150, y=170, width=70, height=50)

btn12 = Button(window, font=('', '25'), bg='black', fg='white',
               text='-', command=lambda: input_into_entry('-'))
btn12.place(x=220, y=170, width=70, height=50)

btn13 = Button(window, font=('', '16'), bg='black', fg='white',
               text='1', command=lambda: input_into_entry('1'))
btn13.place(x=10, y=220, width=70, height=50)

btn14 = Button(window, font=('', '16'), bg='black', fg='white',
               text='2', command=lambda: input_into_entry('2'))
btn14.place(x=80, y=220, width=70, height=50)

btn15 = Button(window, font=('', '16'), bg='black', fg='white',
               text='3', command=lambda: input_into_entry('3'))
btn15.place(x=150, y=220, width=70, height=50)

btn16 = Button(window, font=('', '22'), bg='black', fg='white',
               text='+', command=lambda: input_into_entry('+'))
btn16.place(x=220, y=220, width=70, height=50)
#
btn13 = Button(window, font=('', '16'), bg='black', fg='white',
               text='+/-', command=lambda: input_into_entry('-'))
btn13.place(x=10, y=270, width=70, height=50)

btn14 = Button(window, font=('', '16'), bg='black', fg='white',
               text='0', command=lambda: input_into_entry('0'))
btn14.place(x=80, y=270, width=70, height=50)

btn15 = Button(window, font=('', '16'), bg='black', fg='white',
               text='.', command=lambda: input_into_entry('.'))
btn15.place(x=150, y=270, width=70, height=50)

btn_result = Button(window, font=('', '30'), bg='black', fg='white', text='=', command=count_result)
btn_result.place(x=220, y=270, width=70, height=50)
#
# Для бесконечной работы программы
window.mainloop()
