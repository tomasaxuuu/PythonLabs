from Labs.MiniProjectOOP.Energy import Energy
from Labs.MiniProjectOOP.Monster import MonsterEnergy


def importType():
    importTypeEn = input("Ваш напиток из другой страны? (y, любая другая клавиша): ")
    return True if importTypeEn == 'y' else False


def userChoice():
    match importType():
        case True:
            # Экземпляр класса
            monster = MonsterEnergy('Monster', 0.5, 'USA', 1)
            # устанавливаем цену
            monster.priceEnergy(int(input("Введите стоимость напитка: ")))
            # получаем id
            monster.get_id()
            # сеттер (присваиваем тип для напитка)
            monster.setType(input("Введите вид вашего монстра: "))
            monster.choice(monster.getType, True)
        case False:
            # Экземпляр класса
            defaultEnergy = Energy('Tornado', 0.449, 'Russia')
            # метод для вывода энергетика
            defaultEnergy.choice()
            # метод получения остатка напитка
            defaultEnergy._is_enoughDrink(defaultEnergy.priceEnergy(50))


if __name__ == "__main__":
    userChoice()
