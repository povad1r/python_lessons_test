class Product:
    def __init__(self, name, calories_per_100g, protein_per_100g, fat_per_100g, carbs_per_100g):
        self.name = name
        self.calories_per_100g = calories_per_100g
        self.protein_per_100g = protein_per_100g
        self.fat_per_100g = fat_per_100g
        self.carbs_per_100g = carbs_per_100g

class Meal:
    def __init__(self):
        self.products = []

    def add_product(self, product, grams):
        self.products.append((product, grams))

    def calculate_total_calories(self):
        total_calories = 0
        for product, grams in self.products:
            total_calories += (grams / 100) * product.calories_per_100g
        return total_calories

    def display_meal_contents(self):
        print("Склад страви:")
        for product, grams in self.products:
            print(f"{product.name}: {grams} грам | Калорії: {int((grams / 100) * product.calories_per_100g)} кілокалорій")
