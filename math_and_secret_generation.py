import string
import secrets


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
        password_length = input("Password Length: ")
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
        return

    def set_numerator(self):
        numerator = input('Enter a positive integer numerator: ')


def validate_is_digit(input):
    if input.isdigit():
        return True
    else:
        print("Value must be a number.  Please try again.")
        return False

def main():
    """Main function"""
    password_generator = PasswordGenerator()
    password_generator.generate_password()


main()
