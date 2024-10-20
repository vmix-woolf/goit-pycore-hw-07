from datetime import datetime
from Field import Field
from Exceptions import InvalidDateFormatError, InvalidDateValueError
import re

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value


    def validation_birthday(date_of_birth)-> bool:
        try:
            if bool(re.match(r'\d{2}\.\d{2}\.\d{4}', date_of_birth)):
                datetime.strptime(date_of_birth, '%d.%m.%Y')
                return True
            else:
                raise InvalidDateFormatError()
        except InvalidDateFormatError():
            return False
        except InvalidDateValueError():
            return False
       
