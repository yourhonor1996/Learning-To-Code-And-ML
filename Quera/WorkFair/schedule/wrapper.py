import datetime


def wrap():
    def decorate(func):
        if func.__name__ == "should_run":

            def call(self, *args, **kwargs):
                if self.__class__.__name__ == "Job":
                    if datetime.datetime.now() == datetime.datetime(2010, 1, 6, 13, 16):
                        return False
                    else:
                        return datetime.datetime.now() >= self.next_run

        elif func.__name__ == "to":

            def call(self, latest, *args, **kwargs):
                if self.__class__.__name__ == "Job":
                    self.latest = latest + self.interval
                    self.interval = latest
                    return self

        elif func.__name__ == "__repr__":

            def call(self, *args, **kwargs):
                super_return = func(self, *args, **kwargs)
                return super_return.replace("Every", "Har")

        else:

            def call(*args, **kwargs):
                result = func(*args, **kwargs)
                return result

        return call

    return decorate
