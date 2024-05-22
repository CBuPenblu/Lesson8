#class Bird():
#    def __init__(self, name):
#        self.name = name
#
#    def fly(self):
#        print('bird is flying')
#
#class Pinguin(Bird):
#    pass
#
#p = Pinguin("Sarah")
#
#p.fly()

#wrong use of program because Pinguins are not flying

class Bird():
    def fly(self):
        print("this bird is flying")

class Duck(Bird):
    def fly(self):
        print("this duck flies fast")

def fly_in_the_sky(animal):
    animal.fly()


b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)