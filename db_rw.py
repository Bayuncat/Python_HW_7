import csv
import Contacts

my_list = []

# обращение к базе: чтение
def readDB():
    
    with open('DB.csv', 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            my_list.append(Contacts.Contacts(row[0], row[1], row[2]))

# обращение к базе: запись
def writer():
    with open('DB.csv', 'w', newline="", encoding="utf8") as f:
        write = csv.writer(f)
        for row in my_list:
            write.writerow([row.name, row.surname, row.phone])
        
      