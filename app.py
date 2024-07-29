from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    IS_REQUIRED = True
    
    def __init__(self, value):
         if self.IS_REQUIRED and (value is None or value == ''):
             raise ValueError('Field Name is required');
         
         super().__init__(value);
              

class Phone(Field):
    IS_REQUIRED = True;
    REQURIED_LENGTH = 10;

    def __init__(self, value):
            if self.IS_REQUIRED and (value is None or value == ''):
                raise ValueError('Field Phone is required');
            
            if len(value) != self.REQURIED_LENGTH:
                raise ValueError(f'Field Phone must contain exactly {self.REQURIED_LENGTH} numbers');
            
            super().__init__(value);
         

class Record:
    def __init__(self, name):
        self.name = Name(name);
        self.phones = [];

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}";
    
    def add_phone(self, phone):
           self.phones.append(Phone(phone));
    
    def remove_phone(self, phone):
           self.phones.remove(phone);

    def find_phone(self, phone):
           if phone in self.phones:
                return phone;

    def edit_phone(self, phone, new_phone):
          if phone in self.phones:
              self.phones[self.phones.index(phone)] = new_phone;



class AddressBook(UserDict):
       def add_record(self, record):
              self.data[record.name.value] = record;
              
       def find(self, name: str):
         return self.data[name];

       def delete(self, name: str):
            self.data.pop(name);

# Створення нової адресної книги
book = AddressBook();

# Створення запису для John
john_record = Record("John");
john_record.add_phone("1234567890");
john_record.add_phone("5555555555");

# Додавання запису John до адресної книги
book.add_record(john_record);

# Створення та додавання нового запису для Jane
jane_record = Record("Jane");
jane_record.add_phone("9876543210");
book.add_record(jane_record);

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record);

# Знаходження та редагування телефону для John
john = book.find("John");
john.edit_phone("1234567890", "1112223333");

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555");
print(f"{john.name}: {found_phone}");  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane");
