import csv
from datetime import datetime


# класс отдельного айтема для его инициализации в данных и выводе на экран при добавлении
class Item():
    # инициализация полей
    def __init__(self, number: int, width: int, longitude: int, temperature: int, date: datetime):
        self.number = number
        self.width = width
        self.longitude = longitude
        self.temperature = temperature
        self.date = date

    # вывод нового элемента с помощью перегрузки repr и str
    def __str__(self):
        return f"'number': '{self.number}', 'width': '{self.width}', 'longitude': '{self.longitude}', " \
               f"'temperature': '{self.temperature}', 'date': '{self.date}'"

    def __repr__(self):
        return f"'number': '{self.number}', 'width': '{self.width}', 'longitude': '{self.longitude}', " \
               f"'temperature': '{self.temperature}', 'date': '{self.date}'"


class DataFile(Item):
    def __init__(self, path):
        self.prod = None
        self.path = path
        self.data = self.read(self.path)

    # итератор
    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        return next(self.s)

    # перегрузка методов __repr__ и  __str__ для вывода данных из файла
    def __str__(self):
        return '' + '\n'.join([str(row) for row in self.data])

    def __repr__(self):
        return '' + '\n'.join([repr(row) for row in self.data])

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    # getitem для получения опредленного элемента коллекции
    def __getitem__(self, item):
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    # генератор коллекции
    def generator(self):
        self.prod = 0

        while self.prod < len(self.data):
            yield self.data[self.prod]
            self.prod += 1

    # чтение из файла
    @staticmethod
    def read(path) -> list:
        sort = []
        with open(path, "r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sort.append(row)
        return sort

    # сортировка
    def sorting(self, typeSorting):
        match typeSorting:
            case '1':
                self.data = sorted(self.data, key=lambda row: int(row['number']), reverse=False)
            case '2':
                self.data = sorted(self.data, key=lambda row: datetime.strptime(row['date'], "%Y-%m-%d %H:%M"),
                                   reverse=False)
            case '3':
                self.data = list(filter(lambda row: int(row['number']) > 3, self.data))
        # запись в файл новых данных
        with open('final.csv', 'w') as outcsv:
            # configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['number', 'width', 'longitude', 'temperature', 'date'])
            for item_1 in self.data:
                writer.writerow(
                    [item_1['number'], item_1['width'], item_1['longitude'], item_1['temperature'], item_1['date']])
        print("\nСортировка окончена. Проверьте файл final.csv!\n")

    # добавление новой записи в словарь
    def add_new(self, number, width, longitude, temperature, date):
        self.data.append(Item(number, width, longitude, temperature, date))
        appender = [number, width, longitude, temperature, date]
        with open('data-1.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(appender)
        return self.data


# создаем экземпляр класса
data = DataFile('data-1.csv')

# итератор
print("\nИтератор:\n")
for row in data:
    print(row)
print('\n')

# получение элемента через getItem
print(data.__getitem__(int(input("Enter number of elem: "))))

# вывода начальных данных файла с помощью repr и str
print("\nДанные (__repr__):\n", repr(data), sep='\n')
print("\nДанные (__str__):\n", data, sep='\n')

# сортировка
print('\n')
data.sorting(input("Выберите тип сортировки:\n1 - Сортировка по номеру записи (integer)"
                   "\n2 - Сортировка по дате\n3 - сортировка по критерию\n"))

# с помощью итератора выводим новые данные
for row in data:
    print(row)

data.add_new(int(input("\nВведите номер: ")), int(input("Введите широту: ")), int(input("Введите долготу: ")),
             int(input("Введите температуру: ")), input("Введите дату и время в формате (%Y-%M-%D %H:%m): "))

# с помощью генератора выводим данные
print('\nГенератор:')
for item in data.generator():
    print(item)
