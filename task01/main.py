from AddressBook import AddressBook
from Record import Record
from upcoming_birthdays import get_upcoming_birthdays


if __name__ == "__main__":
    # check functionality
    # create new address book
    book = AddressBook()

    # create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("23.10.2000")

    # add John's record to the Address book
    book.add_record(john_record)

    # create new record for Jane and add it to Address book
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("24.10.1980")
    book.add_record(jane_record)

    # display all the records in the Address book
    for name, record in book.data.items():
        print(record)

    # Searching and updating phone number for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

    # Search specific phone number for John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Output: 5555555555

    # Delete phone number for John
    john.remove_phone("5555555555")

    # Delete record for Jane
    book.delete("Jane")

    # Implement function from the previous tasks
    upcoming_birthdays = get_upcoming_birthdays(book)
    print("This week's congratulations list:", upcoming_birthdays)
