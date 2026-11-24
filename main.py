price = 150
quantity = 4
total = price * quantity
print(total) # 600

result = 10 + 2 * 3 **2
# 10 + 2 * 9 
#10 + 18
print(result) # 28 

#Приклад: перетворення часу
seconds = int(input("Кількість секунд: *))
hours = seconds // 3600
minutes = seconds % 3600 //60
rest = seconds %60
print(f"{hours} год {minutes} хв {rest} сек")

#Приклад:розрахунок замовлення 
price = float(input"Ціна товару: "))
quatity = int(input("Кількість: ")

# Розрахунок вартості та знижки
total = price * quantity
discount = total * 0.10
final_price = total - discount
print(f"До сплати: {final_price:.2f} грн")

a = int(input("Перше число: "))
b = int(input("Друге число: "))
print(a + b) # для 10 і 20: 30

#Перевірка числа та діапазону
number = int(input("Число: "))
is_even = number % 2 == 0
in_range = 10 <= number <= 100
valid = is_even and in_range
print(f"Допустиме число: {valid}")
