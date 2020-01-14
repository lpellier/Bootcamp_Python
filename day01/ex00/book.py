import time
from recipe import Recipe
from recipe import check_error
from recipe import InputError

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def __str__(self):
        txt = ""
        txt += "name = " + self.name + ", last_update = " + self.last_update + ", creation_date = " + self.creation_date + ",\nrecipes_list = ("
        for keys in self.recipes_list:
            txt += keys + '('
            for values in self.recipes_list.get(keys):
                txt += values
                txt += ', '
            txt == ','
            txt += ')'
        txt += ')'
        return (txt)

    def get_recipe_by_name(self, name):
        for keys in self.recipes_list:
            for values in self.recipes_list.get(keys):
                if values == name:
                    print(name)

    def get_recipe_by_types(self, recipe_type):
        for keys in self.recipes_list.keys():
            if keys == recipe_type:
                for values in self.recipes_list.get(keys):
                    print(values)

    def add_recipe(self, recipe):
        if check_error(recipe) == 0:
            self.recipes_list.setdefault(recipe.recipe_type, []).append(recipe)
            last_update = time.ctime()

def error_check(book):
    if type(book.name) != str:
        return ("The name is supposed to be a string.")
    elif type(book.last_update) != str:
        return ("The name is supposed to be a string.")
    elif type(book.creation_date) != str:   
        return ("The name is supposed to be a string.")
    elif type(book.recipes_list) != list:
        return ("The recipes list is supposed to be a list.")
    else:
        return 0

if __name__ == "__main__":
    message = error_check(book)
    if message != 0:
        error = InputError(message)
        to_print = 'Invalid input.\n' + str(error)
        print(to_print)
        exit(0)

