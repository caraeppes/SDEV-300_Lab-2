import string
import secrets
import datetime
import math


class PasswordGenerator:

    def __init__(self):
        self.password_length = None
        self.minimum_uppercase_letters = None
        self.minimum_lowercase_letters = None
        self.minimum_digits = None
        self.minimum_special_characters = None
        self.allowed_characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self):
        self.set_password_length()
        self.set_minimum_uppercase_letters()
        self.set_minimum_lowercase_letters()
        self.set_minimum_digits()
        self.set_minimum_special_characters()

        run_password_generator = (self.minimum_uppercase_letters + self.minimum_lowercase_letters + self.minimum_digits
                                  + self.minimum_special_characters <= self.password_length)

        while run_password_generator:
            password = ''.join(secrets.choice(self.allowed_characters) for i in range(self.password_length))
            if (sum(c.isupper() for c in password) >= self.minimum_uppercase_letters
                and sum(c.islower() for c in password) >= self.minimum_lowercase_letters
                and sum(c.isdigit() for c in password) >= self.minimum_digits
                    and self.get_number_of_special_characters(password) >= self.minimum_special_characters):
                print("Password Generated: ", password)
                break

        if not run_password_generator:
            print('The sum of the minimum values provided is greater than the password length.  Please try again.\n')
            self.generate_password()

    def get_number_of_special_characters(self, password):
        return len([c for c in password if c in string.punctuation])

    def set_password_length(self):
        password_length = input("\nPassword Length: ")
        if validate_is_digit(password_length):
            self.password_length = int(password_length)
        else:
            self.set_password_length()

    def set_minimum_uppercase_letters(self):
        minimum_uppercase_letters = input('Minimum Number of Uppercase Letters: ')
        if self.validate_minimums(minimum_uppercase_letters):
            self.minimum_uppercase_letters = int(minimum_uppercase_letters)
        else:
            self.set_minimum_uppercase_letters()

    def set_minimum_lowercase_letters(self):
        minimum_lowercase_letters = input('Minimum Number of Lowercase Letters: ')
        if self.validate_minimums(minimum_lowercase_letters):
            self.minimum_lowercase_letters = int(minimum_lowercase_letters)
        else:
            self.set_minimum_lowercase_letters()

    def set_minimum_digits(self):
        minimum_digits = input('Minimum Number of Digits: ')
        if self.validate_minimums(minimum_digits):
            self.minimum_digits = int(minimum_digits)
        else:
            self.set_minimum_digits()

    def set_minimum_special_characters(self):
        minimum_special_characters = input('Minimum Number of Special Characters: ')
        if self.validate_minimums(minimum_special_characters):
            self.minimum_special_characters = int(minimum_special_characters)
        else:
            self.set_minimum_special_characters()

    def validate_minimums(self, value):
        return validate_is_digit(value) and self.validate_less_than_password_length(value)

    def validate_less_than_password_length(self, value):
        if int(value) <= self.password_length:
            return True
        else:
            print("Value cannot be greater than the password length.  Please try again.")
            return False


class PercentageCalculator:

    def __init__(self):
        self.numerator = None
        self.denominator = None
        self.precision = None

    def calculate_percentage(self):
        self.set_numerator()
        self.set_denominator()
        self.set_precision()
        percentage = self.numerator / self.denominator
        print(f"{self.numerator} / {self.denominator} = {percentage:.{self.precision}f}%")

    def set_numerator(self):
        numerator = input('Enter a positive integer numerator: ')
        if validate_is_digit(numerator):
            self.numerator = int(numerator)
        else:
            self.set_numerator()

    def set_denominator(self):
        denominator = input('Enter a positive integer denominator: ')
        if validate_is_digit(denominator):
            self.denominator = int(denominator)
            if self.denominator == 0:
                print("Denominator cannot be 0.  Please try again.")
                self.set_denominator()
        else:
            self.set_denominator()

    def set_precision(self):
        precision = input('Enter a positive integer float precision: ')
        if validate_is_digit(precision):
            self.precision = int(precision)
        else:
            self.set_precision()


class DateCountdown:

    def create_countdown(self):
        today = datetime.date.today()
        target_date = datetime.date(2025, 7, 4)
        days_to_target_date = target_date - today
        print(f"There are {days_to_target_date.days} days until July 4, 2025.")

class LawOfCosinesCalculator:

    def __init__(self):
        self.line_a = None
        self.line_b = None
        self.angle_c = None

    def calculate_triangle_leg(self):
        self.set_line_a()
        self.set_line_b()
        self.set_angle_c()

        cos_angle_c = math.cos(math.radians(self.angle_c))
        c_squared = self.line_a ** 2 + self.line_b ** 2 - (2 * self.line_a * self.line_b * cos_angle_c)
        line_c = math.sqrt(c_squared)
        print(f"The length of line c is {line_c:.2f}.")

    def set_line_a(self):
        line_a = input("Enter a positive integer for the length of line a: ")
        if validate_is_digit(line_a):
            self.line_a = int(line_a)
        else:
            self.set_line_a()

    def set_line_b(self):
        line_b = input("Enter a positive integer for the length of line b: ")
        if validate_is_digit(line_b):
            self.line_b = int(line_b)
        else:
            self.set_line_b()

    def set_angle_c(self):
        angle_c = input("Enter a positive integer for the angle of C: ")
        if validate_is_digit(angle_c):
            self.angle_c = int(angle_c)
        else:
            self.set_angle_c()


class CylinderVolumeCalculator:

    def __init__(self):
        self.radius = None
        self.height = None

    def calculate_volume(self):
        self.set_radius()
        self.set_height()

        volume = math.pi * self.radius ** 2 * self.height

        print(f"The volume of the cylinder is {volume:.5f}.")

    def set_radius(self):
        radius = input("Enter a positive integer for the radius of the cylinder: ")
        if validate_is_digit(radius):
            self.radius = int(radius)
        else:
            self.set_radius()

    def set_height(self):
        height = input("Enter a positive integer for the height of the cylinder: ")
        if validate_is_digit(height):
            self.height = int(height)
        else:
            self.set_height()


def display_menu():
    menu = """ 
    What would you like to do today?
        a. Generate a Secure Password 
        b. Calculate and format a percentage
        c. How many days from today until July 4, 2025?
        d. Use the Law of Cosines to calculate the leg of a triangle
        e. Calculate the volume of a Right Circular Cylinder
        f. Exit Program 
        """
    print(menu)

def run(password_generator, percentage_calculator, date_countdown, law_of_cosines_calculator, cylinder_volume_calculator):
    print("Welcome to the Python SDEV300 Lab 2 Application.")

    while True:
        display_menu()
        selection = input("Enter selection: ")
        if selection == "a":
            password_generator.generate_password()
        elif selection == "b":
            percentage_calculator.calculate_percentage()
        elif selection == "c":
            date_countdown.create_countdown()
        elif selection == "d":
            law_of_cosines_calculator.calculate_triangle_leg()
        elif selection == "e":
            cylinder_volume_calculator.calculate_volume()
        elif selection == "f":
            print("Exiting program.  Thanks for using the Python SDEV300 Lab 2 Application.")
            break
        else:
            print("Invalid menu selection.  Please enter a valid option (a - f).")




def validate_is_digit(input):
    if input.isdigit():
        return True
    else:
        print("Value must be a positive number.  Please try again.")
        return False


def main():
    """Main function"""
    password_generator = PasswordGenerator()
    percentage_calculator = PercentageCalculator()
    date_countdown = DateCountdown()
    law_of_cosines_calculator = LawOfCosinesCalculator()
    cylinder_volume_calculator = CylinderVolumeCalculator()

    run(password_generator, percentage_calculator, date_countdown, law_of_cosines_calculator, cylinder_volume_calculator)

main()
