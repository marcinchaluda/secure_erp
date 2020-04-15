""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def read_content_from_file_in_nested_list():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data


def append_nested_list_and_write_content(entry):
    data = data_manager.read_table_from_file(DATAFILE)
    name, email, subscribed = entry
    data_to_append = [util.generate_id(), name, email, subscribed]
    data.append(data_to_append)
    write_to_file(data)


def delete_nested_list_and_write_content(number):
    data = data_manager.read_table_from_file(DATAFILE)
    del data[int(number) - 1]
    write_to_file(data)


def update_nested_list_and_write_content(number, entry):
    index_of_customer = int(number) - 1
    list_of_customers = data_manager.read_table_from_file(DATAFILE)
    name, email, subscribed = entry
    list_of_customers[index_of_customer][1] = name
    list_of_customers[index_of_customer][2] = email
    list_of_customers[index_of_customer][3] = subscribed
    write_to_file(list_of_customers)


def write_to_file(data):
    return data_manager.write_table_to_file(DATAFILE, data)
