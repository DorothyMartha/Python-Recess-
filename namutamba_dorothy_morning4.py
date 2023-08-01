class Temperature:
    def __init__(self, Celsius):
        self._celsius = Celsius
    
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Create an instance of Temperature
temperature = Temperature(37)

# Call the fahrenheit method to get the Fahrenheit value
temperature_fahrenheit = temperature.fahrenheit()

print(f"{temperature._celsius} degrees Celsius is equal to {temperature_fahrenheit} degrees Fahrenheit.")
print("****************************************************************")
#Assignment 1 
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def give_pay_increment(self, increment_amount):
        self._salary += increment_amount


# Create an instance of Employee
employee = Employee("Dorothy Martha", 850000)

# Get the employee's current salary
current_salary = employee.get_salary()
print(f"Current salary of {employee.get_name()}: {current_salary} Ugx")

# Give a pay increment of 150,000 Ugx
increment_amount = 150000
employee.give_pay_increment(increment_amount)

# Get the updated salary
new_salary = employee.get_salary()
print(f"New salary of {employee.get_name()}: {new_salary} Ugx")
