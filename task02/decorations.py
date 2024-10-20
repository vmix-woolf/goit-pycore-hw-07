def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "This name is already in the contacts."
        except IndexError:
            return "This name is absent in the contacts."

    return inner
