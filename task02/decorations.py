import constants

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return constants.VALUE_ERROR
        except KeyError:
            return constants.KEY_ERROR
        except IndexError:
            return constants.INDEX_ERROR

    return inner
