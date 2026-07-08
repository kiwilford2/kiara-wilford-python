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

age = input("Enter the year you were born: ")
age = int(age)

birth_year = 1989
current_year = 2026

birth_year = int(birth_year)
current_year = int(current_year)
age = (current_year - birth_year)
print(f" You are approximately {age} years old.")

num_1 = input("Enter a number: ")
num_2 = input("Enter a second number: ")

num_1 = float(num_1)
num_2 = float(num_2)

total = num_1 * num_2
print(f"The answer is {total}.")


name = "receipt"
item = "Movie Ticket"
price = 15.00
price = float(price)
quantity = 4
total = 60.00
total = float(total)

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

name = input("Who is the name of the person? ")
occasion = input("What's the occassion? ")
name = name.strip().upper()
occasion = occasion.strip().lower()

age = int(age)

print("╔════════════════════════════╗")
print(f"   Profile: {name}")
print("╚════════════════════════════╝")
print(f"Hometown:       {hometown}")
print(f"Hobby:          {hobby}")
print(f"Age:            {age}")
