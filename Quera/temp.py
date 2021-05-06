class Sample:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


sample = Sample(2)
print(sample.get_x())
sample.set_x(20)
print(sample.get_x())
print(sample._Sample__x)
# print(sample.__x)
dir(sample)