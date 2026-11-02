""" 
1. Prior to lists, I felt that code was very strict in their rules, and what happens is more set in stone than I thought. However,
after using lists and creating them, it makes python feel more flowy and allows more room for error because of how easily changeable
they are. 
2. In my previous job at a law office, I was in charge monthly to create lists of expenses for each case that required them. I had to use
excel and it would sometimes take hours to complete it. However, with these lists, it would be easier to process them. """



# Exercise 1: Built a List

print("--- Exercise 1; Built a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)

# Exercise 3

print("--- Exercise 3: List Slicing ---")
print(inventory[:3]) 
print(inventory[-2:])
print(inventory[::2])

# Exercise 4

print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) #NYC Coords

try: 
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

# Exercise 6

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of sales: {count}")
print(f"Average Sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sales: {min(sales)}")

best = sales[0]
worst = sales [0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best Sale (loop): {best}")
print(f"Worst Sale (loop): {worst}")

# Exercise 7

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8
print("--- Exercise 8: Filter ---")

sales = [340, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/ len(high_sales):.2f}")