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
    transaction_number = view.get_input("transaction number")
    entry = view.get_inputs(["id", "customer", "product", "price", "date"])
    sales.update_transaction(transaction_number, entry)


def delete_transaction():
    try:
        transaction_number = view.get_input("transaction number")
        if transaction_number == 0:
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
            view.print_message(key)


def check_dates(start_date, end_date, transaction_date):
    start_date = time.strptime(start_date, "%Y-%m-%d")
    end_date = time.strptime(end_date, "%Y-%m-%d")
    transaction_date = time.strptime(transaction_date, "%Y-%m-%d")
    if transaction_date >= start_date and transaction_date <= end_date:
        return True
    return False


def count_transactions_between(other_funtion_use=False):
    start_date, end_date = view.get_inputs(["start date", "end date"])
    transactions = sales.read_data_from_file()
    data_index = sales.HEADERS.index("Date")
    transactions_between_dates = []
    for transaction in transactions:
        compare_dates = check_dates(start_date, end_date, transaction[data_index])
        if compare_dates:
            transactions_between_dates.append(transaction)
    if other_funtion_use:
        return transactions_between_dates
    else:
        view.print_message(len(transactions_between_dates))


def sum_transactions_between():
    transactions_between_dates = count_transactions_between(True)
    price_index = sales.HEADERS.index("Price")
    transactions_price = [float(element[price_index]) for element in transactions_between_dates]
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
