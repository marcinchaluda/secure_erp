def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for i in range(len(list_options)):
        print(i, " ", list_options[i])


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print(label)
    print(result)


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    longest_string = []
    for element in table:
        for text in element:
            longest_string.append(len(text))
    max_word = max(longest_string)
    index = 0
    if max_word < 16:
        border_line = "+" + ("-" * ((len(table[0]) * 20) - 2)) + "+"
    else:
        border_line = "+" + ("-" * ((len(table[0]) * 29) - 2)) + "+"
    print(border_line)
    for row in table:
        if index == 0:
            line_of_text = "| {:^6} |".format("Index")
        else:
            line_of_text = "| {:^6} |".format(str(index))
        for col in row:
            if max_word < 16:
                line_of_text += " {:^15} |".format(col)
            else:
                line_of_text += " {:^24} |".format(col)
        if index != 0:
            print(border_line)
        print(line_of_text)
        index += 1
    print(border_line)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(f"Input {label}: ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    user_data = []
    for label in labels:
        user_input = input(f"Input {label}: ")
        user_data.append(user_input)
    return user_data


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass
