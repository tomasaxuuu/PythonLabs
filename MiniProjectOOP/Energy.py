class Energy:

    def __init__(self, nameEnergy: str = '', volumeEnergy: float = 0, countryEnergy: str = ''):
        self.nameEnergy = nameEnergy
        self._volume = volumeEnergy
        self.country = countryEnergy

    # два метода, которые мы переопредилили в дочернем классе
    def choice(self):
        print(f"Hi, bro! Your choice: {self.nameEnergy} with volume: {self._volume} and country is: {self.country}")

    def priceEnergy(self, price):
        return price

    def _is_enoughDrink(self, price):
        if self._volume * 2 >= price / 100 and self._volume > 0.4:
            print(f"Осталось: {price - self._volume * 3} мл напитка")
            return True
        print('Осталось недостаточно напитка')
        return False


