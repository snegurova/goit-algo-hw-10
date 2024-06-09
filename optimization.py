"""Module providing a function optimizing production."""
import pulp

# Створення проблеми максимізації
prob = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Цільова функція
prob += lemonade + fruit_juice, "Total Drinks"

# Обмеження
prob += 2 * lemonade + fruit_juice <= 100, "Water Constraint"
prob += lemonade <= 50, "Sugar Constraint"
prob += lemonade <= 30, "Lemon Juice Constraint"
prob += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання проблеми
prob.solve()

# Виведення результатів
print("Статус:", pulp.LpStatus[prob.status])
print("Кількість Лимонаду:", pulp.value(lemonade))
print("Кількість Фруктового соку:", pulp.value(fruit_juice))