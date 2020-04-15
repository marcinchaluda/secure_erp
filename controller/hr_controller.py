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
        entry = get_input_from_user("update")
        number_of_employee = entry[0]
        if int(entry[number_of_employee]) == 0:
            raise IndexError
        hr.update_nested_list_and_write_content(entry)
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
            "number of employee",
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
    dict_of_birth_datas = {}
    for employee in list_of_employes:
        dict_of_birth_datas[employee[birth_date]] = employee[name]
    oldest_date = min(dict_of_birth_datas)
    youngest_date = max(dict_of_birth_datas)
    results = (dict_of_birth_datas[oldest_date], dict_of_birth_datas[youngest_date])
    view.print_general_results(results, label)


def get_average_age():
    label = "Average age of employees"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    birth_date = 2
    list_of_birth_datas = []
    for employee in list_of_employes:
        year_of_birthday = employee[birth_date].split("-")
        list_of_birth_datas.append(2020 - int(year_of_birthday[0]))
    sum_of_age = 0
    for age in range(len(list_of_birth_datas)):
        sum_of_age += list_of_birth_datas[age]
    results = sum_of_age / len(list_of_birth_datas)
    view.print_general_results(results, label)


def next_birthdays():
    label = "Employees which have birthday in 14days from inputted date"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    list_of_employes_with_birthday = []
    name = 1
    birth_date = 2
    start_data = view.get_input("data")
    max_data = start_data.split("-")
    max_year, max_month, max_day = int(max_data[0]), int(max_data[1]), int(max_data[2]) + 14
    if max_day > 30:
        max_month = max_month + 1
        if max_month > 12:
            max_year = max_year + 1
            max_month = max_month - 12
        max_day = max_day - 30
    if len(str(max_month)) == 1:
        max_month = "0" + str(max_month)
    if len(str(max_day)) == 1:
        max_day = "0" + str(max_day)
    end_data = "-".join([str(max_year), str(max_month), str(max_day)])
    for employee in list_of_employes:
        if employee[birth_date] >= start_data and employee[birth_date] <= end_data:
            list_of_employes_with_birthday.append(employee[name])
    view.print_general_results(list_of_employes_with_birthday, label)


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
