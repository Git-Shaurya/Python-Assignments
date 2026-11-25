def calculate_calories(carbs, fat, protein):
    return carbs * 4 + fat * 9 + protein * 4

carbs = float(input("Enter grams of carbohydrates: "))
fat = float(input("Enter grams of fat: "))
protein = float(input("Enter grams of protein: "))

total = calculate_calories(carbs, fat, protein)

print("Total calorie intake:", total)