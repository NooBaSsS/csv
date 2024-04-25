import csv
a = {'id': 0,
     'name': 1,
     'surname': 2,
     'age': 3,
     'weight': 4,
     'height': 5,
     'eyesight': 6,
     'education': 7,
     'english_language': 8
     }
d = []
right_header = []
right_row = []

with open(r'C:\Users\DDT\Desktop\Архив\us.csv') as file:
    reader = csv.reader(file, delimiter='#')
    next_row = next(reader)

    header = next(reader)
    for c in header:
        d.append(a[c])

    for c in d:
        right_header.append(header[c])

    for i in d:
        right_row.append(next_row[i])

    print(right_header)

    print(header)
    print(next_row, 'aa')
    print(right_row, 'aaa')
