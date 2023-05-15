while True:
    response = input("Would you like to proceed? (y/n): ").lower().strip()

    if response == "y" or response == "yes":
        print("Great, let's proceed!")
    elif response == "n" or response == "no":
        print("Okay, we'll stop here.")
    elif response == "exit":
        print("Goodbye!")
        break
    else:
        print("please respond yes or no or y/n")