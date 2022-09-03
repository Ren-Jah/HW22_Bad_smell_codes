# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord, y_coord, movement_mode):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.movement_mode = movement_mode

    def _calculation_speed(self):
        """ Расчет скорости в зависимоти от режима передвижения"""
        if self.movement_mode == "default":
            self.speed = 1
        if self.movement_mode == "fly_mode":
            self.speed = self.speed * 1.2
        if self.movement_mode == "crawl_mode":
            self.speed = self.speed * 0.5
        else:
            raise ValueError('Что-то пошло не так')
        return self.speed

    def move(self, direction):
        """ Метод отвечающий за движение по направлениям"""

        speed = self._calculation_speed()

        if direction == 'UP':
            self.field.set_unit(x=self.x_coord, y=self.y_coord + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x_coord, y=self.y_coord - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x_coord - speed, y=self.y_coord, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x_coord + speed, y=self.y_coord, unit=self)

#     ...
