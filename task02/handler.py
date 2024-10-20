from decorations import input_error
from AddressBook import AddressBook
from Record import Record
from Exceptions import ExactDigitException

@input_error
def add_contact(args, book):
    name, phone_number, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    
    if phone_number:
        try:
            record.add_phone(phone_number)
            return message
        except ExactDigitException:
            AddressBook.delete(name)
            return f'Phone should consist of exactly 3 digits!'
            


@input_error
def change_contact(args, book):
    name, old_phone_number, new_phone_number, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        raise IndexError
    if new_phone_number:
        book[name] = new_phone_number

    return message


@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    
    if record.name.value != name:
        raise IndexError
    
    return f"{record} has the following phone number: {book[name]}."


@input_error
def add_birthday(args, book):
    pass

@input_error
def show_birthday(args, book):
    pass

@input_error
def birthdays(args, book):
    pass

@input_error
def show_all(book):
    if len(book) == 0:
        return f"Contact list is empty"
    else:
        for _, item in book.items():
            if item:
                return f"{item}"
