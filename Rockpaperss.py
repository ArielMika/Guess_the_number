import random

user_wins = 0
pc_wins = 0
while True:
    option = ['rock','pepar','scissors']

    user_input = input("type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break


    if user_input not in ['rock', 'paper' ,'scissors']:
        continue

    random_number = random.randint(0,2)
    # rock = 0 , paper = 1, scissors = 2
    computer_pick = option[random_number]
    print('computer pick' , computer_pick + '.')
    if user_input == "rock" and computer_pick == 'scissors':
        print('you won!')
        user_wins += 1

    elif user_input == "paper" and computer_pick == 'rock':
        print('you won!')
        user_wins += 1

    elif user_input == "scissors" and computer_pick == 'paper':
        print('you won!')
        user_wins += 1

    else:
        print('you lost')
        pc_wins += 1


print('you won: ',user_wins, 'times.')
print('computer won',pc_wins,'times.')
print('Goodbye')