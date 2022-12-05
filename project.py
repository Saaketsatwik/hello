print("Welcome To the game")
print("DESCRIPTION of the game - This a game where you enter a choice i.e. rock, paper, scissor."
      """ Then the computer will also make a choice""")
print("press p for playing")
print("press q for exiting")
x="p"
y="q"
z=str(input("input your choice"))
while z==x:
    a=["rock", "paper","scissor"]
    b=str(input("enter your choice  "))
    import random
    c=random.choice(a)
    print("your choice =",b)
    print("computer choice =",c)
    if b=="rock" and c=="paper":
        print("you lost")
    elif b=="rock" and c=="scissor":
        print("you won")
    elif b=="rock" and c=="rock":
        print("draw")
    elif b=="paper" and c=="rock":
        print("you won")
    elif b=="paper" and c=="scissor":
        print("you lost")
    elif b==c:
        print("draw")
    elif b=="scissor" and c=="rock":
        print("you lost")
    elif b=="scissor" and c=="paper":
        print("you won")
    elif b==c:
        print("draw")
    print("PRESS p TO PLAY AGAIN ")
    z=str(input())