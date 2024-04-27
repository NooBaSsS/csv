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
        # print(right_row_idx)
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


get_sort()
get_raw_data()
sort_data()

print(sort_idx)
print(sorted_data, 'сортированные')
