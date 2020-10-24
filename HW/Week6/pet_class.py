class pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self):
            self.name
    def get_name(self):
            return self.name

    def set_animal_type(self):
            self.animal_type
    def get_animal_type(self):
            return self.animal_type

    def se_age(self):
            self.age
    def get_age(self):
            return self.age
    def printResult(self):
        print( self.name, self.animal_type, self.age)
if __name__=="__main__":
    A = pet("dog", "poodle", 1)
    A.printResult()