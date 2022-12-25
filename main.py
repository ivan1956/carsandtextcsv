import csv

modelList = [
    "BMW",
    "VAZ",
    "Jeep",
    "Chevrolet",
    "Lexus",
    "Infiniti",
    "Volvo",
    "Audi"
]
priceList = [
    6034900,
    1627300,
    3928700,
    3145200,
    3096900,
    2961500,
    2351100,
    2338500
]


# Функция создающая словарь из списков
def createDict(a, b):
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = b[i]
    return dict


# Функция создающая CSV файл из словаря
def createCSV(path, dict):
    writer = csv.writer(open(path, 'w', newline=''))
    for i in range(len(dict)):
        keys = list(dict.keys())
        values = list(dict.values())
        writer.writerow([keys[i], values[i]])


# Функция, возвращающая количество выбранных букв в тексте
def getCharacters(path, symbol):
    counter = 0
    with open(path, 'r', encoding='utf-8') as file:
        for i in file.read():
            if i == symbol:
                counter += 1
    f.close()
    return counter


# Вывод в консоль словаря
print(createDict(modelList, priceList))

# Вывод в консоль CSV
createCSV('ff.csv', createDict(modelList, priceList))
with open('ff.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Вывод в консоль количества букв 'и' в файле txt
print(getCharacters('Байкал.txt', 'и'))