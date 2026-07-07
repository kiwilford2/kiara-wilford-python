#Lesson 1

name = "Kiara"
age = 36
print("name:", name)
print("age:", age)
print(name, "is", age)

###########################################################################################

age = input("Enter your age: ")
age = int(age)            # Convert the string to an integer
next_year = age + 1
print("Next year you will be", next_year)

###########################################################################################
total = 20 +10
print(total)

remainder = 20 % 15
print(remainder)

squared = 8 ** 2
print(squared)

#############################################################################################

print("=== Greeting Card Generator ===")
print()                               # print() with nothing inside prints a blank line

name = input("Who is this card for? ")
occasion = input("What's the occasion? (birthday, graduation, etc.) ")
sender = input("Who is it from? ")

name = name.strip().upper()       # Chaining: strip() runs first, then upper() runs on the result
occasion = occasion.strip().lower()
sender = sender.strip().upper()

print()
print("╔══════════════════════════════╗")
print(f"   Happy {occasion}, {name}!")
print()
print("   Wishing you all the best.")
print(f"   — {sender}")
print("╚══════════════════════════════╝")

########################################################################################################3
#TIP CALCULATOR

bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")

bill = float(bill)
tip_rate = float(tip_rate)

tip_amount = bill * (tip_rate/100)
total = bill + tip_amount

print(f"Tip: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")


print("====================")
print("  TIP CALCULATOR"    )
print("====================")
print(f"Bill:       ${bill:.2f}")
print(f"Tip:        ${tip_amount:.2f}")
print(f"Total:      ${total:.2f}")
print("====================")


What was the bill amount? $80
What tip percentage? 50
Tip: $40.00
Total: $120.00
====================
  TIP CALCULATOR
====================
Bill:       $80.00
Tip:        $40.00
Total:      $120.00
====================
################################################################################################


name = "Jazmine"
print(f"Hello, {name}!")
age = input("How old are you? ")
next_year = int(age) + 1
print(f"Next year you will be {next_year}")
