import csv

base = {'id': 0,
        'name': 1,
        'surname': 2,
        'age': 3,
        'height': 4,
        'weight': 5,
        'eyesight': 6,
        'education': 7,
        'english_language': 8,
        }
FILE = r'C:\Users\username\Desktop\csv-olimp\Архив\ita.csv'
candidates = []
sort_idx = []
raw_data = []
sorted_data = []
approved = []


def get_number_of_rows():
    '''возвращает количество строк в файле csv'''
    with open(FILE) as file:
        return len(list(csv.reader(file)))


def get_raw_data():
    '''
    в переменную raw_data записывает каждую строку файла csv в виде списка
    '''
    with open(FILE) as file:
        for i in range(get_number_of_rows()):
            reader = csv.reader(file, delimiter='#')
            raw_data.append(next(reader))
    raw_data.pop(0)


def get_sort():
    '''
    в переменную sort_idx записывает правильный порядок индексов
    '''
    with open(FILE) as file:
        reader = csv.reader(file, delimiter='#')
        next_row = next(reader)

        right_row_idx = []
        for a in next_row:
            right_row_idx.append(base[a])
        global sort_idx
        sort_idx = right_row_idx


def sort_data():
    '''
    сортирует каждый элемент raw_data в по порядку индексов,
    записанных в sort_idx
    '''
    for candidate in raw_data:
        temp_element = {}
        temp_dict = {}
        for i in range(0, 9):
            temp_dict[candidate[i]] = sort_idx[i]
        for element, idx in temp_dict.items():
            temp_element[idx] = element
        sorted_data.append(temp_element)


def qualify():
    '''
    отбрасывает не подходщих кандидатов
    '''
    '''
    не менее 20 и не более 59 лет  key:3
    150-190 см  key:4
    зрение 1.0  key: 6
    Master или PhD  key: 7
    знание английского: true  key: 8
    '''
    for candidate in sorted_data:
        if 20 <= int(candidate[3]) or int(candidate[3]) >= 59:
            if 150 <= int(candidate[4]) or int(candidate[4]) >= 190:
                if float(candidate[6]) == 1.0:
                    if candidate[7] == 'Master' or candidate[7] == 'PhD':
                        if candidate[8]:
                            global approved
                            approved.append(candidate)


def sort_approved():
    '''
    сортрует допущенных в соответствии с правилами
    приоритет от 27 до 37 лет
    далее по алфавиту имя+фамилия
    '''
    for candidate in approved:  # TODO: работает неправильно, исправить
        if int(candidate[3]) < 27 or int(candidate[3]) > 37:
            approved.append(approved.pop(approved.index(candidate)))


get_sort()
get_raw_data()
sort_data()
qualify()

# print(sort_idx)
# print(sorted_data, 'сортированные')
print(approved, 'прошедшие')
sort_approved()
print(approved, 'прошедшие + сортировка')
