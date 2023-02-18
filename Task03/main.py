'''
Счастливым билетом называют такой билет с шестизначным номером,
 где сумма первых трех цифр равна сумме последних трех. 
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
 Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no'''
print('Ведите шестизначное число: ')
happy_number = (input())
first_digit = int(happy_number[0])
second_digit = int(happy_number[1])
third_digit = int(happy_number[2])
fourth_digit = int(happy_number[3])
fifth_digit = int(happy_number[4])
sixth_digit = int(happy_number[5])
if (first_digit + second_digit + third_digit == fourth_digit + fifth_digit + sixth_digit):
    print('Yes, this is a happy ticket')
else:
    print('No, this ticket isn\'t happy')