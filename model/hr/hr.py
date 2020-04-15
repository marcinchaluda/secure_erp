""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def read_content_from_file_in_nested_list():
    return data_manager.read_table_from_file(DATAFILE)


def print_content_from_file_in_nested_list():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data


def append_nested_list_and_write_content(entry):
    data = data_manager.read_table_from_file(DATAFILE)
    name, birth_date, department, clearance = entry
    data_to_append = [util.generate_id(), name, birth_date, department, clearance]
    data.append(data_to_append)
    write_to_file(data)


def delete_nested_list_and_write_content(number):
    data = data_manager.read_table_from_file(DATAFILE)
    del data[int(number) - 1]
    write_to_file(data)


def update_nested_list_and_write_content(index_of_employee, entry):
    name, birth_date, department, clearance = entry
    list_of_employes = data_manager.read_table_from_file(DATAFILE)
    employee_atribute = {
        "index": int(index_of_employee) - 1,
        "name": 1,
        "birth date": 2,
        "department": 3,
        "clearance": 4
    }
    list_of_employes[employee_atribute["index"]][employee_atribute["name"]] = name
    list_of_employes[employee_atribute["index"]][employee_atribute["birth date"]] = birth_date
    list_of_employes[employee_atribute["index"]][employee_atribute["department"]] = department
    list_of_employes[employee_atribute["index"]][employee_atribute["clearance"]] = clearance
    write_to_file(list_of_employes)


def write_to_file(data):
    data_manager.write_table_to_file(DATAFILE, data)
