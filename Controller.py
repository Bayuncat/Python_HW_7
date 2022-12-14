import Contacts
import db_rw

# Вывод всех контактов
def Print():
    for row in db_rw.my_list:
        print("%2d" %(db_rw.my_list.index(row) +1), end=' ')
        Contacts.Contacts.display_contacts(row)

# Удаление контакта
def Erase(id):
    print('Удален контакт:')
    Contacts.Contacts.display_contacts(db_rw.my_list[id-1])
    db_rw.my_list.pop(id-1)
    print('\n')

# Добавление контакта
def Add(name, surname, phone):
    db_rw.my_list.append(Contacts.Contacts(name, surname, phone))
    print('Добавлен контакт:')
    Contacts.Contacts.display_contacts(db_rw.my_list[-1])
    print('\n')
    
# Поиск контакта
def search(anyfield):
    j = 0
    
    for row in db_rw.my_list:
        if (anyfield == Contacts.Contacts.getName(row)) or (anyfield == Contacts.Contacts.getSurname(row)) or (anyfield == Contacts.Contacts.getPhone(row)):
            print("%2d" %(db_rw.my_list.index(row) +1), end=' ')
            Contacts.Contacts.display_contacts(row)
            j += 1
    if j == 0: print('\nТакой контакт не найден.\n')

