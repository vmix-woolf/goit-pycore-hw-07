from decorations import input_error
from AddressBook import AddressBook
from Record import Record
from Phone import Phone
from Exceptions import ExactDigitException, NoSuchPhoneNumberError, ContactInBookError
import constants

@input_error
def add_contact(args, book: AddressBook):
    name, phone_number, *_ = args
    record = book.find(name)
    
    try:
        if record is None:  # if such name is new
            if Phone.validation_phone(phone_number):
                record = Record(name)
                book.add_record(record)
                record.add_phone(phone_number)
                message = constants.CONTACT_ADDED
            else:
                raise ExactDigitException()
        else :  # continue if such name is already kept
            raise ContactInBookError()
    except ExactDigitException:
        return constants.DIGITS_ERROR
    except ContactInBookError:
        return constants.CONTACT_IS_IN_BOOK
    
        
    return message


@input_error
def change_contact(args, book):
    name, old_phone_number, new_phone_number, *_ = args
    record = book.find(name)
    
    if record is None:
        raise IndexError

    try:
        if record.find_phone(old_phone_number):
            if Phone.validation_phone(new_phone_number):
                record.edit_phone(old_phone_number, new_phone_number)
            else:
                raise ExactDigitException()
        else:
            raise NoSuchPhoneNumberError()
    except NoSuchPhoneNumberError:
        return constants.NO_PHONE_NUMBER
    except ContactInBookError:
        return constants.CONTACT_IS_IN_BOOK
    except ExactDigitException:
        return constants.DIGITS_ERROR
    
    return constants.CONTACT_UPDATED


@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    
    if record.name.value != name:
        raise IndexError
    
    return f"{record.name.value} has the following phone number: {record.phones}."


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
        print(constants.CONTACT_LIST_EMPTY)
    else:
        for _, item in book.items():
            if item:
                print(f"{item}")
