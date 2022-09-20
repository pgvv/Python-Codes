# Ask user for their email address
email = input("What is your email address?\n").strip()

# Slice out user name
username = email[:email.index("@")]

# Slice domain name
domain = email[email.index("@") + 1:]

# Format message
message = "Your username is {}\nYour domain name is {}".format(username, domain)

# Display output message
print(message)
