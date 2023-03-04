number=int(input('введите 3-х значное число:  '))
one_ch=(number//100)%10
two_ch=(number//10)%10
tree_ch=number%10
print (f'первая цифра: {one_ch} вторая цифра: {two_ch} третья цифра: {tree_ch}')