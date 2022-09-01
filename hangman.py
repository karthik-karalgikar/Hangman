word = list("pussy")
wronguesslist = []
length = len(word)
print("_ "*length)
print("The word contains ", length, " letters")
guessedWord = ["_"]*length
wrongGuesses = 0
while guessedWord != word and wrongGuesses != 7:

    ele = str(input("Enter an alphabet of your choice: "))
    if ele in word:
        print("You have guessed correctly! One of the alphabets is ",ele)
        for i in range(0, length):
            if word[i] == ele:
                guessedWord[i] = ele
    else:
        wrongGuesses += 1
        print("Wrong guess. Try again. You have ",7-wrongGuesses," chances")
        wronguesslist.append(ele)
    print("The guesses which you have already made are",wronguesslist )
    print(" ".join(guessedWord))

if wrongGuesses == 7:
    print("You lost. The correct word was ",word)
else:
    print("You won!")
    


