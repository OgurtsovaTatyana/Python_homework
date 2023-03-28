str='пара-ра-рам рам-пам-папам па-ра-па-дам' 
my_list=str.split()
print(my_list)

def count_glassn(word:list):# считает количество гласных в слове
    count=0
    glasn=['а','е','и','о','у','я','ю','ё']
    gl_list=[]
    gl_list=list(filter(lambda x: x in glasn,word)) 
    count=len(gl_list)
    return count


def rifma(word_list:list) ->list: # сравнивает число глассных вкаждом слове, определяет рифму
    list1=list(map(count_glassn,word_list))
    if len(set(list1))>1:
        print('Пам парам')
    else:
        print('Парам пам-пам')
rifma(my_list)
