class Animals:
    def __init__(self, views, name):
        self.views = views
        self.name = name


class Dog(Animals):
    def __init__(self, name):
        super().__init__(views='dog', name=name)
        self.dog_color = 'dark brown'

    def dog_barking(self):
        return f"{self.name} makes 'Woof'"


dog = Dog('Charli')


class Cat(Animals):
    def __init__(self,  name):
        super().__init__(views='cat', name=name)
        self.cat_color = 'white'

    def cat_sharpens_claws(self):
        return f"{self.name} sharpens its claws"


cat = Cat('Barsik')


class Elephant(Animals):
    def __init__(self, name):
        super().__init__(views='elephant', name=name)
        self.elephant_color = 'grey'

    def elephant_pick_up_the_food(self):
        return f"{self.name} picks up food"


elephant = Elephant('Fin')

print(dog.dog_barking())
print(cat.cat_sharpens_claws())
print(elephant.elephant_pick_up_the_food())

