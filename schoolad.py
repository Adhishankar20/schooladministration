from file import File
from random import choice
class Main:


def __init__(self):

        # The file_handler object will be used to read and write to files.
        self.file_handler = File()

        login_menu_is_running = True

        while login_menu_is_running:

            print('1 - Sign up')
            print('2 - Login')

            menu_choice = input('\nEnter menu option: ')

            login_menu_is_running = False

            if menu_choice == '1':
                self.signup()
            elif menu_choice == '2':
                self.login()
            else:
                print('Please choose a number from the menu.')
                login_menu_is_running = True

        menu_is_running = True

        while menu_is_running:

            print('\n1 - Add a new student to the system.')
            print('2 - Display a student\'s details.')
            print('3 - Edit a students details.')
            print('4 - Log out.')

            menu_choice = input('\nEnter menu option: ')

            if menu_choice == '1':
                self.add_student()

            elif menu_choice == '2':
                self.print_student_details()

            elif menu_choice == '3':
                self.edit_student_details()

            elif menu_choice == '4':
                menu_is_running = False

            else:
                print('Please choose a number from the menu.')
def __init__(self):

        # The file_handler object will be used to read and write to files.
        self.file_handler = File()

        login_menu_is_running = True

        while login_menu_is_running:

            print('1 - Sign up')
            print('2 - Login')

            menu_choice = input('\nEnter menu option: ')

            login_menu_is_running = False

            if menu_choice == '1':
                self.signup()
            elif menu_choice == '2':
                self.login()
            else:
                print('Please choose a number from the menu.')
                login_menu_is_running = True

        menu_is_running = True

        while menu_is_running:

            print('\n1 - Add a new student to the system.')
            print('2 - Display a student\'s details.')
            print('3 - Edit a students details.')
            print('4 - Log out.')

            menu_choice = input('\nEnter menu option: ')

            if menu_choice == '1':
                self.add_student()

            elif menu_choice == '2':
                self.print_student_details()

            elif menu_choice == '3':
                self.edit_student_details()

            elif menu_choice == '4':
                menu_is_running = False

            else:
                print('Please choose a number from the menu.')
                class File:

    @staticmethod
    def get_accounts():
        with open('accounts.txt', 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def add_account(username, password):
        with open('accounts.txt', 'a') as file:
            file.write(username)
            file.write(', ')
            file.write(password)
            file.write('\n')

    @staticmethod
    def get_students():
        with open('student_details.txt', 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def add_student(student_details):
        with open('student_details.txt', 'a') as file:
            file.write(student_details)
            file.write('\n')

    @staticmethod
    def remove_student(student_id):
        pass

