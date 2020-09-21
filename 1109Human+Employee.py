# Create a class Human, everyone has a name, create a method in the class that displays 
# a welcome message to a each person. 
# Create a class method in the class that returns 
# information that it is a species of "Homosapiens". 
# And also in the class create a static method that returns an arbitrary message. 

# 
# class Human():
#     species = 'Homosapiens'
#     def __init__(self, name):
#         self.name = name

#     def welcome(self):
#         print(f'Hi, {self.name}!')
    
#     def species_human():
#         return f'All of you are {Human.species}!'

#     def static_method():
#         return 'Bye-bye!'

# H1 = Human('Adam')
# H1.welcome()
# print(Human.species_human())
# print(Human.static_method())


class Employee:
    """Class for employees, with names and salaries"""
    count = 0
    def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.count += 1

    def total_empl():
        print(f'Total number of employees is {Employee.count}')

    def empl_info(self):
        return f"Employee name is {self.name}, employee salary is {self.salary}"

    
e_1 = Employee('Ostap', 340)
e_2 = Employee('Bogdan', 400)
Employee.total_empl()
print(e_1.empl_info())
print(e_2.empl_info())
print("Employee.__doc__:", Employee.__doc__)  
print("Employee.__name__:", Employee.__name__)  
print("Employee.__module__:", Employee.__module__)  
print("Employee.__bases__:", Employee.__bases__)  
print("Employee.__dict__:", Employee.__dict__) 
