class Unit:
    def move(self, field, x_coord: int, y_coord: int, direction, fly_mode: bool, crowling_mode: bool, points_per_action=1):
        """ Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита,
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит """

        if fly_mode and crowling_mode:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly_mode:
            points_per_action *= 1.2
            if direction == 'UP':
                new_y = y_coord + points_per_action
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - points_per_action
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - points_per_action
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + points_per_action

        if crowling_mode:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = y_coord + points_per_action
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - points_per_action
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - points_per_action
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)


