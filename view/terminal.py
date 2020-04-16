def print_menu(title, list_options):
    print("{}:".format(title))
    for i in range(len(list_options)):
        if i != 0:
            print("({}) ".format(i), list_options[i])
    print("({}) ".format("0"), list_options[0])


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(str(message) + '\n')


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int or type(result) == float:
        print(f"{label}: {round(result, 2)}")
    elif type(result) == list or type(result) == tuple:
        print(label + ":")
        print(*result)
    else:
        print(label + ":")
        for key in result:
            print(str(key + ': ' + str(result[key])), end='; ')
        print()


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    longest_string = []
    for element in table:
        for text in element:
            longest_string.append(len(text))
    length_of_longest_string = max(longest_string)
    border_line = get_border_line_from_max_word(len(table[0]), length_of_longest_string)
    dividing_line = get_dividing_line_from_max_word(len(table[0]), length_of_longest_string)
    index = 0
    line_of_text = ""
    print(border_line)
    for row in table:
        line_of_text = get_starting_index_of_line(index)
        for col in row:
            line_of_text += get_line_of_text_from_max_word_and_col(col, length_of_longest_string)
        if index != 0:
            print(dividing_line)
        print(line_of_text)
        index += 1
    print(border_line)


def get_border_line_from_max_word(len_of_table, max_word):
    if max_word < 16:
        return "+" + ("-" * ((len_of_table * 20) - 2)) + "+"
    return "+" + ("-" * ((len_of_table * 29))) + "+"


def get_dividing_line_from_max_word(len_of_table, max_word):
    start_string = "+" + ("-" * 8)
    if max_word < 16:
        return start_string + ("+" + ("-" * 17)) * len_of_table + "+"
    return start_string + ("+" + ("-" * 26)) * len_of_table + "+"


def get_starting_index_of_line(index):
    if index == 0:
        return "| {:^6} |".format("Index")
    return "| {:^6} |".format(str(index))


def get_line_of_text_from_max_word_and_col(col, max_word):
    if max_word < 16:
        return " {:^15} |".format(col)
    return " {:^24} |".format(col)


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
    print(str(message) + '\n')
