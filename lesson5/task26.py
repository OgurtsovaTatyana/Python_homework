number=int(input('введите число '))
step=int(input('введите степень '))
def pow(a,b):
    if b==0 :
        return 1
    else:
        return a*pow(a,b-1)
print(pow(number,step))