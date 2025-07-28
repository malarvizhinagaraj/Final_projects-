def convert_measurement(amount, from_unit, to_unit):
    conversions = {
        ('cup', 'ml'): 240,
        ('tbsp', 'ml'): 15,
        ('tsp', 'ml'): 5
    }
    return amount * conversions.get((from_unit, to_unit), 1)

def calculate_nutrition(ingredients):
    return {
        "calories": 200,
        "fat": "10g",
        "protein": "5g"
    }
