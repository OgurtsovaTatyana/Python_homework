num=int(input('введите число до которого нужно вывести все степени 2 '))
i=0
deg=0
while deg<num:
    if i==0 :
        deg=1
    else: 
        deg*=2
    if deg<num:
        print (f'{i}-я степень 2-х = {deg}')
    i+=1
    
        