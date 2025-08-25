import random

easy_word = ["apple","train","book","tiger","india"]
mediuam_word = ["computter","bottle","mouse","website","pencile"]
hard_word = ["network","laptop","softwore","python","mobile"]

print("Wellcome to the password gussing game:")
print("choose dificulty lavel (easy,medium,hard):")
level =input("Enter dificulty:").lower()


if level=="easy" :
    secret=random.choice(easy_word)
elif level=="medium" :
    secret=random.choice(mediuam_word)
elif level=="hard" :
    secret=random.choice(hard_word)

else:
    print ("ivelid choose.Defaulting to easy lavel:")
    secret=random.choice(easy_word)

attampt=0
print("guess the secret:")
while True :
    guess=input("Enter your guess:")

    attampt+=1

    if guess==secret:
        print(f"Congratulation you guess the carrect word in {attampt} attampt:")
        break

    hint =""

    for i in range (len(secret)):
        if i <  len(guess) and guess[i]==secret[i]:
         hint += guess[i]
        else:
            hint+="_" 
    print("HINT:",hint)    
print("GAME OVER:")
    



   

 