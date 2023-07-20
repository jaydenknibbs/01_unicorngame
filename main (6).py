import random

#main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
#testing
for item in range(0, 20):
  chosen_num = random.randint(1, 10)

#AJUSTING THE BALANCE/S
  if 1 <=chosen_num <= 5:
      chosen = "unicorn"
      balance +=4
  elif 6 <= chosen_num <= 36:
      chosen = "donkey"
      balance -= 1
  else:
        balance -= 0.5


print ()
print ("starting balance: ${:2f}".format(STARTING_BALANCE))
print ("final balance : ${: .2f}".format(balance))