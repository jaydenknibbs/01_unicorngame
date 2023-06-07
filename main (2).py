def num_cheaker(question, low, high):
    error = "Please enter a whole number between {} and {}\n".format(low+1, high)

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))

            # Check if the amount is within the desired range
            if low < response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Call the function to start the game
how_much = num_cheaker("How much would you like to play with? ", 0, 10)

print (" you will be spending ${}".format(how_much))