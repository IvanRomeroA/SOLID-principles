class Animal:

    def walk(self):
        print("Walk")


class LightweightAnimal(Animal):

    def jump(self):
        print("Jump")


class Elephant(Animal): ...


class Dog(LightweightAnimal): ...


def jump_hole(animal: LightweightAnimal):
    animal.walk()
    animal.jump()
    animal.walk()


elephant = Elephant()
dog = Dog()

jump_hole(dog)
