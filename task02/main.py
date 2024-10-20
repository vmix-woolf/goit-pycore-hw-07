from handler import (
    add_contact, 
    change_contact, 
    show_phone, 
    show_all,
    add_birthday,
    show_birthday,
    birthdays
)
from parser import parse_input
from AddressBook import AddressBook
from Exceptions import ExactDigitException


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                print(add_contact(args, book))
            except ExactDigitException:
                # print(f'Phone should consist of exactly 3 digits!')
                continue
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            add_birthday(args, book)
        elif command == "show-birthday":
            show_birthday(args, book)
        elif command == "birthdays":
            birthdays(args, book)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
