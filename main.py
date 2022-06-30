import random

top_of_range =input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a numbe rlarger than 0 next time')
        quit()
else:
    print('please type a number next time')
    quit()

random_number = random.randint( 0 , top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input('guess your number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time')
        continue
    if user_guess == random_number:
        print("you got it!")
        break
    else:
        print('wrong!')
    if user_guess > random_number:
            print('youre above the number')
    else:
            print('youre below the nubmer')


print('you got it in ', guesses ,'guesses')