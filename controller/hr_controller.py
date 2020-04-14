from model.hr import hr
from view import terminal as view
import datetime


def list_employees():
    list_of_employes = hr.print_content_from_file_in_nested_list()
    view.print_table(list_of_employes)


def add_employee():
    entry = get_input_from_user("add")
    hr.append_nested_list_and_write_content(entry)


def update_employee():
    number = view.get_input("number of employee")
    entry = get_input_from_user("update")
    hr.update_nested_list_and_write_content(number, entry)


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
    number = view.get_input("number of employee")
    hr.delete_nested_list_and_write_content(number)


def get_oldest_and_youngest():
    label = ("Oldest person", "Youngest person")
    list_of_employes = hr.read_content_from_file_in_nested_list()
    name = 1
    birth_date = 2
    list_of_birth_datas = []
    for employee in list_of_employes:
        list_of_birth_datas.append(employee[birth_date])
    max_data = max(list_of_birth_datas)
    min_data = min(list_of_birth_datas)
    for employee in list_of_employes:
        if max_data == employee[birth_date]:
            youngest_name = employee[name]
        if min_data == employee[birth_date]:
            oldest_name = employee[name]
    results = (oldest_name, youngest_name)
    view.print_general_results(results, label)


def get_average_age():
    label = "Average age of employees"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    birth_date = 2
    list_of_birth_datas = []
    for employee in list_of_employes:
        year_of_birthday = ""
        for i in range(4):
            year_of_birthday += employee[birth_date][i]
        list_of_birth_datas.append(2020 - int(year_of_birthday))
    sum_of_age = 0
    for age in range(len(list_of_birth_datas)):
        sum_of_age += list_of_birth_datas[age]
    results = sum_of_age / len(list_of_birth_datas)
    view.print_general_results(results, label)


def next_birthdays():
    label = "Employees which have birthday in 14days from inputted date"
    list_of_employes = hr.read_content_from_file_in_nested_list()
    name = 1
    birth_date = 2
    list_of_names = []
    inputted_data = change_data_into_integer(view.get_input("data").split("-"))
    inputted_birthday = datetime.date(inputted_data["year"], inputted_data["month"], inputted_data["day"])
    for employee in list_of_employes:
        employee_data = change_data_into_integer(employee[birth_date].split("-"))
        employee_birthday = datetime.date(employee_data["year"], employee_data["month"], employee_data["day"])
        if abs((employee_birthday - inputted_birthday).days) <= 14:
            list_of_names.append(employee[name])
    view.print_general_results(list_of_names, label)


def change_data_into_integer(data):
    year, month, day = data[0], data[1], data[2]
    if month[0] == "0":
        month = month.replace("0", "", 1)
    if day[0] == "0":
        day = day.replace("0", "", 1)
    dictionary = {
                "year": int(year),
                "month": int(month),
                "day": int(day)
        }
    return dictionary


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
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
