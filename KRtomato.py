class Tomato:

    # Статические cвойства - стадии созревания томатов
    stages = {"0": "томат высажен", "1": "томат цветет", "2": "томат зреет", "3": "томат созрел!"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_stage()

    # проверка созревания томата
    def is_ripe(self):
        if self._stage == 3:
            print("томат созрел!")
        else:
            print("томат зреет")

    def _change_stage(self):
        if self._stage < 3:
            self._stage += 1
        self._print_stage()

    def _print_stage(self):
        print(f"Tomato {self._index} is {Tomato.stages[self._stage]}")


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num-1)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли томаты созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    # Выдаем садовнику саженец
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за саженцем
    def work(self):
        print("Садовник работает...")
        self._plant.grow_all()
        print("Садовник закончил работу")

    # Собираем урожай, если все томаты созрели
    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Сбор урожая завершен")
        else:
            print("Слишком рано! Томат еще не созрел")

    # Статический метод,выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''В идеале время сбора урожая томатов должно наступить, когда плод достиг равномерной окраски.
        Это предотвращает расщепление и позволяет в определенной мере контролировать процесс созревания''')

    # Тесты
    if __name__ == "__main__":
        Gardener.knowledge_base()
        great_tomato_bush = TomatoBush(4)
        gardener = Gardener("Viktar", great_tomato_bush)
        gardener.work()
        gardener.work()
        gardener.harvest()
        gardener.work()
        gardener.harvest()



