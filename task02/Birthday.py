from datetime import datetime
from Field import Field
from Exceptions import FormatError
import re

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            # add data correctness validation
            if bool(re.match(r'\d{2}\.\d{2}\.\d{4}', value)):
                #  and convert the string to a datetime object
                self.value = datetime.strptime(value, '%d.%m.%Y')
            else:
                raise FormatError()
        except FormatError:
            print(f"Invalid format. Use DD.MM.YYYY")
            exit()
        except ValueError:
            print(f"Invalid date format. Use correct DD, MM and YYYY")
            exit()    
