#Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
#Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
#не изменяя существующий код бойцов или механизм боя.
#Исходные данные:
#Есть класс Fighter, представляющий бойца.
#Есть класс Monster, представляющий монстра.
#Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#Шаг 1: Создайте абстрактный класс для оружия
#Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
#Шаг 2: Реализуйте конкретные типы оружия
#Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
#Каждый из этих классов реализует метод attack() своим уникальным способом.
#Шаг 3: Модифицируйте класс Fighter
#Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
#Добавьте метод changeWeapon(), который позволяет изменить оружие бойца.
#Шаг 4: Реализация боя
#Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
#Требования к заданию:
#Код должен быть написан на Python.
#Программа должна демонстрировать применение принципа открытости/закрытости:
#новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
#Программа должна выводить результат боя в консоль.
#Пример результата:
#Боец выбирает меч.
#Боец наносит удар мечом.
#Монстр побежден!
#Боец выбирает лук.
#Боец наносит удар из лука.
#Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return("hit with a sword")

class Bow(Weapon):
    def attack(self):
        return("shot from the bow")

class Axe(Weapon):
    def attack(self):
        return("hit with an axe")


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return(f"{self.name} attacks: {self.weapon.attack()}")
        else:
            return(f"{self.name} has no weapon")


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return(f"{self.name} got {damage} damage, health: {self.health}")
        else:
            return(f"{self.name} defeated!")


def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    damage = 10
    print(monster.take_damage(damage))


fighter = Fighter("Fighter")
monster = Monster("Creep", 30)

fighter.change_weapon(Sword())
battle(fighter, monster)

fighter.change_weapon(Bow())
battle(fighter, monster)

fighter.change_weapon(Axe())
battle(fighter, monster)


#Вот эту логику:
#self.health -= damage
#if self.health > 0:
#return(f"{self.name} got {damage} damage, health: {self.health}")
#else:
#return(f"{self.name} defeated!")

#Можно вынести в @property.setter декоратор здоровья.
#Условно, делаем при инициализации приватный атрибут self._health = 100.
#Затем, пишем:
#@property
#def health(self):
#return self._health

#И условия переназначения:
#@health.setter
#def health(self):
#if self._health > 0:
#return(f"{self.name} got {damage} damage, health: {self.health}")
#else:
#return(f"{self.name} defeated!")

#Таким образом, каждый раз, когда атрибут .health будет переназначаться или изменяться - проверка будет автоматической.