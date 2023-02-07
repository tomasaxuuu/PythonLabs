import csv
from collections import defaultdict
from datetime import datetime
import os


def countFilesInDir(path):
    return sum(len(files) for _, _, files in os.walk(path))


print(countFilesInDir(input("path for scanning with format(disc:\ folder) ")), 'files in this dir')

sorted_list = []


def sortByDate(pathCsv, reverse):
    with open(pathCsv + '.csv', newline='') as f:
        reader = csv.reader(f)
        sorted_list.append(next(reader))
        sorted_list.extend(
            sorted(reader, key=lambda x: datetime.strptime(x[4], "%Y-%m-%d %H:%M"),
                   reverse=False if reverse == 'n' else True)
        )
    return sorted_list


def sortByInt(pathCsv, column, reverse):
    with open(pathCsv + '.csv', newline='') as f:
        reader = csv.reader(f)
        sorted_list.append(next(reader))
        sorted_list.extend(
            sorted(reader, key=lambda x: int(x[column - 1]), reverse=False if reverse == 'n' else True)
        )
    return sorted_list


def sortByCrit(pathCsv):
    with open(pathCsv + '.csv', newline='') as f:
        reader = csv.reader(f)
        sorted_list.append(next(reader))
        for row in reader:
            if int(row[3]) >= 0:
                sorted_list.append(row)
    return sorted_list


def writeCsv(funcSorting, pathCsvSave):
    with open(pathCsvSave + '.csv', 'wt', newline='') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(funcSorting)


# try:
#     match input("Enter type by sort - Date or number or crit format(d or n or c): "):
#         case 'd':
#             writeCsv(sortByDate(input('enter name file .csv for read: '), input("want reversed? (y, n) ")),
#                      input("enter file name for save final file .csv: "))
#         case 'n':
#             writeCsv(sortByInt(input('enter name file .csv for read: '),
#                                int(input('enter number of column for sorting 1 - 4: ')),
#                                input("want reversed? (y, n) ")),
#                      input("enter file name for save final file .csv: "))
#         case 'c':
#             writeCsv(sortByCrit(input('enter name file .csv for read: ')),
#                      input("enter file name for save final file .csv: "))
#         case _:
#             print("Error")
# except Exception:
#     print("Error")
my_dict = defaultdict(list)

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        for key, value in line.items():
            try:
                my_dict[key].append(value)
            except KeyError:
                my_dict[key] = [value]
print(my_dict)
