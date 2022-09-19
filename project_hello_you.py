# Ask user for name
name = input("What is your name?\n")

# Ask user for age
age = input("What is your age?\n")

# Ask user of city
city = input("Which city do you live?\n")

# Ask user what they enjoy
love = input("What do you love doing?\n")

# Print output text
string = "Your name is {}. You are {} years old. You live in {} & you love doing {}."
output = string.format(name, age, city, love)

# Print output to string
print(output)
