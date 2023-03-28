# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6)
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
# у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
num_rows=int(input('введите количество строк '))
num_columns=int(input('введите количество столбцов '))

def print_operation_table(operation, num_col=6, num_row=6):
    data_table=[]
    i=0
    for row in range(0,num_row):
        for column in range(0,num_col):
            data_table.append(operation(row+1,column+1))
            print(data_table[i],end=' ')
            i=i+1
        print( end='\n')
print_operation_table(lambda x, y: x * y,num_rows,num_columns)
