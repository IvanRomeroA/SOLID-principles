class Animal:

    def walk(self):
        print("Walk")

    def jump(self):
        print("Jump")


class Elephant(Animal):

    def jump(self):
        raise Exception("An elephant cannot jump")


def jump_hole(animal: Animal):
    animal.walk()
    animal.jump()
    animal.walk()


elephant = Elephant()

jump_hole(elephant)
