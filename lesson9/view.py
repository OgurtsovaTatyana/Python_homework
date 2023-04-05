import text_fields

def main_menu() ->int:
    print(text_fields.main_menu)
    length_menu=len(text_fields.main_menu.split('\n'))
    while True:
        choice=input('Выберите пункт меню:')
        if choice.isdigit() and 0<int(choice)<=length_menu:
            return int(choice)
        else:
            print(f'Введите Число от 1 до {length_menu}')

def show_contacts(book:list, error_message:str):
    if not book:
        print(error_message)
        return False
    else:
        for i,contact in enumerate(book,1):
            print(f'{i}.{contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20}')
        return True
def add_contact() ->dict:
    name=input('Введите Фамилию и Имя: ')
    phone=input('Введите номер телефона: ') 
    comment=input('Введите комментарий: ')
    return {'name':name,'phone': phone,'comment':comment} 

def input_index(message:str):
    return int(input(message))

def input_search(message):
    return input(message)

def change_contact(book:list,index:int):
    print('Введите новые данные или оставьте поле пустым, если изменений нет')
    contact=add_contact()
    return {'name':contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone':contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment':contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}
    
def del_contact(book:list,index:int)->bool:
    prov=input(f'''Вы уверены, что хотите удалить контакт:
          {book[index-1].get("name")}  {book[index-1].get("phone")}  {book[index-1].get("comment")} ?
           для подтверждения введите д 
           для выхода в меню введите любой друго символ 
           ''')
    return prov=='д'

def show_message(message:str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))