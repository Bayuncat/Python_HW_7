class Contacts:  
      
    def __init__(self, name, surname, phone):  
        self.name = name
        self.surname = surname
        self.phone = phone
         
    def display_contacts(self):  
        print('Имя: {}. Фамилия: {}. Телефон: {}'.format(self.name,  self.surname, self.phone))
    
    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname
    
    def getPhone(self):
        return self.phone