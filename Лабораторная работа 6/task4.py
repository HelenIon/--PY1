import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=None, new_line=None) -> list[dict]:
    if delimiter is None:
        delimiter = ','
    if new_line is None:
        new_line = '\n'

    list_of_dicts = []
    with open(filename) as file:
        data = file.readlines()
        headers = [line.rstrip(new_line) for line in data[0].split(delimiter)]

        for row in data[1:]:
            dictionary = {}
            row = [line.rstrip(new_line) for line in row.split(delimiter)]

            for i in range(len(row)):
                dictionary[headers[i]] = row[i]

            list_of_dicts.append(dictionary)

    return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
