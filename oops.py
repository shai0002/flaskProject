'''
Class and objects
'''


class Interview:
    '''    The self parameter is a reference to the current instance of the class ,
    and is used to access variables that belong to the class.
    '''

    def __init__(self, schedule, type):
        self.schedule = schedule
        self.type = type

    def get_schedule(self):
        print(f"You have an interview scheduled on {self.schedule}")
        return True

    def get_type(self):
        if self.type == "1":
            print(f"Type {self.type} is Phone Screen")
        elif self.type == "2":
            print(f"Type {self.type} is Coding Challenge")
        else:
            print(f"Type {self.type} is Invalid")
        return

    def interview_type_info(self):
        print("This is a role specific interview")


class Hiring(Interview):
    '''
    This is an example of Inheritence
    '''

    def __init__(self, schedule, type, role):
        super().__init__(schedule, type)
        self.role = role

    def get_role(self):
        print(f"The role for this interview is {self.role}")
        return

    def interview_type_info(self):
        print("This is a Hiring Event")


interview = Hiring("04/22/2024", "2", "Python Developer")
interview.get_schedule()
interview.get_type()
interview.get_role()
interview.interview_type_info()  # Polymorphism Hiring's method overrides Interview class' implementation
interview = Interview("2024-04-16", "1")
interview.interview_type_info()

# -----------------------------------------------------------
'''
Singleton Pattern can only have one instance for a class '''
from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self):
        pass


class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        else:
            raise Exception("Singleton instance already exists")
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton instance already exists")
        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    @staticmethod
    def get_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton}")


p = PersonSingleton("Shehnaz", 30)
print(p)
p.get_data()
try:
    p2 = PersonSingleton("Another Name", 25)
except Exception as e:
    print("Error:", e)
