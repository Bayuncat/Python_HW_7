import db_rw
import Controller

# Чтение контактов из базы
db_rw.readDB()

# Основное меню
choice=0
while True:
    print('Добро пожаловать в основное меню справочника телефонов.\n'
    'Варианты работы со справочником:\n'
    '1 - вывод всего справочника. '
    '2 - добавляем контакт. '
    '3 - ищем совпадения по любому полу.\n'
    '4 - удаляем контаткт по id. '
    '5 - сохранить изменения в базу и выйти')
    try:
        choice = int(input(f'Ваш выбор: '))
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")
    else:
        if (choice < 1) or (choice > 5):
            print("Здесь нет такой операции.")

# Вывод всего списка контактов
    if choice == 1:
        Controller.Print()

# Добавление нового контакта
    if choice == 2:
        name = str(input(f'Введите имя: '))
        surname = str(input(f'Введите фамилию: '))
        phone = str(input(f'Введите телефон: '))
        Controller.Add(name, surname, phone)  

# Поиск контакта
    if choice == 3:
        anyfield = str(input(f'Введите имя, фамилию или телефон для поиска: '))
        Controller.search(anyfield)

# Удаление контакт
    if choice == 4:
        id = int(input(f'Введите номер контакта для удаления из списка: '))
        Controller.Erase(id)  

# Выход и запись изменений
    if choice == 5:
        db_rw.writer()
        break