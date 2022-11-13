from pprint import pprint


def get_dict(number):
    return {'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)}


dict_list = [get_dict(number) for number in range(16)]

pprint(dict_list)