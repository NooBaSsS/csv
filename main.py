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
FILES = [
    r'C:\Users\username\Desktop\csv\Архив\ger.csv',
    r'C:\Users\username\Desktop\csv\Архив\ita.csv',
    r'C:\Users\username\Desktop\csv\Архив\rus.csv',
    r'C:\Users\username\Desktop\csv\Архив\us.csv',
    ]
candidates = []
sort_idx = []
raw_data = []
sorted_data = []
approved = []


def get_number_of_rows(file_):
    '''возвращает количество строк в файле csv'''
    with open(file_) as file:
        return len(list(csv.reader(file)))


def get_raw_data(file_):
    '''
    в переменную raw_data записывает каждую строку файла csv в виде списка
    '''
    global raw_data
    raw_data = []
    with open(file_) as file:
        for i in range(get_number_of_rows(file_)):
            reader = csv.reader(file, delimiter='#')
            raw_data.append(next(reader))
    raw_data.pop(0)
    get_sort(file_)


def get_sort(file_):
    '''
    в переменную sort_idx записывает правильный порядок индексов
    '''
    global sort_idx
    sort_idx = []
    with open(file_) as file:
        reader = csv.reader(file, delimiter='#')
        next_row = next(reader)

        right_row_idx = []
        for a in next_row:
            right_row_idx.append(base[a])
        sort_idx = right_row_idx
    sort_data()


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
    '''
    15 должно остаться
    '''
    for candidate in sorted_data:
        if 20 <= int(candidate[3]) or int(candidate[3]) >= 59:
            if 150 <= int(candidate[4]) and int(candidate[4]) <= 190:
                if float(candidate[6]) == 1.0:
                    if candidate[7] == 'Master' or candidate[7] == 'PhD':
                        if candidate[8] == 'true':
                            approved.append(candidate)


def sort_approved():
    '''
    сортрует допущенных в соответствии с правилами
    приоритет от 27 до 37 лет
    далее по алфавиту имя+фамилия
    после сортировки изменяет их id по порядку
    '''
    global approved
    candidates_in_age = []
    candidates_out_age = []
    for candidate in approved:
        if int(candidate[3]) >= 27 and int(candidate[3]) <= 37:
            candidates_in_age.append(candidate)
        else:
            candidates_out_age.append(candidate)
    candidates_in_age = sorted(candidates_in_age, key=lambda d: (d[1], d[2]))
    candidates_out_age = sorted(candidates_out_age, key=lambda d: (d[1], d[2]))
    approved = candidates_in_age + candidates_out_age
    for idx, candidate in enumerate(approved, 1):
        candidate[0] = idx


def write_to_file():
    with open('result.csv', 'w+', newline='') as file:
        writer = csv.writer(file, delimiter='#')
        for element in approved:
            writer.writerow([element[0],
                             element[1],
                             element[2],
                             element[4],
                             element[5],
                             element[7],
                             ])


for path in FILES:
    get_raw_data(path)
qualify()
sort_approved()
write_to_file()
