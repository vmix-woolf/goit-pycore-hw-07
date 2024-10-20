from decorations import input_error
from AddressBook import AddressBook
from Record import Record
from Phone import Phone
from Exceptions import ExactDigitException

@input_error
def add_contact(args, book):
    name, phone_number, *_ = args
    record = book.find(name)
    # if such name is kept
    message = "Contact updated."
    
    # if such name is new
    if record is None:
        try:
            if Phone.validation_phone(phone_number):
                record = Record(name)
                book.add_record(record)
                record.add_phone(phone_number)
                message = "Contact added."
            else:
                raise ExactDigitException()
        except ExactDigitException:
            return f'Phone should consist of exactly 3 digits!'
    else : #  continue if such name is already kept
        if phone_number:
            book.add_record(record)
            record.add_phone(phone_number)
        else:
            raise ValueError
        
    return message

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
                print(f"{item}")
