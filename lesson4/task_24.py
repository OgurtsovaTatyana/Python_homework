import random
n=int(input('введите количество кустов '))
my_list=[random.randint(1,10) for i in range (0,n)]
print(my_list)
max_sum=0
for i in range(-1, len(my_list)-1):
    sum= my_list[i-1]+ my_list[i]+my_list[i+1]
    print (sum)
    if sum>max_sum:
        max_sum=sum
print ('максиматьное мисло ягоды',max_sum)