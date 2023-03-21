# Задачи из семинара
# задача1
# import random
# n= int(input('введите длину первого списка '))
# m= int(input('введите длину второго списка '))

# list1=[random.randint(1,20) for i in range(n)]
# list2=[random.randint(1,20) for i in range(m)]
# print (list1)
# print (list2)
# for item in list1:
#     if item not in list2:
#         print(item,end=',')

#    задача2 (про тройки чисел)
# import random
# n= int(input('введите длину списка '))
# list1=[random.randint(1,20) for i in range(n)]
# print(list1)
# count=0
# for i in range(-1,n-1):
#     print(list1[i-1],list1[i],list1[i+1]) #вывожу тройки посмотреть
#     if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
#         count+=1
# print('количество элементов=',count)

 #  задача3 (количество пар чисел в списке )
# import random
# n= int(input('введите длину списка '))
# list1=[random.randint(1,10) for i in range(n)]
# print(list1)
# def para(my_list):
#     count=0
#     di=dict()
#     for i in my_list:
#         pars=my_list.count(i)//2
#         di.setdefault(i,pars)  
#     for item in di.values():
#         count=count+item
#     return count
# print(para(list1))

 #  задача4 (про дружественные числа)
k= int(input('введите число '))
def sum_del(num): # находит сумму всех делителей числа
    sum=0
    for i in range(2,num+1):
       if num%i==0:
           sum= sum+num//i
    return sum

dic_sum=dict()  # заполняем словарь числами и сумамми их делителей
for j in range (1,k):
    dic_sum[j]= sum_del(j)

for i in range (1,k): # находим сами числа
    for j in range(i+1,k-1):
        if dic_sum[i]==j and dic_sum[j]==i:
            print(i,j)
     