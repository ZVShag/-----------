'''
Создать базовый класс «Животное» и производные
классы «Тигр», «Крокодил», «Кенгуру». С помощью конструктора установить
 имя каждого животного и его характеристики. Создайте для каждого класса необходимые
методы и поля.
'''
class Animal():
    def __init__(self,name):
        self.name=name
        self.vid='animal'
        self.__age()
        self.__ves()
    def __age(self):
        while True:
            try:
                age=int(input('Введите возраст:'))
                if age>0 and age<200:
                    self.__age=age
                    break
            except:
                print('Неверно введен возраст!')  
    def __ves(self):
        while True:
            try:
                ves=int(input('Введите вес:'))
                if ves>0 and ves<1000:
                    self.__ves=ves
                    break
            except:
                print('Неверно введен вес!') 

    def info(self):
        print( f'Имя: {self.name}, вид: {self.vid}, возраст: {self.__age}, вес: {self.__ves}')

class Tiger(Animal):
    def __init__(self,name,area,okras):
        super().__init__(name)
        self.vid='Tiger'
        self.area=area
        self.okras=okras

    def info(self):
        super().info()
        print(f'Ареал обитания: {self.area}, окрас: {self.okras}')

class Crocodile(Tiger):
    def __init__(self,name,area,okras,diametr):
        super().__init__(name,area,okras)
        self.diametr=diametr
        self.vid='Crocodile'
        
    def info(self):
        super().info()
        print(f'Диаметр яйца в кладке: {self.diametr}')

a=Crocodile('Bobik','Nill','Зеленый',10.5)
a.info()
