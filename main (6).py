# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

numb_of_payers = len(names)

bill_payer = random.randint(0,numb_of_payers - 1
)


print(f"Looks like {names[bill_payer]} is paying the bill!") 

