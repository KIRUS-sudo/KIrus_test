import time # импортировали время
from datetime import datetime # из дат (datetime) импортировали некоторые даты (datetime)
from random import randint # из любых (random) чисел импортировали случайные целые числа (randint)
                           # для удобства
odds = [] # чётные числа равны списку 
                           # для удобства
for i in range (60) : # постоянное действие(цикл (for)): переменная i вольируется (in range) от 0 до 100
    if i % 2 == 0: # если остаток от частного (%) i на 2 равен ( (==), т. к. арифметическое действие ) 0
        odds.append(i) # значение evens будет равна значениям i по списку (отсылка на 5-ую строку)
        # для удобства
print(oddsC) # напечатать значения чётных чисел (evens)

while True:
    right_this_second = datetime.today().second
    if right_this_second in odds:
        print(datetime.today().strftime('%H:%M:%S'), 'это нечётная секунда.')
    else:
        print(datetime.today().strftime('%H:%M:%S'), 'это чётная секунда.')
    wait_time = randint(1, 5)
    time.sleep(wait_time)
break