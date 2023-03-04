sum=int(input('введите сумму чисел '))
mult=int(input('введите произведение чисел '))
flag=1
i=1
while flag:
    p=i*(sum-i)
    if p==mult:
        print (f'загаданные числа {i},{sum-i}')
        flag=0
    else:
        i+=1
        