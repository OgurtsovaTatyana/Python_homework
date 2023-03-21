number1=int(input('введите первое число '))
number2=int(input('введите второе число '))
def sum(a,b):
    
    if b==0 :
        return a
    else:
        return 1+sum(a,b-1)

print('сумма чисел равна',sum(number1,number2))