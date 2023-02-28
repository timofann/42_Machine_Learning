cookbook = {
    'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                 'meal': 'lunch',
                 'prep_time': '10'},
    'cake':     {'ingredients': ['flour', 'sugar', 'eggs'],
                 'meal': 'dessert',
                 'prep_time': '60'},
    'salad':    {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                 'meal': 'lunch',
                 'prep_time': '15'}
}


def print_recipe(name):
    if isinstance(name, str) and cookbook.get(name):
        print(f"Recipe for {name}:\n\
        \r\rIngredients list: {cookbook[name]['ingredients']}\n\
        \r\rTo be eaten for {cookbook[name]['meal']}.\n\
        \r\rTakes {cookbook[name]['prep_time']} minutes of cooking.")
    else:
        print("There is no such recipe.")


def delete_recipe(name):
    if isinstance(name, str) and cookbook.get(name):
        cookbook.pop(name)
    else:
        print("There is no such recipe.")


def add_a_new_recipe(name, ingredients, meal, prep_time):
    if isinstance(name, str) and \
            not cookbook.get(name) and \
            isinstance(ingredients, list) and len(ingredients) != 0 and \
            sum(isinstance(i, str) for i in ingredients) == len(ingredients) and \
            isinstance(meal, str) and \
            isinstance(prep_time, str) and prep_time.isdigit():
        cookbook[name] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time
        }
    else:
        print("Can't add this recipe, sorry.")


def print_all_recipe_names():
    for key in cookbook:
        print(key)


actions_list = """\
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
"""

error_msg ="""\
This option does not exist, please type the corresponding number.
To exit, enter 5"""

actions_dict = {
    '1': lambda: add_a_new_recipe(input("Recipe's name: "),
                                    input("Ingredients (use ' ' to divide): ").split(),
                                    input("Meal type: "),
                                    input("Preparation time: ")) or print(),
    '2': lambda: delete_recipe(input("Please enter the recipe's name to delete: ")) or print(),
    '3': lambda: print_recipe(input("Please enter the recipe's name to get its details: ")) or print(),
    '4': lambda: print_all_recipe_names(),
    '5': lambda: print('Cookbook closed.'),
}


if __name__ == '__main__':
    instr = 'start'
    while instr != '5':
        instr = input(actions_list)
        print()
        f = actions_dict.get(instr)
        f() if f else print(error_msg)

