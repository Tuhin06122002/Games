P1 = input("Name of Player 1: ")
P2 = input("Name of Player 2: ")

s = input(P1+", Enter your word: ").lower()
r = "*"*len(s)

life = 5
ct=1

while life>0 and "*" in r:
    if ct:
        print(r)
        ct = 0
    
    b = input(P2+", guess: ").lower()

    if len(b)>1:
        if b==s:
            break
        else:
            print("Wrong")
            life -= 1

    elif len(b)==1:
        if b not in r:
            if b in s:
                t = ""
                for i in range(len(s)):
                    if s[i]==b:
                        t += b
                    elif r[i] != "*":
                        t += r[i]
                    else:
                        t += "*"
                r=t
                ct=1
            else:
                print("Wrong")
                life -= 1
        else:
            print("You have already said this alphabet.")
if life == 0:
    print("You are hanged.")
else:
    print("You win.")

print("The word is",s)
