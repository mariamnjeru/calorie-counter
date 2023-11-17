import json

meals = []
combos = []

# Read data from the JSON file
with open("Data/meals.json", "r") as file:
    data = json.load(file)
    meals = data.get("meals", [])

with open("Data/combos.json", "r") as file:
    data = json.load(file)
    combos = data.get("combos", [])

# Now, 'meals' and 'combos' lists contain the data from the JSON file
print(meals)
print(combos)


calories_dict = {meal["id"]: meal["calories"] for meal in meals}

combos_dict = {combo["id"]: combo["meals"] for combo in combos}

meal_price_dict = {meal["id"]: meal["price"] for meal in meals}

combo_price_dict = {combo["id"]: combo["price"] for combo in combos}
