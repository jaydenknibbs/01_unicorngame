def yes_no(question):
    valid = False
    while not valid:
        played_before = input(question).lower()

        if played_before == "yes" or played_before == "y":
            return "yes"
        elif played_before == "no" or played_before == "n":
            return "no"
        else:
            print("Please answer yes or no.")


def instructions () :
    print ("*** how to play ***")
    print ()
    print ("the rules of the game go here")
    print()
    return""
# Main routine goes here
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
  instructions ()

print ("program continues")