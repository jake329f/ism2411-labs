""" Self-Reflection Questions:
1. In Exercise 5, the first error I saw was the lack of a colon and I figured that out through saying the code out loud. For me, it is more helpful to hear myself explain it, because if it does not sound right, I can 
catch it a little quicker.
2. apply_discount(price, tier) looks at the price of the item. Based off that price level, it gets put into a certain tier and certain percentage is taken off,
which is the application of this discount. 
3. I used AI for Exercise 5, to help understand and break down the meanings of the errors in the broken code so that it could be fixed.  """


# Exercise 1

#Defining the function
def calculate_tax(price, rate):
    return price * rate

#Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 ar 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2

# Defining a function with multiple parameters
def apply_discount(price,tier):
    if tier == "gold":
        return price * 0.85 #15% discount
    elif tier == "silver":
        return price * 0.90 #10% discount
    elif tier == "bronze":
        return price * 0.95 #5% discount
    else:
        return price #No discount

#Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Calling the final_price funciton
print(f"final_price(200, 0.07, 'gold') = {final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold' ), (150, 'silver'), (80, 'silver'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

#Exercise 5
"Error #1: At the end of 'for sale in sales, there is no colon. But it is necessary to make it a working function. The colon signifies that is is a for loop function."
"It is also able to be determined that it is correct if the next line is indented."
"Error #2: For the print(sales[i]) piece of code, the index is not curerntly in the scope of the previous code. Python starts with the number 0, not with 1."
"Because of this, everything is pushed up when it needs to be brought back to match up."
" Error #3: In the first portion of code, total is set equal to sales. Also, total was set to 0. Because of this equal sign, it simply replaces each total as they come in"
"rather than adding the different totals together to get one number. By adding a plus sign to the equal sign so it is +=, they will start being added together and will resolve"
"the issue.'"