import phone_book
import view
my_book=phone_book.PhoneBook('phone.txt')
print(my_book.phone_list)
my_book.open()

def start():
    while True:
        pb=my_book.phone_list
        choice=view.main_menu()
        
        if choice ==1:
            print('\n Tелефонный справочник: \n')
            print(my_book)
            
        elif choice ==2:  #     2. Найти контакт
            print('Введите искомый элемент ')
            search_cont=input()
            print(my_book.search(search_cont))
            
        elif choice ==3: #     3. Добавить контакт
            new_name=input('Введите Имя Фамиию ')
            new_phone=input('Введите телефон ')
            new_comment=input('Введите коментарий ')
            my_book.add_cont(new_name,new_phone,new_comment)
            
        elif choice ==4: #     4. Изменить контакт
            index=int(input('Введите порядковый номер контакта, который хотите изменить'))
            print('Заполните поле или оставьте пустым, если не нужно его изменять')
            new_name=input('Введите Имя Фамиию ')
            new_phone=input('Введите телефон ')
            new_comment=input('Введите коментарий ') 
            my_book.change_cont(index-1,new_name,new_phone,new_comment) 
        elif choice ==5: #     5. Удалить контакт
            index=int(input('Введите порядковый номер контакта, который хотите удалить '))
            my_book.del_cont(index-1)  
                  
        elif choice ==6: #     6. Сохранить файл
            my_book.save()
            print('Файл сохранен') 

        elif choice ==7: #     7.  Выход
            return  