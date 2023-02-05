import random

from numpy import number


# custom lengthList
def lenList(array):
    count = 0
    for c in array:
        count += 1
    return count


# custom sumList
def sumList(array):
    sum_list = 0
    for i in array:
        sum_list += i
    return sum_list


# custom maxList
def maxList(array):
    maximum = array[0]
    for i in array:
        if maximum < i:
            maximum = i
    return maximum


# methodsFunc
def methodsList():
    custom_List = []
    length = int(input("enter the length of the future list: "))
    if length == 0:
        return []
    match input("Filling in randomly or manually: (r or m) "):
        case "r":
            custom_List = [random.randint(0, 10) for _ in range(0, length)]
        case "m":
            while len(custom_List) < length:
                elem = input()
                if elem.isdigit():
                    custom_List.append(int(elem))
                else:
                    print("It`s not a number!")
                    return {"List": custom_List}
        case _:
            print("Error!")
    print("List: ", custom_List)
    indexMaximum = custom_List.index(max(custom_List))
    srZn: float = sum(custom_List) / len(custom_List)
    i = indexMaximum + 1
    while i < len(custom_List):
        if custom_List[i] < srZn:
            del custom_List[i]
        else:
            i += 1
    return {'List:': custom_List, 'maximum': max(custom_List), 'indexMax': indexMaximum, 'arithmetic mean': srZn}


# customMethods
def customList():
    custom_List: list = []
    length: int = int(input("enter the length of the future list: "))
    if length == 0:
        return []
    match input("Filling in randomly or manually: (r or m) "):
        case "r":
            custom_List = [random.randint(0, 10) for _ in range(0, length)]
        case "m":
            while lenList(custom_List) < length:
                elem: str = input()
                try:
                    custom_List += [int(elem)]
                except Exception as e:
                    print("It`s not a number!")
                    return {"List": custom_List}
        case _:
            print("Error!")
    print("List: ", custom_List)
    srZn: float = sumList(custom_List) / lenList(custom_List)
    i: int = custom_List.index(maxList(custom_List)) + 1
    while i < lenList(custom_List):
        if custom_List[i] < srZn:
            custom_List = custom_List[:i] + custom_List[i + 1:]
        else:
            i += 1
    return {'List:': custom_List, 'maximum': maxList(custom_List), 'indexMax': custom_List.index(maxList(custom_List)), 'arithmetic mean': srZn}


match input("Methods or Custom? (m or c): "):
    case "c":
        print(customList())
    case "m":
        print(methodsList())
    case _:
        print("Error!")