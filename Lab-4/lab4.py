import csv
from datetime import datetime


class Record():
    def __init__(self, number: int, width: int, longitude: int, temperature: int, date: datetime):
        self.number = number
        self.width = width
        self.longitude = longitude
        self.temperature = temperature
        self.date = date

    def __str__(self):
        return f"'number': '{self.number}', 'width': '{self.width}, 'longitude': '{self.longitude}, " \
               f"'temperature': '{self.temperature}, 'date': '{self.date}'"

    def __repr__(self):
        return {'number': {self.number}, 'width': {self.width}, 'longitude': {self.longitude},
                "temperature": {self.temperature}, 'date': {self.date}}

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class DataFile(Record):
    def __init__(self, path):
        self.path = path
        self.data = self.read(self.path)

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        return next(self.s)

    # перегрузка метода __str__ для вывода данных из файла
    def __str__(self):
        return '' + '\n'.join([str(row) for row in self.data])

    def __repr__(self):
        return '' + '\n'.join([repr(row) for row in self.data])

    def __getitem__(self, item):
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    @staticmethod
    def read(path) -> list:
        sort = []
        with open(path, "r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sort.append(row)
        return sort

    # @staticmethod
    # def save(path, data):
    #     field_names = ['number', 'width', 'longitude', 'temperature', 'date']
    #     lines = {'number': int(input("number: ")), 'width': int(input("width: ")),
    #              'longitude': int(input("longitude: ")),
    #              "temperature": int(input("temperature: ")), 'date': input("date (format(%Y-%m-%d %H:%M): ")}
    #
    #     with open(path, 'a+', newline='') as f:
    #         writer = csv.DictWriter(f, fieldnames=field_names)
    #         writer.writerow(lines)

    def sorting(self, typeSorting):
        match typeSorting:
            case '1':
                self.data = sorted(self.data, key=lambda row: int(row['number']), reverse=False)
            case '2':
                self.data = sorted(self.data, key=lambda row: datetime.strptime(row['date'], "%Y-%m-%d %H:%M"),
                                   reverse=False)
            case '3':
                self.data = list(filter(lambda row: int(row['number']) > 3, self.data))

        print("\nСортировка окончена\n")

    def add_new(self, number, width, longitude, temperature, date):
        self.data.append(Record(number, width, longitude, temperature, date))
        # self.save(self.path, self.data)


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
print("\nНачальные данные (__repr__):\n", repr(data), sep='\n')
print("\nНачальные данные (__str__):\n", data, sep='\n')

# сортировка
print('\n')
data.sorting(input("Выберите тип сортировки:\n1 - Сортировка по номеру записи (integer)"
                   "\n2 - Сортировка по дате\n3 - сортировка по критерию\n"))

# с помощью итератора выводим новые данные
for row in data:
    print(row)

data.add_new(10, 20, 30, 40, '2000-12-12 23:20')
print("\n")
for row in data:
    print(row)
print(data.__getitem__(int(input("Enter number of elem: "))))