def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower()
    if response == "yes" or response == "y":
        response = "yes"
        return response
    elif response == "no" or response == "n":
      response = "no"
      return response
    else:
      print("Please answer yes or no.")

# main routine goes here
show_instructions = yes_no("Have you played the game before? ")
print ("you chose {}".format (show_instructions))
print ()
having_fun = yes_no (" Are you having fun?")
print ("you said {} to having fun".format(having_fun))