def get_count_char(str_):
    str_ = str_.lower().split()
    str_ = "".join(str_)
    str_dict = {}

    for char in str_:
        if char.isalpha():
            if char in str_dict:
                str_dict[char] += 1
            else:
                str_dict[char] = 1

    return str_dict


def get_percent_char(str_dict):
    total = sum(str_dict.values())
    for char in str_dict:
        str_dict[char] /= total / 100
        str_dict[char] = round(str_dict[char], 1)
    return str_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percent_char(get_count_char(main_str)))
