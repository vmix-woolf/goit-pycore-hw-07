from handler import (
    add_contact, 
    change_contact, 
    show_phone, 
    show_all,
    add_birthday,
    show_birthday,
    birthdays
)
import constants
from parser import parse_input
from AddressBook import AddressBook


def main():
    book = AddressBook()
    print(f"{constants.WELCOME_MESSAGE}")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            show_all(book)
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            birthdays(book)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
