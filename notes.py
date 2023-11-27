import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for i in range(20):
...     if player_one.pos() >= (300,100):
...             print("Player One Wins!")
...             break
...     elif player_two.pos() >= (300,-100):
...             print("Player Two Wins!")
...             break
...     else:
...             player_one_turn = input("Press 'Enter' to roll the die ")
...             die_outcome = random.choice(die)
...             print("The result of the die roll is: ")
...             print(die_outcome)
...             print("The number of steps will be: ")
...             print(20*die_outcome)
...             player_one.fd(20*die_outcome)
...             player_two_turn = input("Press 'Enter' to roll the die ")
...             die_outcome = random.choice(die)
...             print("The result of the die roll is: ")
...             print(die_outcome)
...             print("The number of steps will be: ")
...             print(20*die_outcome)
...             player_two.fd(20*die_outcome)