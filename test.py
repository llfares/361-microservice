import time

valid_ingredients = {'flour', 'butter', 'eggs', 'baking soda', 'chocolate chips'}

def get_recipes(ingredients):
    """Return list of recipes based on ingredients."""
    return ['chocolate chip cookies', 'sugar cookies', 'pound cake']

def validate_ingredients(ingredients):
    """Validate ingredients against the database."""
    return all(ingredient in valid_ingredients for ingredient in ingredients)

# Track if ingredients were received
ingredients_received = False

while True:
    try:
        # Read ingredients from ingredients text file
        with open('ingredients.txt', 'r') as file:
            ingredients = file.readline().strip().split(',')
            ingredients_received = True
    except FileNotFoundError:
        # If ingredients text file not found, wait and continue
        time.sleep(1)
        continue

    # Check if no ingredients received
    if not ingredients_received:
        time.sleep(1)
        continue

    # Validate ingredients
    if not validate_ingredients(ingredients):
        time.sleep(10)
        print("Error: Invalid ingredients received from the UI.")
        continue

    # Get recipes based on ingredients
    recipes = get_recipes(ingredients)

    # Write recipes to recipes text file
    with open('recipes.txt', 'w') as file:
        file.write('\n'.join(recipes))
        print("Recipes written to file.")

    # Break the loop once recipes are written
    break
