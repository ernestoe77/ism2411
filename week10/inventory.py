  

  # inventory.py
  # AUTHOR: Ernesto Espinosa
 # Module 10 lab: Inventory List Manager


# Exercise 1: Build a list 

print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)

# Exercise 3: List slicing 

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs the first three items
print(inventory[-2:])# grabs items from index 1 to 3
print(inventory[::2])



# Exercise 4

print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds an item to the end of a list
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts the list in alphabetical order
print(inventory)

# Exercise 5

print("--- Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060) # New York City coordinates 


try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")


# Exercise 6

print("--- Exercise 6: List Average Sales")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")


best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount 

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")


# Exercise 7

print("--- Exercise 7: Accumlator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount

print(prices)
print(discounted)



# Exercise 8

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # empty list 

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")




# Reflection 1:

# The most surprising thing about lists and python compared to what I expected coming in is how lists can hold many amounts of information like numbers and words. 
# I also found it pretty interesting that you do not have to give a size or length before typing and coding information and data into it. 



# Reflection 2:

# I used to work in retail and dislked always having to scan and change the price's of items during discount seasons. 
# To save time, python could be used here to turn a long hour of scans and updating numbers to a quick and easy script run that checks and updates everything based on certain conditions and price's. 