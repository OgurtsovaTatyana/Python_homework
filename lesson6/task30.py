#задача 30. (элементы арифметической прогресии)
num_str=input('введите 3 числа через пробел ')
list1=num_str.split()
print(list1)
for i in range(1,int(list1[2])+1):
    print(int(list1[0]) +(i-1)*int(list1[1]))