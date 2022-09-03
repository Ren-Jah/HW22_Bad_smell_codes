# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room_num, city_population):
        self.planet = Planet()
        self.room_num = room_num
        self.city_population = city_population

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

if __name__ == '__main__':
    person = Person(1408, 123456)
    print(f"Номер комнаты {person.get_person_room()}")
    print(f"Население города {person.get_city_population()} чел.")
