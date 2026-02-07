from vebplib.text import Error

class Message[T]:
    def __init__(self, var: T, msg: Exception | str | Error = None):
        self.var: T = var

        if isinstance(msg, Error):
            tmp = msg
        elif isinstance(msg, (str, Exception)):
            tmp = Error(msg)
        else:
            raise TypeError(msg)

        self.msg: Error = tmp

    def __str__(self):
        return str(self.msg)

    def __iter__(self):
        yield self.var
        yield self.msg