from datetime import datetime as dt, timedelta
from AddressBook import AddressBook

def get_upcoming_birthdays(users: AddressBook) -> list:
    upcoming_birthdays = []
    today = dt.today().date()
    
    for user in users.values():
        bd_date = user.birthday.value.strftime("%d.%m.%Y")
        birthday_this_year = (dt.strptime(bd_date, "%d.%m.%Y")).date().replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  

        if (birthday_this_year - today).days < 7:
            if birthday_this_year.weekday() < 5:  # weekday
                upcoming_birthday = {
                    "name": user.name.value,
                    "congratulation_date": dt.strftime(birthday_this_year, '%d.%m.%Y')
                }
            elif birthday_this_year.weekday() == 5:  # Saturday
                upcoming_birthday = {
                    "name": user["name"],
                    "congratulation_date": dt.strftime(birthday_this_year + timedelta(days=2), '%y.%m.%d')
                }   
            else:  # Sunday
                upcoming_birthday = {
                    "name": user["name"],
                    "congratulation_date": dt.strftime(birthday_this_year + timedelta(days=1), '%y.%m.%d')
                }
        else: 
            continue

        upcoming_birthdays.append(upcoming_birthday)

    return upcoming_birthdays

