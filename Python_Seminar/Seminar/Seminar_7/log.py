from datetime import datetime as dt

def save_log(*args):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'w', encoding='utf-8') as file:
        file.write(f'{value_a} {operacia} {value_b} = {result}: Time {time}\n') 
                            