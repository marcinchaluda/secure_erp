""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def read_data_from_file():
    return data_manager.read_table_from_file(DATAFILE)


def write_data_to_file(data):
    return data_manager.write_table_to_file(DATAFILE, data)


def list_transactions():
    transactions = read_data_from_file()
    transactions.insert(0, HEADERS)
    return transactions


def add_transaction(entry):
    transactions = read_data_from_file()
    product, price, date = entry
    new_transaction = [util.generate_id(), util.generate_id(), product, price, date]
    transactions.append(new_transaction)
    write_data_to_file(transactions)


def update_transaction(number, entry):
    index_of_transaction = int(number) - 1
    transactions = read_data_from_file()
    id, customer, product, price, date = entry
    transactions[index_of_transaction][0] = id
    transactions[index_of_transaction][1] = customer
    transactions[index_of_transaction][2] = product
    transactions[index_of_transaction][3] = price
    transactions[index_of_transaction][4] = date
    write_data_to_file(transactions)


def remove_transaction(number):
    transactions = read_data_from_file()
    del transactions[int(number) - 1]
    write_data_to_file(transactions)
