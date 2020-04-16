import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    random_id = ""
    for i in range(int(number_of_small_letters)):
        random_id += random.choice(string.ascii_lowercase)
    for i in range(int(number_of_capital_letters)):
        random_id += random.choice(string.ascii_uppercase)
    for i in range(int(number_of_digits)):
        random_id += random.choice(string.digits)
    for i in range(int(number_of_special_chars)):
        random_id += random.choice(allowed_special_chars)

    random_id = ''.join(random.sample(random_id, len(random_id)))
    return random_id
