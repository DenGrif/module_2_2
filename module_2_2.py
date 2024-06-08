# В этом примере, если все три числа равны, программа выводит 3,
# если есть два одинаковых числа, программа выводит 2,
# в противном случае программа выводит 0.

first = int(input('Ввести целое число '))
second = int(input('Ввести целое число '))
third = int(input('Ввести целое число '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)