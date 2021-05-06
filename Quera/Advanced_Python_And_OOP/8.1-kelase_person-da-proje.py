import math


class Person:
    instances = []

    def __init__(self, name, age):
        Person.instances.append(self)
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place = None

    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        return sum([person.calc() for person in  Person.instances])
    
