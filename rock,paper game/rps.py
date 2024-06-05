import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      'Rock vs Paper -> Paper wins\n'
      'Rock vs Scissors -> Rock wins\n'
      'Paper vs Scissors -> Scissors wins\n')
choices = ['Rock', 'Paper', 'Scissors']
while True:
    print("Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n")
    user_choice = int(input("Enter your choice: "))
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input('Enter a valid choice please: '))
    user_choice_name = choices[user_choice - 1]
    print(f'User choice is: {user_choice_name}')
    print("Now it's Computer's Turn...")
    comp_choice = random.randint(1, 3)
    comp_choice_name = choices[comp_choice - 1]
    print(f"Computer choice is: {comp_choice_name}")
    if user_choice_name == comp_choice_name:
        result = "DRAW"
    elif (user_choice_name == 'Rock' and comp_choice_name == 'Scissors') or \
         (user_choice_name == 'Paper' and comp_choice_name == 'Rock') or \
         (user_choice_name == 'Scissors' and comp_choice_name == 'Paper'):
        result = "User"
    else:
        result = "Computer"
    if result == "DRAW":
        print("<== It's a tie ==>")
    else:
        print(f"<== {result} wins ==>")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing")
