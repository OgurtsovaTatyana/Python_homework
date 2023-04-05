import model
import view

def start():
    while True:
        pb=model.get_phone_book()
        choice=view.main_menu()
        # match choice: #не работает в версии 3.8 
        #     case 1:
        #         model.open_file()
        #         view.show_message('Файл открыт')
        #     case 2:
        #         model.save_file()
        #         view.show_message('Файл сохранен') 
        #     case 3:
        #         view.show_contacts(pb,'Телефоннаякнига пуста или не открыта')
        #     case 4:
        #         model.add_contact(view.add_contact())
        #     case 5:
        #         if view.show_contacts(pb,'Телефоннаякнига пуста или не открыта'):
        #             index=view.input_index('Введите номер изменяемого контакта')
        #             contact=view.change_contact(pb,index)
        #             view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен!')     
        #     case 6:
        #         search=view.input_search('Введите искомый элемент')
        #         result=model.find_contact(search)
        #         view.show_contacts(result,'Контакты не найдены')
        #     case 7: 
        #         return 
                      
        if choice ==1:
            model.open_file()
            view.show_message('Файл открыт')
        elif choice ==2:  
            model.save_file()
            view.show_message('Файл сохранен') 
        elif choice ==3:
            view.show_contacts(pb,'Телефоннаякнига пуста или не открыта')
        elif choice ==4:
            model.add_contact(view.add_contact())
        elif choice ==5:
            if view.show_contacts(pb,'Телефоннаякнига пуста или не открыта'):
                index=view.input_index('Введите номер изменяемого контакта')
                contact=view.change_contact(pb,index)
                view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен!')     
        elif choice ==6:
            search=view.input_search('Введите искомый элемент ')
            result=model.find_contact(search)
            view.show_contacts(result,'Контакт не найден')
        elif choice ==7:
            if view.show_contacts(pb,'Телефоннаякнига пуста или не открыта'):
                index=view.input_index('Введите номер удаляемго контакта')
                result=view.del_contact(pb,index)
                if result:
                    view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} удален!') 
                    model.del_contact(index)
                     
        elif choice ==8:
            return  