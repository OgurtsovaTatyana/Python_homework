# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
set_n=set()
set_m=set()
n=int(input('введите количество элементов первого множества '))
for i in range(0,n):
    set_n.add(int(input(f'введите {i+1}-й элемент первого множества ')))
m= int(input('введите количество элементов второго множества '))
for i in range(0,m):
    set_m.add(int(input(f'введите {i+1}-й элемент второго множества ')))
# set_n={2,5,7,1,3,4}
# set_m={3,5,1,6}
print(set_n)
print(set_m)
print(set_n.intersection(set_m))

