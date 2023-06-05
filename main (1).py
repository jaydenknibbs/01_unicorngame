error = "please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the question
        response = input("How much would you like to play with? ")
        response = int(response)  # Convert the input to an integer

        # check if the amount is within the desired range
        if 1 <= response <= 10:
            print("You have asked to play with ${}".format(response))
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
