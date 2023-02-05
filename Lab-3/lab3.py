import csv
from datetime import datetime
import os
# def countFilesInDir(path):
#     return sum(len(files) for _, _, files in os.walk(path))
#
#
# print(countFilesInDir(input("path for scanning with format(disc:\ folder) ")), 'files in this dir')

sorted_listInt = []


def sortByDate(pathCsv, reverse):
    with open(pathCsv + '.csv', newline='') as f:
        reader = csv.reader(f)
        sorted_listInt.append(next(reader))
        sorted_listInt.extend(
            sorted(reader, key=lambda x: datetime.strptime(x[4], "%Y-%m-%d %H:%M"), reverse=False if reverse == 'n' else True)
        )
    return sorted_listInt


def sortByInt(pathCsv, column, reverse):
    with open(pathCsv + '.csv', newline='') as f:
        reader = csv.reader(f)
        sorted_listInt.append(next(reader))
        sorted_listInt.extend(
            sorted(reader, key=lambda x: int(x[column - 1]), reverse=False if reverse == 'n' else True)
        )
    return sorted_listInt


def sortByCrit(pathCsv):
    with open(pathCsv + '.csv', newline='') as f:
        reader = csv.reader(f)
        sorted_listInt.append(next(reader))
        for row in reader:
            if int(row[3]) > 5 and int(row[2]) < 60:
                sorted_listInt.append(row)
    return sorted_listInt


def writeCsv(funcSorting, pathCsvSave):
    with open(pathCsvSave + '.csv', 'wt', newline='') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(funcSorting)


match input("Enter type by sort - Date or number or crit format(d or n or c): "):
    case 'd':
        writeCsv(sortByDate(input('enter name file .csv for read: '), input("want reversed? (y, n) ")), input("enter file "
                                                                                                         "name for "
                                                                                                         "save final "
                                                                                                         "file .csv "))
    case 'n':
        writeCsv(sortByInt(input('enter name file .csv for read: '), int(input('enter number of column for sorting 1 - 4: ')), input("want reversed? (y, n) ")), input("enter file "
                                                                                                         "name for "
                                                                                                         "save final "
                                                                                                         "file .csv "))
    case 'c':
        writeCsv(sortByCrit(input('enter name file .csv for read: ')), input("enter file name for save final file .csv"))
    case _:
        print("Error")