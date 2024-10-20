from Name import Name
from Phone import Phone
from Birthday import Birthday
from Exceptions import ExactDigitException

class Record:
    def __init__(self, record_name):
        self.name = Name(record_name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone):
        if Phone.validation_phone(phone):
            self.phones.append(phone)
        else:
            raise ExactDigitException()


    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)


    def edit_phone(self, old_phone, new_phone):
        try:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        except ValueError:
            return f"No a such phone"
            
    
    def find_phone(self, phone):
        try:
            index = self.phones.index(phone)
            return self.phones[index]
        except ValueError:
            return False
    
    def add_birthday(self, date_of_birth):
        self.birthday = Birthday(date_of_birth)


    def __str__(self):
        if self.birthday is not None:
            return f"Contact name: {self.name.value}, " + \
                f"phones: {'; '.join(p for p in self.phones)}, " + \
                f"birthday: {self.birthday.value.date()}" 
        else: 
            return f"Contact name: {self.name.value}, " + \
                f"phones: {'; '.join(p for p in self.phones)}"
