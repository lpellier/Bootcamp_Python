def del_recipe(cookbook, name):
    cookbook[name].clear()

def add_recipe(cookbook, name, ingr, meal_type, preptime):
    cookbook[name] = {
            'ingredients': ingr,
            'meal': meal_type, 
            'prep_time': preptime,
            }

def print_recipe(cookbook, name):
    ingredients = cookbook[name].get('ingredients')
    meal = cookbook[name].get('meal')
    prep_time = cookbook[name].get('prep_time')
    new = ', '.join(ingredients)
    print(name, "'s ingredients are %s." % new)
    print("it is a", meal, "and it takes", prep_time, "of preparation.")

def print_all_recipes(cookbook):
    for key in cookbook.keys():
        print_recipe(cookbook, key)
        print("\n")

def recipe():
    cookbook = {
            'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': '10 minutes',},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60 minutes',},
            'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15 minutes',},
            }
    return (cookbook)

def display_menu():
    print("Please select an option by typing the corresponding number:")
    print("1 - Add a recipe\n2 - Delete a recipe\n3 - Print a recipe\n4 - Print the cookbook\n5 - Quit")

def choice_effect(cookbook):
    print("\n")
    display_menu()
    choice = input(">> ")
    if choice == '1':
        print("To add a recipe, please type : ingredient1, ingredient2, ..., meal type(lunch, dessert ?), prep time(x minutes)")
        name = input("what is the name of your recipe ?\n")
        ingredients = input("ingredients :")
        meal = input("meal type :")
        prep_time = input("preparation time :")
        add_recipe(cookbook, name, ingredients, meal, prep_time)
    elif choice == '2':
        print("here is a list of all the recipes :")
        for keys in cookbook.keys():
            print(keys)
        name = input("what is the name of the recipe you want gone?\n")
        del_recipe(cookbook, name)
    elif choice == '3':
        print("here is a list of all the recipes :")
        for keys in cookbook.keys():
            print(keys)
        name = input("what is the name of the recipe you want to print?\n")
        print_recipe(cookbook, name)
    elif choice == '4':
        print_all_recipes(cookbook)
    elif choice == '5':
        return (0)
    choice_effect(cookbook)


if __name__ == "__main__":
    cookbook = recipe()
    if choice_effect(cookbook) == 0:
        exit(0)
