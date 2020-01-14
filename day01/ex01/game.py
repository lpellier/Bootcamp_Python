class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = True

    def __str__(self):
        if self.is_alive == True:
            string = "is alive!"
        else:
            string = "is dead :'("
        return ("first name is " + self.first_name + " and " + string)

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def __dict__(self):
        return('first name = ' + self.first_name + ', family name = ' + self.family_name + ', is_alive = ' + str(self.is_alive) + ', house_words = ' + self.house_words)

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

if __name__ == "__main__":
    arya = Stark("arya")
    print (arya.__dict__())
    arya.die()
    print (arya.__dict__())
