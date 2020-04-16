from model.hr import hr
from view import terminal as view
from os import system


def list_employees():
    list_of_employes = hr.print_content_from_file_in_nested_list()
    view.print_table(list_of_employes)


def add_employee():
    entry = get_input_from_user("add")
    hr.append_nested_list_and_write_content(entry)


def update_employee():
    try:
        number = view.get_input("number of employee")
        if int(number) == 0 or int(number) > len(hr.read_content_from_file_in_nested_list()):
            raise IndexError
        entry = get_input_from_user("update")
        hr.update_nested_list_and_write_content(number, entry)
    except IndexError:
        view.print_error_message("Index not found")


def get_input_from_user(mode):
    text = {
        "add": [
            "name",
            "birth date",
            "department",
            "clearance"
            ],
        "update": [
            "new name",
            "new birth date",
            "new department",
            "new clearance"
            ]
    }
    entry = view.get_inputs(text[mode])
    return entry


def delete_employee():
    try:
        number = view.get_input("number of employee")
        if int(number) == 0:
            raise IndexError
        hr.delete_nested_list_and_write_content(number)
    except IndexError:
        view.print_error_message("Index not found")


def get_oldest_and_youngest():
    label = ("Oldest person and Youngest person")
    list_of_employes = hr.read_content_from_file_in_nested_list()
    name = 1
    birth_date = 2
    dict_of_names_with_birth_date = {}
    for employee in list_of_employes:
        dict_of_names_with_birth_date[employee[birth_date]] = employee[name]
    latest_date = min(dict_of_names_with_birth_date)
    earliest_date = max(dict_of_names_with_birth_date)
    results = (dict_of_names_with_birth_date[latest_date], dict_of_names_with_birth_date[earliest_date])
    view.print_general_results(results, label)


def get_average_age():
    label = "Average age of employees"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    birth_date = 2
    sum_of_age = 0
    for employee in list_of_employes:
        birth_date_in_list = employee[birth_date].split("-")
        year_of_birthday = int(birth_date_in_list[0])
        sum_of_age += (2020 - year_of_birthday)
    results = sum_of_age / len(list_of_employes)
    view.print_general_results(results, label)


def next_birthdays():
    label = "Employees which have birthday in 14days from inputted date"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    list_of_employes_with_birthday = []
    name = 1
    birth_date = 2
    try:
        start_date = view.get_input("data")
        if not inputted_date_in_right_format(start_date):
            raise ValueError
        max_date = start_date.split("-")
        max_year, max_month, max_day = int(max_date[0]), int(max_date[1]), int(max_date[2]) + 14
        end_date = change_data_into_correct_format(max_day, max_month, max_year)
        for employee in list_of_employes:
            if employee[birth_date] >= start_date and employee[birth_date] <= end_date:
                list_of_employes_with_birthday.append(employee[name])
        view.print_general_results(list_of_employes_with_birthday, label)
    except ValueError:
        view.print_error_message("Data in invalid format")


def inputted_date_in_right_format(date):
    if len(date) == 10 and date[4] == "-" and date[7] == "-":
        if date[0].isdigit() and date[1].isdigit() and date[2].isdigit() and date[3].isdigit():
            if date[5].isdigit() and date[6].isdigit() and date[8].isdigit() and date[9].isdigit():
                return True
    return False


def change_data_into_correct_format(max_day, max_month, max_year):
    dict_of_days_in_month = {
        "1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30,
        "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31
    }
    days_in_month = dict_of_days_in_month[str(max_month)]
    if max_day > days_in_month:
        max_month = max_month + 1
        if max_month > 12:
            max_year = max_year + 1
            max_month = max_month - 12
        max_day = max_day - days_in_month
    if len(str(max_month)) == 1:
        max_month = "0" + str(max_month)
    if len(str(max_day)) == 1:
        max_day = "0" + str(max_day)
    return "-".join([str(max_year), str(max_month), str(max_day)])


def count_employees_with_clearance():
    label = "Number of employees with inputted clearance level or greater"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    clearance = 4
    iterator = 0
    number = view.get_input("clearance level")
    for employee in list_of_employes:
        if employee[clearance] >= number:
            iterator += 1
    view.print_general_results(iterator, label)


def count_employees_per_department():
    label = "Employees in department in dictionary"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    dictionary_of_departments = {}
    department = 3
    for employee in list_of_employes:
        if employee[department] in dictionary_of_departments:
            dictionary_of_departments[employee[department]] += 1
        else:
            dictionary_of_departments[employee[department]] = 1
    view.print_general_results(dictionary_of_departments, label)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            system("clear")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
