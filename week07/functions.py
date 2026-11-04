# Disclosure - I used AI to help me understand the bugs and errors for the broken code exercise 5. But it did not fix it for me. It broke it down for me and told me what was wrong and why. 

# Self Assesment Questions 

# Question 1

# In exercise 5 the first bug I spotted was the syntaxerror because of a missing colon to start off the loop intructions.
# I found it by using the python traceback and allowing the code to run to then tell me what line was causing the error. 
# I did use AI but only to explain why it was wrong but not to find it. Finding it became easy with traceback. 


# Question 2

# The apply_discount(price, tier) function calculates a lower price for customers. The inputs are that it takes numbers and then provides a discount on a certain level like bronze, silver, or gold. 
# It returns a single number value that states the final discount of price based on its level. 
# Yes a colleage could use this function without having to read the initial code because it is very simple and easy to understand just by plugging in their respective inputs. 


# Question 3

# I used an AI assistant to help explain to me why an error occurred but did not use it to fix the broken code for me. The AI built my understanding and actually broke down why the error happened and why they usually happen.
# It also helped me understand how different scenarios call for different placements of code. 























# --- Exercise 1 ---

# Defining a function
def calculate_tax (price,rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Exercise 2 --- 

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price 

# Calling the function with different tiers

original_price = 200

for tier in ["gold","silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")
    

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price * tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold) = ${final_price(200, 0.07 , 'gold'):.2f}")

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders: 
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# --- Exercise 6 ---

x = 100 # global x data

def double_it():
    x = 999 # local x 
    return x * 2 


print(x)
print(double_it())
print(x)


# -- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Comments 

# The first error appeared because line 10 was missing a colon at the end of the line. To fix this I placed a colon at the end of line 10. 
# The colon was needed in order to to start the for loop and tell python the instructions in the loop are ready to start. The colon marks the beginning of the loop's instructions.

# The second error happened because python was trying to run the loop while i was less than or equal to the number of items in the list. 
# This was a problem because the pyhton list indexes start at 0, and it allowed the loop to continue when i equaled the number of items. 
# The fix was to stop the loop before i reached an inavlid index that would cause the error.