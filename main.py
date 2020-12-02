from random import choice
again = 1
total_guesses = 0
correct_guesses = 0
while int(again) > 0:
    inpt = input("Input your prediction for the face of the dice\n")
    otpt = choice(['1','2','3','4','5','6'])
    print(otpt)
    if (inpt == otpt):
        print("You Guessed it Correctly")
        total_guesses += 1
        correct_guesses += 1
    else:
        print("You Guessed it Wrong")
        total_guesses += 1
    print("Total Guesses are " + str(total_guesses) +
          " and correct guesses are " + str(correct_guesses))
    again = input("Input 1 to play again and 0 to stop\n")
