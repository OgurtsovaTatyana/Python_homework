N_str=(input('введите 6-ти значное число:  '))
sum_left=int(N_str[0])+int(N_str[1])+int(N_str[2])
sum_right=int(N_str[3])+int(N_str[4])+int(N_str[5])
if sum_left==sum_right:
    print (f'билет счастливый: сумма чисел {N_str[:3]} равна сумме чисел {N_str[3:]}')
else:
    print (f'билет несчастливый')