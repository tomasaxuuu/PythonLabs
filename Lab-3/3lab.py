import csv
import os
from datetime import datetime
from csv import DictWriter


def countFilesInDir(path):
    print(f'Кол-во файлов в директории {path} = {sum(len(files) for _, _, files in os.walk(path))}')


def readCsv(path):
    with open(path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


def writeCsv():
    field_names = ['number', 'width', 'longitude', 'temperature', 'date']
    lines = {'number': int(input("number: ")), 'width': int(input("width: ")), 'longitude': int(input("longitude: ")),
             "temperature": int(input("temperature: ")), 'date': input("date (format(%Y-%m-%d %H:%M): ")}

    with open('data.csv', 'a+', newline='') as f:
        writer = DictWriter(f, fieldnames=field_names)
        writer.writerow(lines)
    print('\ndata.csv:\n')
    f.close()
    readCsv('data.csv')


def sorting(typeBySort):
    with open('data.csv', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        match typeBySort:
            case '1':
                sortedlist = sorted(reader, key=lambda x: int(x['number']), reverse=False)
            case '2':
                sortedlist = sorted(reader, key=lambda row: datetime.strptime(row['date'], "%Y-%m-%d %H:%M"),
                                    reverse=False)
            case '3':
                sortedlist = filter(lambda row: int(row['number']) >= 10, reader)
            case _:
                print('Error')
        with open('final.csv', 'w') as outcsv:
            # configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['number', 'width', 'longitude', 'temperature', 'date'])
            for item in sortedlist:
                # Write item to outcsv
                writer.writerow([item['number'], item['width'], item['longitude'], item['temperature'], item['date']])
        readCsv('final.csv')


match input("What are you want to do?\n1 - Output count files in dir\n2 - Output a data from .csv\n"
            "3 - Write a new record in .csv\n4 - Let`s Sort!!!\n"):
    case '1':
        countFilesInDir(input("Enter name of directory: "))
    case '2':
        readCsv('data.csv')
    case '3':
        writeCsv()
    case '4':
        sorting(input("Выберите тип сортировки:\n1 - Сортировка по номеру записи (integer)"
                      "\n2 - Сортировка по дате\n3 - сортировка по критерию\n"))
