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


def biggest_revenue_transaction():
    transactions = read_data_from_file()
    price_index = HEADERS.index("Price")
    transaction_price = [float(transaction[price_index]) for transaction in transactions]
    transaction_index = transaction_price.index(max(transaction_price))
    return transactions[transaction_index]


def biggest_revenue_altogether():
    transactions = data_manager.read_table_from_file(DATAFILE)
    price_index = HEADERS.index("Price")
    product_index = HEADERS.index("Product")
    products_revenue = {}
    product_scores = []

    for transaction in transactions:
        if transaction[product_index] not in products_revenue.keys():
            products_revenue[transaction[product_index]] = [float(transaction[price_index])]
        else:
            products_revenue[transaction[product_index]].append(float(transaction[price_index]))

    for key, value in products_revenue.items():
        product_scores.append(sum(value))

    best_seller = max(product_scores)

    for key, value in products_revenue.items():
        if best_seller == sum(value):
            return key
