import random
words=['lily', 'lotus', 'rose', 'tulip', 'daisy']
   #chose a random word
word=random.choice(words)  
   #show dash for gussing letter
guesses_space=["_"]*len(word)  
# chance for gussing
attempts=6
# list to store user gussed letter
guessed_letter=[]

print("######welcome to hangman game######")
print("best of luck***")
print("guss the word")
print(" ".join(guesses_space))
#loop work in condition (attempts remaining & untill guess space still)
while attempts > 0 and "_" in guesses_space:   
    guess=input("\n Enter a letter:").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("please enter only alphabat letter from A TO Z, a to z")
        continue

    if guess in guessed_letter:
        print("\n you've already guess that letter. please! guess another letter.... ")
        continue

    guessed_letter.append(guess)   # # guess letter store in list

    if guess in word:
        print("great! you guess correct letter")

        for i in range(len(word)):
            if word[i] == guess:
                guesses_space[i]= guess           # update letter inplace of space display word
    else:
                attempts-=1                        # no. of attempts decrease when chose wrong letter
                print("ohh wrong!  Attempts left:",attempts)
    print("     "," ".join(guesses_space))
#lopp break in two condition attempts are completed or word are guessed
if "_" not in guesses_space:
     print("*congratulation*   you win~")
     
else:
     print("you louse! try next time..")
     print("The word was", word)     
