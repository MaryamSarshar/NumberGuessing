import random
highest_val = 0
lowest_val = 0
difficulty = input("Choose a difficulty level(Easy, Medium, Hard, Legendry): ")
if difficulty == "Easy":
    highest_val = 10
    lowest = 1
elif difficulty == "Medium":
    highest_val = 100
    lowest = 1
elif difficulty == "Hard":
    highest_val = 500
    lowest = 1
elif difficulty == "Legendry":
    highest_val = 1000
    lowest = 1
else:
    print("Invalid difficulty level. please select a level of (Easy, Medium, Hard,Legendry)")
random_num = random.randint(lowest_val , highest_val)
print("Guess the number between {} and {}".format(lowest_val,highest_val))

guesses = 0
max_guesses = int(input("Enter the maximum number of guesses allowed: "))

while guesses < max_guesses:
    guess = int(input("guess the number: "))
    guesses +=1
    if guess < random_num:
        print("guess higher")
    elif guess > random_num:
        print("guess lower")
    else:
        print("Congratulations!! You found the number in {} guesses!".format(guesses))
        break
    if  guesses == max_guesses:
        print("Sorry, You've reached the maximum number of guesses. The number was {0}".format(random_num))
        

