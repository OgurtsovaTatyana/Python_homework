#задача 32. (принадлежность чисел диапазону)
n=int(input('введите размер списка '))
num_str=input('диапазон: два числа через пробел ')
import random
list1=[random.randint(1,10) for i in range(n)]
print(list1)
list2=num_str.split()
print(list2)
for i in range(0,n):
    if int(list2[0])<list1[i]<int(list2[1]):
        print('элемент ',list1[i], ' индекс=',i )
    