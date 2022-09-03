# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def list_sorting(self, reverse: bool = False):
        return sorted(self.lst, reverse=reverse)


if __name__ == "__main__":
    sorting_class = SomeClass()
    print(sorting_class.list_sorting(True))