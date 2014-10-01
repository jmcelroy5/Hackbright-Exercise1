def main():
    import random

    print "Welcome to the guessing game."

    name = raw_input("What is your name? ")

    print "Hello there, %s" % name

    print "%s, I'm thinking of a number between 1 and 100. Try to guess my number. " % name

    count = 0

    personal_best = 0

    answer = random.randint(1, 100)

    while True:
        guess = raw_input("What is your guess?")
        count += 1

        if not guess.isdigit():
            print "That is not a valid number."
        else:
            guess = int(guess)

        if guess > 100 or guess < 1:
            print "That number is out of range."
        elif guess > answer:
            print "Too high!"
        elif guess < answer: 
            print "Too low!"
        else:
            print "Correct! You win."
            print "Well done, %s! You found my number in %d tries!" % (name, count)
            print "Do you want to play again?"
            print "Type 1 to continue or 2 to exit."
            
            playagain = raw_input('--> ')
            if playagain == "1":
                if personal_best == 0 or count < personal_best:
                    personal_best = count
                print "Ok, let's play again. Try to beat your record score of %s tries." % personal_best
                print "%s, I'm thinking of a number between 1 and 100. Try to guess my number" % name
                answer = random.randint(1, 100)
                count = 0
            else:
                print "Thanks for playing!"
                break

if __name__ == "__main__":
    main()