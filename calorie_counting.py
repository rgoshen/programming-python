burgers = {
    1: ['Cheeseburger', 461],
    2: ['Fish Burger', 431],
    3: ['Veggie Burger', 420],
    4: ['no burger', 0]
}
sides = {
    1: ['Fries', 100],
    2: ['Baked Potato', 57],
    3: ['Chef Salad', 70],
    4: ['no side', 0]
}
drinks = {
    1: ['Soft Drink', 130],
    2: ['Orange Juice', 160],
    3: ['Milk', 118],
    4: ['no drink', 0],
}
desserts = {
    1: ['Apple Pie', 167],
    2: ['Sundae', 266],
    3: ['Fruit Cup', 75],
    4: ['no dessert', 0],
}

calories = 0

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger in burgers:
    calories += burgers[burger][1]
if side in sides:
    calories += sides[side][1]
if drink in drinks:
    calories += drinks[drink][1]
if dessert in desserts:
    calories += desserts[dessert][1]

print(f'Your total Calorie count is {calories}.')
