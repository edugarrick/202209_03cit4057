class ClassManual: 

    def __init__(self,name,leg_count): 
        self._name = name
        self._leg_count = leg_count

    def eat(self): 
        print("{0} is now eating".format(self._name))
        
    def walk(self): 
        print("{0} is now walking".format(self._name))

    def show_genome(self):
        self.__dna = "ACGT"
        print("{} DNA: {}".format(self._name, self.__dna))

    def __cellsplit(self):
        return self

def main():
    obj_cat=ClassManual("Cat",4)
    obj_dog=ClassManual("Dog",4) 
    obj_human=ClassManual("Human",2) 
    print("Mammal {} has {} legs.".format(
        obj_cat._name,obj_cat._leg_count)
    )
    print("Mammal {} has {} legs.".format(
        obj_dog._name,obj_dog._leg_count)
    )
    print("Mammal {} has {} legs.".format(
        obj_human._name,obj_human._leg_count)
    )

    obj_cat.eat()
    obj_dog.walk()
    obj_human.show_genome()
    obj_human.__cellsplit

if __name__ == "__main__":
    main()
