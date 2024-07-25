predefine_num=56

max_attempts=10

attempts=0

print("You haave to guess the write I write down you have 10 attempts ")

while attempts < max_attempts:#0<12345678910
    guess = int(input("Enter your guess: "))
    if (guess==predefine_num):
        print("Congrats your guess is right")
        break
    else:
        attempts = attempts +1 
        remaining_attempts= max_attempts - attempts
        
        if(remaining_attempts>0):
            print("Try again  you have some  attempts left")
        else:
            print("Loser , You are out of the game")

