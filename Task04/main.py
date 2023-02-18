'''
Требуется определить, 
можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками 
   (то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no'''
print("Введите длину шоколадки: ")
choc_length = int(input())
print("Введите ширину шоколадки: ")
choc_width =  int(input())
print(F'Размер шоколадки {choc_length} х {choc_width} долек')
print("Сколько хотите долек?")
choc_piece =int(input())
if (choc_piece%choc_length ==0 or choc_piece%choc_width==0):
    print('Yes, you can get it')
else:
    print('No, sorry')