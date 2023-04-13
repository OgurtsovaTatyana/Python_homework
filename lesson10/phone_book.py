class Contact:
    def __init__(self,name:str,phone:int,comment:str):
        self.name=name
        self.phone=phone
        self.comment=comment
    def __str__(self): #печать при использовании print(контакт)
        return f'{self.name:<20} | {self.phone:<20} | {self.comment:<20}'    


class PhoneBook:
    def __init__(self,path:str):
        self.path=path
        self.phone_list=[]
        self.open()
    def __str__(self): #печать при использовании print(книга)
        result=''
        for i,contact  in enumerate(self.phone_list,1):
            result+=(f'{i}.{contact} \n')
        return result   
    
    
    def open(self):
        self.phone_list=[]
        with open(self.path,'r',encoding='UTF-8') as file:
            data=file.readlines() 
        for item in data:
            new_contact=item.strip().split(';')
            self.phone_list.append(Contact(new_contact[0],new_contact[1],new_contact[2]))
                                             
    def save(self):
        data=[]
        with open(self.path,'w',encoding='UTF-8') as file:   
            for cont in self.phone_list:
                    line=f'{cont.name};{cont.phone};{cont.comment}'
                    data.append(line)
                    text='\n'.join(data)
            file.write(text)

    def search(self,search_name:str): #     2. Найти контакт
        result=''
        for contact in self.phone_list:
            str_cont=f'{contact.name} {contact.phone} {contact.comment}' 
            if search_name.lower() in str_cont.lower() :
                result+=(f'{contact} \n')
        if result :
            print(result)
        else:
            print('Такой котнакт не найден')
    def add_cont(self,new_name:str,new_phone:int,new_comment:str):
         self.phone_list.append(Contact(new_name,new_phone,new_comment)) 
    def change_cont(self,index:int,new_name:str,new_phone:int,new_comment:str):
        print (f' Контакт: \n {self.phone_list[index]} \n Изменен: ') 
        if new_name:
            self.phone_list[index].name=new_name
        if new_phone:    
            self.phone_list[index].phone=new_phone
        if new_comment:
            self.phone_list[index].comment=new_comment
        print (f'  {self.phone_list[index]} ')   
    def del_cont(self,index:int):
        print(f'{self.phone_list[index]} удален')
        self.phone_list.pop(index)
    