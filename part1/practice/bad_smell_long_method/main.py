# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля

import operator

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(csv):
    # Чтение данных из строки
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def _sorted(data):
    # Сортировка по возрасту по возрастанию
    data_sorted = sorted(data, key=operator.itemgetter('age'))
    return data_sorted


def _filter(data, age: int = 10):
    # Фильтрация по возрасту
    result_data = []
    for person in data:
        if person['age'] < age:
            continue
        else:
            result_data.append(person)
    return result_data


def get_users_list():
    data = _read(csv)
    sorted_data = _sorted(data)
    filtered_data = _filter(sorted_data)
    return filtered_data


if __name__ == '__main__':
    print(get_users_list())
