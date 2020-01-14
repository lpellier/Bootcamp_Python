class InputError(Exception):
    def __init__(self, message):
        self.message = message
        self.errors = "InputError"
                       
    def __str__(self):
        return (self.message)

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        cook_lvl = str(self.cooking_lvl)
        ingr = "("
        for i in range(len(self.ingredients)):
            ingr += self.ingredients[i]
            if i != len(self.ingredients) - 1:
                ingr += ', '
        ingr += ')'
        txt =  'Recipe (name = ' + self.name + ', cooking_lvl = ' +  cook_lvl + ', cooking time = ' + str(self.cooking_time) + ', \ningredients = ' + ingr + ', recipe_type = ' + self.recipe_type + ')'
        return txt

def check_error(recipe):
    typ = recipe.recipe_type
    if type(recipe.name) != str:
        return("The name is supposed to be a string.")
    elif type(recipe.cooking_lvl) != int or recipe.cooking_lvl > 5 or recipe.cooking_lvl < 1:
        return ("The cooking level is supposed to be an integer between 1 and 5.")
    elif type(recipe.cooking_time) != int or recipe.cooking_time < 0:
        return ("The cooking time is supposed to be a positive integer.")
    elif type(recipe.ingredients) != list or type(recipe.ingredients[0]) != str:
        return ("The ingredients list is supposed to be a list of strings.")
    elif type(recipe.description) != str:
        return ("The description is supposed to be a string.")
    elif typ != "starter" and typ != "lunch" and typ != "dessert":
        return("The recipe type is either starter, lunch or dessert")
    else:
        return (0)

if __name__ == "__main__":
    message = check_error(recipe)
    if message != 0:
        error = InputError(message)
        to_print = 'Invalid input.\n' + str(error)
        print(to_print)
        exit(0)
