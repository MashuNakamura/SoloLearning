# Magic 8 Balls

import random

question = input("Question : ")
if question == "":
  print("Please input first")
else:
  random_answer = random.randint(1, 9)
  if random_answer == 1:
    answer = "Yes - definitely."
  elif random_answer == 2:
    answer = "It is decidedly so."
  elif random_answer == 3:
    answer = "Without a doubt."
  elif random_answer == 4:
    answer = "Reply hazy, try again."
  elif random_answer == 5:
    answer = "Ask again later."
  elif random_answer == 6:
    answer = "Better not tell you now."
  elif random_answer == 7:
    answer = "My sources say no."
  elif random_answer == 8:
    answer = "Outlook not so good."
  elif random_answer == 9:
    answer = "Very doubtful."
  
  print(f"Magic 8 Ball: {answer}")
