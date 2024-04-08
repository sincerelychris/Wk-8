#1 

number = 0

while number < 100:
  print(number)
  number = number + 5

#

costomer_order = ("")

while costomer_order == "":
  costomer_order = input("WELCOME! What do you want for dinner? ")

print(f"thank you for your order. {costomer_order} is a great choice!")

#
age = int(input("how old are you? "))

while age <= 18:
  print("You are old enough to vote!")
  break
#

num = ()
while num < 1 or num > 5 or num == "":
  num = int(input("Enter a number 1-5: "))
  print(f"sorry, {num} is not a valid choice")
print(f"you entered {num}")