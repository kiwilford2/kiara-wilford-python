name = "Kiara"
age = 36
height = 5.5
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


name = input("What is your name? ")
print(f"Hello! {name}")


birth_year_input = input("Enter the year you were born: ")
birth_year = int(birth_year_input)

current_year = 2026
calculated_age = current_year - birth_year
print(f"You are approximately {calculated_age} years old.")

num_1 = input("Enter a number: ")
num_2 = input("Enter a second number: ")

num_1 = float(num_1)
num_2 = float(num_2)

total = num_1 * num_2
print(f"{num_1} * {num_2} = {total}")


name = "receipt"
item = "Movie Ticket"
price = 15.00
price = float(price)
quantity = 4
total = price * quantity

print("═" * 40)
print(f"        {name.upper()}              ")
print("═" * 40)
print(f"Item:                       {item}")
print(f"Price:                      ${price:.2f}")
print(f"Quantity:                   {quantity}")
print("-" * 40)
print(f"Total:                      ${total:.2f}")
print("═" * 40)


name = "Justin Bieber"
hometown = "Ontario, CAN"
hobby = "Famous Singer"
fun_fact = "I am fluent in French."
age = 32

name = input("Enter profile name: ")
fun_fact = input("Enter one fun fact: ")
hobby = input("Enter favorite hobby: ")
birth_year = input("Enter their birth year: ")


name = name.strip().upper()
fun_fact = fun_fact.strip().lower()
age = 2026 - int(birth_year)


print("╔════════════════════════════╗")
print(f"   Profile: {name}")
print("╚════════════════════════════╝")
print(f"Hometown:       {hometown}")
print(f"Hobby:          {hobby}")
print(f"Age:            {age}")

