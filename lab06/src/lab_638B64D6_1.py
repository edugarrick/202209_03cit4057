class ClassManual: 

    def __init__(self,name,leg_count): 

    def eat(self): 
        
    def walk(self): 

    def show_genome(self):

    def __cellsplit(self):

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
