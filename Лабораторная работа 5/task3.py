from random import randint


def get_unique_list_numbers() -> list[int]:
    numbers = []
    for i in range(15):
        numbers.append(get_uniq_random_elem(-10, 10, numbers))
        i += 1
    return numbers


def get_uniq_random_elem(a: int, b: int, list_numbers: list[int]) -> int:
    rand_elem = randint(a, b)
    while rand_elem in list_numbers:
        rand_elem = randint(a, b)

    return rand_elem


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))