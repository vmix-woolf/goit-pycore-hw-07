from collections import UserDict

class AddressBook(UserDict):
    current_id = 1

    def add_record(self, record_name):
        self.data[AddressBook.current_id] = record_name
        AddressBook.current_id += 1

    
    def find(self, user_name):
        for _, user in self.data.items():
            if user.name.value == user_name:
                return user

    
    def delete(self, user_name):
        {key: value for key, value in self.data.items() if value.name.value != user_name}
   