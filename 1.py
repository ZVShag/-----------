'''
Создать базовый класс «Животное» и производные
классы «Тигр», «Крокодил», «Кенгуру». С помощью 
конструктора установить имя каждого животного и его характеристики. 
Создайте для каждого класса необходимые
методы и поля.
'''

class Animal(object):
    def __init__(self,name):
        self.vid='animal'
        self.name=name
        self.__age()
        self.__ves()
       

    def __age(self):
        while True:
            try:
                age=int(input('Введите возраст:'))
                if age>0 and age<200:
                    self.age=age
                    break
            except:
                print('Неверно указан возраст')

    def __ves(self):
        while True:
            try:
                ves=int(input('Введите вес:'))
                if ves>0 and ves<200:
                    self.ves=ves
                    break
            except:
                print('Неверно указан вес')
        
    def info(self):
        with open('animal.txt','a',encoding='utf-8') as f:
            f.writelines(f'Класс:{self.vid}, имя:{self.name}, возраст:{self.age}, вес:{self.ves}\n')

class Tiger(Animal):
    def __init__(self,name,area,color):
        super().__init__(name)
        self.vid='Tiger'
        self.area=area
        self.color=color

    def info(self):
        super().info()
        with open('animal.txt','a',encoding='utf-8') as f:
            f.writelines(f'Ареал обитания:{self.area}, окрас:{self.color}\n')

class Krokidile(Tiger):
    pass
class Kenga(Animal):
    pass
a=Animal('noname')
a.info()
b=Tiger('noname','Саванна','Полосатый')
b.info()
