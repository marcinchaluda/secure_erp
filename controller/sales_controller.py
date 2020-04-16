from model.sales import sales
from view import terminal as view
import time
from os import system


def list_transactions():
    list_of_transactions = sales.list_transactions()
    view.print_table(list_of_transactions)


def add_transaction():
    entry = view.get_inputs(["product", "price", "date"])
    sales.add_transaction(entry)


def update_transaction():
    try:
        transaction_number = view.get_input("transaction number")
        if int(transaction_number) == 0 or int(transaction_number) > len(sales.read_data_from_file()):
            raise IndexError
        entry = view.get_inputs(["product", "price", "date"])
        sales.update_transaction(transaction_number, entry)
    except IndexError:
        view.print_error_message("Index not found")


def delete_transaction():
    try:
        transaction_number = view.get_input("transaction number")
        if int(transaction_number) == 0:
            raise IndexError
        sales.remove_transaction(transaction_number)
    except IndexError:
        view.print_error_message("Index not found")


def get_biggest_revenue_transaction():
    transactions = sales.read_data_from_file()
    price_index = sales.HEADERS.index("Price")
    transaction_price = [float(transaction[price_index]) for transaction in transactions]
    transaction_index = transaction_price.index(max(transaction_price))
    view.print_message(transactions[transaction_index])


def get_biggest_revenue_product():
    transactions = sales.read_data_from_file()
    price_index = sales.HEADERS.index("Price")
    product_index = sales.HEADERS.index("Product")
    products_revenue = {}
    best_seller = 0

    for transaction in transactions:
        if transaction[product_index] not in products_revenue.keys():
            products_revenue[transaction[product_index]] = float(transaction[price_index])
        else:
            products_revenue[transaction[product_index]] += float(transaction[price_index])
    best_seller = [key for key in products_revenue if products_revenue[key] == max(products_revenue.values())] 
    print(best_seller[0])


def count_transactions_between():
    start_date, end_date = view.get_inputs(["start date", "end date"])
    transactions = sales.read_data_from_file()
    view.print_message(len(transactions_between_dates(start_date, end_date, transactions)))


def transactions_between_dates(start_date, end_date, transactions):
    start_date = time.strptime(start_date, "%Y-%m-%d")
    end_date = time.strptime(end_date, "%Y-%m-%d")
    data_index = sales.HEADERS.index("Date")
    transactions_between_dates = []
    for transaction in transactions:
        transaction[data_index] = time.strptime(transaction[data_index], "%Y-%m-%d")
        if transaction[data_index] >= start_date and transaction[data_index] <= end_date:
            transactions_between_dates.append(transaction)
    return transactions_between_dates


def sum_transactions_between():
    start_date, end_date = view.get_inputs(["start date", "end date"])
    transactions = sales.read_data_from_file()
    price_index = sales.HEADERS.index("Price")
    transactions_price = [float(element[price_index]) for element in transactions_between_dates(start_date, end_date, transactions)]
    prices_sum = sum(transactions_price)
    view.print_message(prices_sum)


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu("Sales", options)


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
