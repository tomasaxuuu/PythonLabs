import random


# функция нахождения длины списка
def lenList(array):
    count = 0
    for c in array:
        count += 1
    return count


# реализация варианта готовыми методами
def methodsList():
    customList = []
    length = int(input("enter the length of the future list: "))
    match input("Filling in randomly or manually: (r or m) "):
        case "r":
            customList = [random.randint(0, 10) for _ in range(0, length)]
        case "m":
            while len(customList) < length:
                elem = input()
                if elem.isdigit():
                    customList.append(int(elem))
                else:
                    print("It`s not a number!")
                    return {"List": customList}
        case _:
            print("Error!")
    print("List: ", customList)
    indexMaximum = customList.index(max(customList))
    srZn: float = sum(customList) / len(customList)
    i = indexMaximum + 1
    while i < len(customList):
        if customList[i] < srZn:
            del customList[i]
        else:
            i += 1
    return {'List:': customList, 'maximum': max(customList), 'indexMax': indexMaximum, 'arithmetic mean': srZn}


# реализация варианта в ручную
def customList():
    customList = []
    s = 0
    maxEl = 0
    indexMax = 0
    length = int(input("enter the length of the future list: "))
    match input("Filling in randomly or manually: (r or m) "):
        case "r":
            customList = [random.randint(0, 10) for _ in range(0, length)]
        case "m":
            while lenList(customList) < length:
                elem = input()
                if elem.isdigit():
                    customList += [int(elem)]
                else:
                    print("It`s not a number!")
                    return {"List": customList}
        case _:
            print("Error!")
    print("List: ", customList)
    for i in range(0, len(customList)):
        s += customList[i]
        if maxEl < customList[i]:
            maxEl = customList[i]
            indexMax = i
    srZn = s / lenList(customList)
    i = indexMax + 1
    while i < lenList(customList):
        if customList[i] < srZn:
            customList = customList[:i] + customList[i + 1:]
        else:
            i += 1
    return {'List:': customList, 'maximum': maxEl, 'indexMax': indexMax, 'arithmetic mean': srZn}


match input("Methods or Custom? (m or c): "):
    case "c":
        print(customList())
    case "m":
        print(methodsList())
    case _:
        print("Error!")
