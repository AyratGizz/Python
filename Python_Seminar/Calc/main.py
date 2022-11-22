from tkinter import *

from customtkinter import *

set_appearance_mode("dark")  # "System" (standard), "Dark", "Light"
set_default_color_theme("dark-blue")  # "blue" (standard), "green", "dark-blue"
# Создание рабочего окна
window = CTk()
window.title('Айрат')
window.geometry('239x265+1200+600')
# Создание поля ввода/вывода данных
frame_1 = CTkFrame(master=window)
frame_1.pack(pady=13, padx=13, fill="both", expand=True)
entry = CTkEntry(master=frame_1, width=210, placeholder_text="0", justify=RIGHT)
entry.pack(pady=13, padx=13)
entry.place(x=1, y=1)


# Функция вывода данных в поле ввода/вывода
def input_into_entry(symbol):
    entry.insert(END, symbol)


# Функция очистки поля ввода/вывода данных
def clear():
    entry.delete(0, END)


# Функции арифметических операций
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


# Функция, которая принимает на вход введенное выражение и далее вызывает функцию вычисления
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


# Функция для вызова функции app и вывода полученного решения в поле ввода/вывода
def count_result():
    txt = entry.get()
    result = app(txt)
    clear()
    entry.insert(0, result)


# Создание кнопок
btn1 = Button(window, font=('', '14'), bg='#008B8B', fg='white',
              text='(', command=lambda: input_into_entry('('))
btn1.place(x=10, y=70, width=70, height=50)

btn_clear = Button(window, font=('', '14'), bg='#008B8B', fg='white',
                   text=')', command=lambda: input_into_entry(')'))
btn_clear.place(x=80, y=70, width=70, height=50)

btn_clear_2 = Button(window, font=('', '14'), bg='#008B8B', fg='white', text='CE', command=clear)
btn_clear_2.place(x=150, y=70, width=70, height=50)

btn4 = Button(window, font=('', '25'), bg='#008B8B', fg='white',
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

btn8 = Button(window, font=('', '25'), bg='#008B8B', fg='white',
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

btn12 = Button(window, font=('', '25'), bg='#008B8B', fg='white',
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

btn16 = Button(window, font=('', '22'), bg='#008B8B', fg='white',
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

btn_result = Button(window, font=('', '30'), bg='#DC143C', fg='white', text='=', command=count_result)
btn_result.place(x=220, y=270, width=70, height=50)
window.mainloop()  # Для бесконечной работы программы
