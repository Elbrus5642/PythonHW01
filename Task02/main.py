'''
Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, 
если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10'''
print("Введите сколько журавликов сделали дети из ряда чисел 6, 12, 18, 24, 30 ... : ")
bird_total =  int(input())
bird_Pet = bird_total//6
bird_Serg = bird_total//6
bird_Kat =  bird_total//6*4
print(f'{bird_total} -> {bird_Pet}  {bird_Kat}  {bird_Serg}')  

    