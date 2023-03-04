# задача с монетами
N_coin=int(input('введите число монет'))
sum=0
import random
for i in range(N_coin):
    coin=random.randint(0,1)
    sum+=coin
    print (f' {coin}')
if sum >N_coin-sum:
    print (f' нужно перевернуть {N_coin-sum} монет')
else:
    print (f' нужно перевернуть {sum} монет')