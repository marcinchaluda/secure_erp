from model.hr import hr
from view import terminal as view


def list_employees():
    list_of_employes = hr.read_content_from_file_in_nested_list()
    line_of_text = "Nr."
    for i in range(len(hr.HEADERS)):
        line_of_text += " {:>12} ".format(hr.HEADERS[i])
    print(line_of_text)
    view.print_table(list_of_employes)


def add_employee():
    name = input("Please input name of employee: ")
    birth_date = input("Please input birth date: ")
    department = input("Please input department: ")
    clearance = input("Please input clearance: ")
    entry = [name, birth_date, department, clearance]
    hr.append_nested_list_and_write_content(entry)


def update_employee():
    number = input("Please input number of employee: ")
    name = input("Please input new name of employee: ")
    birth_date = input("Please input new birth date: ")
    department = input("Please input new department: ")
    clearance = input("Please input new clearance: ")
    entry = [name, birth_date, department, clearance]
    hr.update_nested_list_and_write_content(number, entry)


def delete_employee():
    number = input("Please input number of employee: ")
    hr.delete_nested_list_and_write_content(number)


def get_oldest_and_youngest():
    label = ("Oldest person:", "Youngest person:")
    list_of_employes = hr.read_content_from_file_in_nested_list()
    name = 1
    birth_date = 2
    list_of_birth_datas = []
    for employee in list_of_employes:
        list_of_birth_datas.append(employee[birth_date])
    max_data = max(list_of_birth_datas)
    min_data = min(list_of_birth_datas)
    for employee in list_employees:
        if max_data == employee[birth_date]:
            oldest_name = employee[name]
        if min_data == employee[birth_date]:
            youngest_name = employee[name]
    results = (oldest_name, youngest_name)
    view.print_general_results(results, label)


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


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
