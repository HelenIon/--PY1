import random


def get_random_password(length: int = None) -> str:
    abc = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    if length is not None and length > 0:
        return random.sample(abc + abc.upper() + numbers, length)
    else:
        return random.sample(abc + abc.upper() + numbers, 8)


print(get_random_password())