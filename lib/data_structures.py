spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   return [food ["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        food_formatted = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}"
        print(food_formatted)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    mathing_cuisine = [food for food in spicy_foods if food['cuisine'] == cuisine]
    if mathing_cuisine:
        return mathing_cuisine[0]
    else:
        return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level = "🌶" * food["heat_level"]
            food_formatted = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}"
            print(food_formatted)

def get_average_heat_level(spicy_foods):
    heat_levels =[]
    for food in spicy_foods:
        heat_level = food["heat_level"]
        heat_levels.append(heat_level)

    average = sum(heat_levels) / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods