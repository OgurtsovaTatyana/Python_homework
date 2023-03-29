# Телефонный справочник
# меню:
#     Открыть
#     сохранить
#     показать контакты
#     найти
#     добавить
#     удалить
#     выход
# Формат:
#     №, ФИО, номер, комментарий

ph_action=0 # вводимый номер меню
phone_dir=list()
name_phone=list() # список с фамилиями
path='telephone.txt'

dict_action={1: "Обновить", 
             2: "Сохранить",
             3: "Показать контакты",
             4: "Найти",
             5: "Добавить",
             6: "Удалить",
             7: "Выход"
             }

#подготовительная работа с файлом
#def update_phone_dir(): #открытие и чтение файла
with open(path,'r',encoding='UTF-8') as file:
    phone_dir=file.readlines()
    for item in phone_dir:
        name_phone.append(item.split(' ')[0])

#update_phone_dir()

#функции пунктов меню    
def p3_print_dir():#показать контакты
    print('Список контактов:')
    print(phone_dir)
    for item in phone_dir:
        print(item,end="")
    print('\n')
   
        
def p4_search(): #найти контакты
    input_name=input('Введите Фамилию:')
    if input_name in name_phone:  
        print('Такая фамилия есть:') 
        print(phone_dir[name_phone.index(input_name)])
    else:
        print('Такого контакта нет в словаре')
           
def p5_add_phone_dir(): #добавить контакт
    with open(path,'a',encoding='UTF-8') as file:
        new_contact=input('введите Фамилию, Имя,  номер телефона, комментарий ')
        file.write(f'{new_contact}\n')  
        phone_dir.append(f'{new_contact}\n')
        phone_dir.sort()
        
def p6_del_phone_dir(): #удалить контакт
    with open(path,'w',encoding='UTF-8') as file:
        input_name=input('введите Фамилию,контакта тоторый хотите удалить ')
        if input_name in name_phone:
            contact= phone_dir[name_phone.index(input_name)] 
            del_contact=input(f'Подтвердите удаление контакта {contact}: д ')
            if del_contact=='д':
                phone_dir.pop(name_phone.index(input_name))
                print(phone_dir)
                print(f' контакт {input_name} удален')
                file.write(''.join(str(x) for x in phone_dir))  
            else:
                print(f'контакт {input_name} не удален')
                print(phone_dir)
        else:print(f'такого контакта нет в справочнике')
        
       
        
# запуск работы меню        
def menu(): #вывод меню, ожидание ввода
    print(f"Работа с телефонным справочником: ") 
    for key in dict_action:
        print(f'{key} {dict_action[key]}')
    return input('Введите номер меню ')

while ph_action!='7':
    ph_action=menu()
    if ph_action=='1': print('пока не работает')#update_phone_dir()
    elif ph_action=='3': p3_print_dir()  #показать контакты
    elif ph_action=='4': p4_search()  #найти контакты
    elif ph_action=='5': p5_add_phone_dir() #добавить контакт
    elif ph_action=='6': p6_del_phone_dir() #удалить контакт
    elif ph_action=='7':
        print('До встречи!')
        break
    else:
        print('\n Такого номера нет в меню, введите заново \n')
    if 0< int(ph_action) <7:
        prod=input('Для выхода нажмите q ')
        if prod=='q':
            break
        else:
            print('\n')
   


