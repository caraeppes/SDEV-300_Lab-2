"""
Cara Eppes
5/31/2024
SDEV 300
Lab 2

This is a program that provides the user with a menu of functional options.
The user can choose to generate a secure password, calculate a percentage
with a given degree of precision, get the number of days until July 4, 2025,
calculate a triangle leg length using the Law of Cosines, or calculate the
volume of a right circle cylinder.
"""

import string
import secrets
import datetime
import math


class PasswordGenerator:
    """Class for generating a secure password with specific constraints"""

    def __init__(self):
        """Initialize the password generator"""
        self.password_length = None
        self.min_uppercase = None
        self.min_lowercase = None
        self.min_digits = None
        self.min_special_chars = None
        self.allowed_characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self):
        """
        Gets input from user for password length, minimum uppercase letters,
        minimum lowercase letters,minimum digits, and minimum special characters
        and generates a secure password using the given constraints
        """

        # Gets and validates user input and sets values
        self.set_password_length()
        self.set_min_uppercase()
        self.set_min_lowercase()
        self.set_min_digits()
        self.set_min_special_chars()

        # True if sum of provided minimum values is less than or equal to password length
        run_password_generator = (self.min_uppercase + self.min_lowercase + self.min_digits
                                  + self.min_special_chars <= self.password_length)

        # Generates passwords until all constraints are met
        while run_password_generator:
            password = ''.join(secrets.choice(self.allowed_characters)
                               for i in range(self.password_length))

            if (sum(c.isupper() for c in password) >= self.min_uppercase
                    and sum(c.islower() for c in password) >= self.min_lowercase
                    and sum(c.isdigit() for c in password) >= self.min_digits
                    and self.get_special_chars_count(password) >= self.min_special_chars):
                print("Password Generated: ", password)
                break

        # Restarts password generator if sum of minimum constraints is greater than password length
        if not run_password_generator:
            print('The sum of the minimum values provided is greater than the password length.  '
                  'Please try again.\n')
            self.generate_password()

    def get_special_chars_count(self, password):
        """Returns the number of special characters in a string"""
        return len([c for c in password if c in string.punctuation])

    def set_password_length(self):
        """Gets and validates input for password length"""
        password_length = input("\nPassword Length: ")
        if validate_digit_greater_than_zero(password_length):
            self.password_length = int(password_length)
        else:
            self.set_password_length()

    def set_min_uppercase(self):
        """Gets and validates input for minimum uppercase letters"""
        min_uppercase = input('Minimum Number of Uppercase Letters: ')
        if self.validate_minimums(min_uppercase):
            self.min_uppercase = int(min_uppercase)
        else:
            self.set_min_uppercase()

    def set_min_lowercase(self):
        """Gets and validates input for minimum lowercase letters"""
        min_lowercase = input('Minimum Number of Lowercase Letters: ')
        if self.validate_minimums(min_lowercase):
            self.min_lowercase = int(min_lowercase)
        else:
            self.set_min_lowercase()

    def set_min_digits(self):
        """Gets and validates input for minimum digits"""
        min_digits = input('Minimum Number of Digits: ')
        if self.validate_minimums(min_digits):
            self.min_digits = int(min_digits)
        else:
            self.set_min_digits()

    def set_min_special_chars(self):
        """Gets and validates input for minimum special characters"""
        min_special_chars = input('Minimum Number of Special Characters: ')
        if self.validate_minimums(min_special_chars):
            self.min_special_chars = int(min_special_chars)
        else:
            self.set_min_special_chars()

    def validate_minimums(self, value):
        """Validates input is a positive integer and less than the password length"""
        return validate_is_digit(value) and self.validate_less_than_password_length(value)

    def validate_less_than_password_length(self, value):
        """Validates that input value is less than password length"""
        if int(value) <= self.password_length:
            return True
        print("Value cannot be greater than the password length.  Please try again.\n")
        return False


class PercentageCalculator:
    """Class for calculating a percentage with a specific degree of precision"""

    def __init__(self):
        """Initializes the percentage calculator"""
        self.numerator = None
        self.denominator = None
        self.precision = None

    def calculate_percentage(self):
        """Gets user input for numerator, denominator and precision and calculates the percentage"""
        self.set_numerator()
        self.set_denominator()
        self.set_precision()
        percentage = self.numerator / self.denominator
        print(f"{self.numerator} / {self.denominator} = {percentage:.{self.precision}f}%")

    def set_numerator(self):
        """Gets and validates input for numerator"""
        numerator = input('Enter a positive integer numerator: ')
        if validate_is_digit(numerator):
            self.numerator = int(numerator)
        else:
            self.set_numerator()

    def set_denominator(self):
        """Gets and validates input for denominator"""
        denominator = input('Enter a positive integer denominator: ')
        if validate_digit_greater_than_zero(denominator):
            self.denominator = int(denominator)
        else:
            self.set_denominator()

    def set_precision(self):
        """Gets and validates input for precision"""
        precision = input('Enter a positive integer float precision: ')
        if validate_is_digit(precision):
            self.precision = int(precision)
        else:
            self.set_precision()


class LawOfCosinesCalculator:
    """Class for calculating the length of side c of a triangle using the Law of Cosines"""

    def __init__(self):
        """Initializes the Law of Cosines Calculator"""
        self.side_a = None
        self.side_b = None
        self.angle_c = None

    def calculate_triangle_leg(self):
        """
        Gets user input for the lengths of a triangle's sides a and b and the angle of
        angle C in degrees. Calculates the length of side c using the Law of Cosines.
        """
        self.set_side_a()
        self.set_side_b()
        self.set_angle_c()

        # Calculating length of side c using Law of Cosines
        cos_angle_c = math.cos(math.radians(self.angle_c))
        c_squared = (self.side_a ** 2 + self.side_b ** 2
                     - (2 * self.side_a * self.side_b * cos_angle_c))
        side_c = math.sqrt(c_squared)

        print(f"The length of side c is {side_c:.2f}.")

    def set_side_a(self):
        """Gets and validates user input for length of side a"""
        side_a = input("Enter a positive integer for the length of side a: ")
        if validate_digit_greater_than_zero(side_a):
            self.side_a = int(side_a)
        else:
            self.set_side_a()

    def set_side_b(self):
        """Gets and validates user input for length of side b"""
        side_b = input("Enter a positive integer for the length of side b: ")
        if validate_digit_greater_than_zero(side_b):
            self.side_b = int(side_b)
        else:
            self.set_side_b()

    def set_angle_c(self):
        """Gets and validates user input for angle of angle C"""
        angle_c = input("Enter a positive integer for the angle of C: ")
        if validate_digit_greater_than_zero(angle_c):
            if int(angle_c) >= 180:
                print("Angle must be less than 180 degrees.  Please try again.")
                self.set_angle_c()
            else:
                self.angle_c = int(angle_c)
        else:
            self.set_angle_c()


class CylinderVolumeCalculator:
    """Class for calculating the volume of a right circle cylinder"""

    def __init__(self):
        """Initializes the Cylinder Volume Calculator"""
        self.radius = None
        self.height = None

    def calculate_volume(self):
        """Gets user input for radius and height of the cylinder and calculates the volume"""
        self.set_radius()
        self.set_height()

        volume = math.pi * self.radius ** 2 * self.height

        print(f"The volume of the cylinder is {volume:.5f}.")

    def set_radius(self):
        """Gets and validates user input for radius of the cylinder"""
        radius = input("Enter a positive integer for the radius of the cylinder: ")
        if validate_digit_greater_than_zero(radius):
            self.radius = int(radius)
        else:
            self.set_radius()

    def set_height(self):
        """Gets and validates user input for height of the cylinder"""
        height = input("Enter a positive integer for the height of the cylinder: ")
        if validate_digit_greater_than_zero(height):
            self.height = int(height)
        else:
            self.set_height()


def display_menu():
    """Prints the menu options to the console"""
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


def run(password_generator, percentage_calculator, law_of_cosines_calculator,
        cylinder_volume_calculator):
    """Displays menu to user and runs the program until the user chooses to exit"""
    print("Welcome to the Python SDEV300 Lab 2 Application.")

    while True:
        display_menu()
        selection = input("Enter selection: ")
        if selection == "a":
            password_generator.generate_password()
        elif selection == "b":
            percentage_calculator.calculate_percentage()
        elif selection == "c":
            create_date_countdown()
        elif selection == "d":
            law_of_cosines_calculator.calculate_triangle_leg()
        elif selection == "e":
            cylinder_volume_calculator.calculate_volume()
        elif selection == "f":
            print("Exiting program.  Thanks for using the Python SDEV300 Lab 2 Application.")
            break
        else:
            print("Invalid menu selection.  Please enter a valid option (a - f).")


def validate_is_digit(value):
    """Validates that the input is a positive integer or zero"""
    if value.isdigit():
        return True
    print("Value must be a positive number.  Please try again.\n")
    return False


def validate_digit_greater_than_zero(value):
    """Validates that the input is a positive integer greater than zero"""
    if not validate_is_digit(value):
        return False
    if int(value) > 0:
        return True
    print("Value cannot be zero.  Please enter a positive integer.\n")
    return False


def create_date_countdown():
    """Calculates and prints the number of days from today until July 4, 2025"""
    today = datetime.date.today()
    target_date = datetime.date(2025, 7, 4)
    days_to_target_date = target_date - today
    print(f"There are {days_to_target_date.days} days until July 4, 2025.")


def main():
    """Main function"""
    password_generator = PasswordGenerator()
    percentage_calculator = PercentageCalculator()
    law_of_cosines_calculator = LawOfCosinesCalculator()
    cylinder_volume_calculator = CylinderVolumeCalculator()

    run(password_generator, percentage_calculator, law_of_cosines_calculator,
        cylinder_volume_calculator)


main()
