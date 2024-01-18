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
    pass
    return [spicy_food["name"] for spicy_food in spicy_foods ]


def get_spiciest_foods(spicy_foods):
    pass
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5 ]
    # def sort_spiciness(spicy_food) :
    #     return spicy_food["heat_level"]
    #     breakpoint()
    
    # return spicy_foods.sort(key = sort_spiciness) 

def print_spicy_foods(spicy_foods):
    pass
    def print_spiciness (spicy_food) :
        return "🌶"*spicy_food['heat_level']
    for spicy_food in spicy_foods :
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {print_spiciness(spicy_food)}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for spicy_food in spicy_foods :
        if spicy_food["cuisine"] == cuisine :
            return spicy_food 

def print_spiciest_foods(spicy_foods):
    pass
    def print_spiciness (spicy_food) :
        return "🌶"*spicy_food['heat_level']
    for spicy_food in spicy_foods :
        if spicy_food["heat_level"] > 5 :
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {print_spiciness(spicy_food)}")
    

def get_average_heat_level(spicy_foods):
    pass
    all_heat_levels = [spicy_food["heat_level"] for spicy_food in spicy_foods]
    total_heat = 0
    for heat_level in all_heat_levels :
        total_heat+= heat_level
        # breakpoint()
    return total_heat/len(all_heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
