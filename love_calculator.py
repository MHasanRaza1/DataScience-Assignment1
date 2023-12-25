name1 = input('Enter Name1: ').lower()
name2 = input('Enter Name2: ').lower()

match = 'true'
count = 0
for letter in match:
    count += name1.count(letter)
    count += name2.count(letter)


match1 = "love"
count1 = 0
for letter in match1:
    count1 += name1.count(letter)
    count1 += name2.count(letter)


score = int(str(count) + str(count1))
print("The Love Calculator is calculating your score...")
print()

if 10 > score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}")
