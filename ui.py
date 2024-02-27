import time

while True:
    ingredients_input = input("Enter ingredients (comma-separated) to find recipes: ")

    # Process and validate ingredients
    ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(',')]
    if not (ingredient in {'flour', 'butter', 'eggs', 'baking soda', 'chocolate chips'} for ingredient in ingredients):
        print("Error: ingredients not found.")
        continue

    # Write ingredients to ingredients text file
    with open('ingredients.txt', 'w') as file:
        file.write(','.join(ingredients))

    # Sleep for 5 seconds while recipes are written to recipes text file
    time.sleep(5)

    # Read recipes from recipes text file and print them
    try:
        with open('recipes.txt', 'r') as file:
            recipes = file.read().splitlines()
            if recipes:
                print("Recipes:")
                for recipe in recipes:
                    print(recipe)
            else:
                print("No recipes available.")
    except FileNotFoundError:
        print("No recipes available.")
