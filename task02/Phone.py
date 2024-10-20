from Field import Field
from Exceptions import ExactDigitException

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
    
    def validation_phone(phone_number)-> bool:
        try:
            if len(phone_number) == 3 and phone_number.isdigit():
                return True
            else:
                raise ExactDigitException()
        except ExactDigitException:
            # print(f'Phone should consist of exactly 3 digits!')
            return False
