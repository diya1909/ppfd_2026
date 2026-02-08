# ==============================
# ABSTRACTION IN PYTHON
# ==============================

from abc import ABC, abstractmethod

# Abstract class
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass


# Concrete class
class English(Greet):
    def say_hello(self):
        return "Hello!"


g = English()
print(g.say_hello())


# Abstract class with property
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass


class Dog(Animal):
    @property
    def species(self):
        return "Canine"


dog = Dog()
print(dog.species)


# Abstract + concrete method
class Animal2(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"


# ==============================
# ENCAPSULATION IN PYTHON
# ==============================

# Private variable example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


emp = Employee("Ramesh", 50000)
print(emp.name)
print(emp._Employee__salary)   # accessing private (not recommended)


# Proper way using method
class Employee2:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)


emp = Employee2("Rajesh", 60000)
print(emp.name)
emp.show_salary()


# Protected variable
class Employee3:
    def __init__(self, name, age):
        self.name = name
        self._age = age


class SubEmployee(Employee3):
    def show_age(self):
        print("Age:", self._age)


emp = SubEmployee("Vikas", 30)
print(emp.name)
emp.show_age()


# Public method and attribute
class Employee4:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


emp = Employee4("Jayesh")
emp.display_name()
print(emp.name)


# ==============================
# INHERITANCE IN PYTHON
# ==============================

# Single inheritance
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def show_role(self):
        print(self.name, "is an employee")


emp = Employee("Robin")
print("Name:", emp.name)
emp.show_role()


# Multiple inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary


class Employee2(Person, Job):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)


emp = Employee2("Ashok", 50000)
emp.details()


# Multilevel inheritance
class Employee3(Person):
    def show_role(self):
        print(self.name, "is an employee")


class Manager(Employee3):
    def department(self, dept):
        print(self.name, "manages", dept, "department")


mgr = Manager("Dinesh")
mgr.show_role()
mgr.department("HR")


# Hierarchical inheritance
class Employee4(Person):
    def role(self):
        print(self.name, "works as an employee")


class Intern(Person):
    def role(self):
        print(self.name, "is an intern")


emp = Employee4("Amit")
emp.role()

intern = Intern("Shlok")
intern.role()


# Hybrid inheritance
class Project:
    def __init__(self, project_name):
        self.project_name = project_name


class TeamLead(Employee4, Project):
    def __init__(self, name, project_name):
        Employee4.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)


lead = TeamLead("Sanjay", "AI Development")
lead.role()
lead.details()


# ==============================
# POLYMORPHISM IN PYTHON
# ==============================

# Method overriding (runtime polymorphism)
class Pen:
    def use(self):
        return "Writing"


class Eraser:
    def use(self):
        return "Erasing"


def perform_task(tool):
    print(tool.use())


perform_task(Pen())
perform_task(Eraser())


# Compile-time polymorphism (method overloading using default args)
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result


calc = Calculator()
print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))


# Runtime polymorphism
class Animal3:
    def sound(self):
        return "Some generic sound"


class Dog2(Animal3):
    def sound(self):
        return "Bark"


class Cat(Animal3):
    def sound(self):
        return "Meow"


animals = [Dog2(), Cat(), Animal3()]
for animal in animals:
    print(animal.sound())
