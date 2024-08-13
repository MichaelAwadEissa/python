class Human:
    # Class variable
    species = "Homo sapiens"
    
    # Initializer / Instance variables
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Instance methods
    def speak(self, words):
        return f"{self.name} says: '{words}'"
    
    def walk(self, steps):
        return f"{self.name} walked {steps} steps."
    
    def introduce(self):
        return f"Hi, I'm {self.name}. I'm {self.age} years old and I'm {self.gender}."



class Employee(Human):
    # Class variable
    company_name = "TechCorp"
    
    # Initializer / Instance variables
    def __init__(self, name, age, gender, employee_id, position, salary):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
    
    # Instance methods
    def work(self):
        return f"{self.name} is working as a {self.position}."
    
    def get_salary(self):
        return f"{self.name}'s salary is ${self.salary}."
    
    def promote(self, new_position):
        self.position = new_position
        return f"{self.name} has been promoted to {self.position}."
