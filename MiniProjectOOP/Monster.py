from Labs.MiniProjectOOP.Energy import Energy


# Наследованный класс от базового Energy
class MonsterEnergy(Energy):

    # private field
    __type = ''

    def __init__(self, name: str = '', volume: float = 0, country: str = '', idEn: int = 0):
        super().__init__(name, volume, country)
        self._id = idEn

    # property
    @property
    def getType(self):
        return self.__type

    # Полиморфизм
    def choice(self, typeMonster: str = '', importEn: bool = ''):
        print(f"Hi, bro! Your choice: {self.nameEnergy, typeMonster} with volume: {self._volume} and country is: {self.country}, "
              f"import = {importEn} ")

    # Полиморфизм
    def priceEnergy(self, price: int = 0):
        print("Price is so big" if price > 10 else "Price is so small")

    def get_id(self):
        print(f"Id your energy: {self.nameEnergy} = {self._id}")

    def setType(self, typeMonster: str = ''):
        self.__type = typeMonster
