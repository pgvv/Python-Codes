user_known =["Alex","Bob"]

while True:
    print("Hello, My name is Travis")
    name = input("What is your name? ").strip().capitalize()

    if name in user_known:
        print("Hello {}! :D".format(name))
        
        remove = input("Would you like to be removed from the system (Y/N)? ").strip().lower()
        if remove == "y":
            user_known.remove(name)
            print("OK {}, you have been removed from the system".format(name))
        elif remove == "n":
            print("Thanks for staying in the system {}!".format(name))
    else:
        print("Sorry, I don't think we have met {}".format(name))

        add = input("Would you like to be added to the system (Y/N)? ").strip().lower()
        if add == "y":
            user_known.append(name)
            print("Congrats {}, you have been successfully added to the system!".format(name))
        elif add == "n":
            print("No problem {}!".format(name))
        
        
