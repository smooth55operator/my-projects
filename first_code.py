user=input("choose: (rock, paper, scissors) ")
import random
choices=["rock", "paper", "scissors"]
computer=random.choice(choices)
print("computer chose:",computer)
if user==computer:
    print("tie")
elif user=="rock" and computer=="scissors":
    print("user won")
elif user=="paper" and  computer=="rock":
    print("user won")
elif user=="scissors" and computer=="paper":
    print("user won")
else:   
    print("computer won")
