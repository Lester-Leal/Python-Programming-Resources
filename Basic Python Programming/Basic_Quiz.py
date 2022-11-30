# Simple Quiz python program
# Author: Jiseeeh

# There are still more things that can be improve here so feel free to refractor this if you want to..

# Concepts you can learn about this program:
# - Conditionals
# - Loops
# - Code reuse
#   - You make small functions that does one thing and can be use over and over again.

score = 0
takes = 1
name: str


def main():
    global name

    print("Hello! Welcome, what's your name?")

    name = input("Name:")

    print("\nWelcome " + name + "!\n")

    takeQuiz()


def takeQuiz():
    global takes
    success = False

    # This will keep prompting the user if they want to take the quiz.
    # This will only stop if the user said no.

    while success == False:
        if takes == 1:
            choice = input("Do you want to take the quiz? (Yes/No): ").lower()
        else:
            choice = input("\nDo you want to try again? (Yes/No): ").lower()

        if choice == "yes":
            quiz()
            success = True
        elif choice == "no":
            exit()
            success = True
        else:
            print("Invalid input, please enter either Yes or No\n")

# start helper functions


def exit():
    global name
    print("\nThankyou " + name)


def quizEnd():
    global score
    global name

    print("Thank you for taking the quiz " + name + "!")
    print("Your total score is: " + str(score))

    takeQuiz()


def answer(correct):
    global score
    success = False

    # This will keep prompting the user for the answer unless they enter a value that is from range 1-4
    while success == False:
        answer = input("Answer: ")

        if not answer.isdigit():
            print("\nPlease enter numbers only\n")
            continue

        # parse the answer if the answer a digit
        answer = int(answer)

        if answer == correct:
            print("\nCorrect!\n")
            score += 1
            success = True

        elif answer >= 1 and answer <= 4:
            print("\nWrong!\n")
            success = True

        else:
            print("\nInvalid input. Please enter a number in the range of 1 to 4.\n")


# end helper functions


def quiz():
    global takes
    global score

    score = 0

    print("\u2500" * 80 + "\n")  # line
    print("Quiz Take #" + str(takes) + "\n")
    takes += 1

    # Question no.1
    print("Question #1")
    print("What does ARPA stands for?")
    print("[1]Advanced Research Project Agency")
    print("[2]Advancing and Researching Protecting Agency")
    print("[3]Advocacy Research Project Association ")
    print("[4]Advancing Research Project Association")
    answer(1)

    # Question no.2
    print("\u2500" * 80 + "\n")  # line
    print("Question #2")
    print("Who developed WWW?")
    print("[1]Tim Berner lee")
    print("[2]Sir Tim Berners Lee")
    print("[3]Sir Tims Berner Lees")
    print("[4]Sir Timber Lee")
    answer(2)

    # Question no.3
    print("\u2500" * 80 + "\n")  # line
    print("Question #3")
    print("Is Python a Low-level Programming Language?")
    print("[1]True")
    print("[2]False")
    print("[3]Maybe")
    print("[4]None of the above")
    answer(2)

    # Question no.4
    print("\u2500" * 80 + "\n")  # line
    print("Question #4")
    print("It is a step by step procedure that has instructions on how to solve a problem")
    print("[1]Flowchart")
    print("[2]Algorithm")
    print("[3]Graph")
    print("[4]Pseudocode")
    answer(2)

    # Question no.5
    print("\u2500" * 80 + "\n")  # line
    print("Question #5")
    print("It is a visual representation of the algorithm")
    print("[1]Flowchart")
    print("[2]Flow")
    print("[3]Graph")
    print("[4]Pseudocode")
    answer(1)

    # Question no.6
    print("\u2500" * 80 + "\n")  # line
    print("Question #6")
    print("Which of the following is not a pointing device?")
    print("[1]Mouse")
    print("[2]Joystick")
    print("[3]Keyboard")
    print("[4]Light pen")
    answer(3)

    # Question no.7
    print("\u2500" * 80 + "\n")  # line
    print("Question #7")
    print("Which of the following stores bits and bytes? (Instructions and Data)")
    print("[1]Optical Disk")
    print("[2]Memory")
    print("[3]Magnetic Disks")
    print("[4]Hard Disk")
    answer(2)

    # Question no.8
    print("\u2500" * 80 + "\n")  # line
    print("Question #8")
    print("A ______ is a computer application that understands the languages\n"
          + "(called protocols) of the internet used to view web pages")
    print("[1]Web page")
    print("[2]Internet")
    print("[3]Web Server")
    print("[4]Browser")
    answer(4)

    # Question no.9
    print("\u2500" * 80 + "\n")  # line
    print("Question #9")
    print("Which of the following is the binary representation of octal = 321?")
    print("[1]011100101 base2")
    print("[2]011010001 base2")
    print("[3]001010001 base2")
    print("[4]1001001000 base2")
    answer(2)

    # Question no.10
    print("\u2500" * 80 + "\n")  # line
    print("Question #10")
    print("Which of the following is the octal representation of binary = 1 111 110 100 111 101 110?")
    print("[1]1778732 base8")
    print("[2]1746675 base8")
    print("[3]1764756 base8")
    print("[4]1746876 base8")
    answer(3)

    # Question no.11
    print("\u2500" * 80 + "\n")  # line
    print("Question #11")
    print("Which of the following is the Decimal representation of binary = 10110")
    print("[1] 22 base10")
    print("[2] 25 base10")
    print("[3] 21 base10")
    print("[4] 24 base10")
    answer(1)

    # Question no.12
    print("\u2500" * 80 + "\n")  # line
    print("Question #12")
    print("___________ created Python")
    print("[1] James Gosling")
    print("[2] Steve Jobs")
    print("[3] Bill Gates")
    print("[4] Guido van Rossum")
    answer(4)

    # Question no.13
    print("\u2500" * 80 + "\n")  # line
    print("Question #13")
    print("When was Python created?")
    print("[1] January 4, 1999")
    print("[2] February 20,1991")
    print("[3] December 12, 2000")
    print("[4] February 20, 1999")
    answer(2)

    # Question no.14
    print("\u2500" * 80 + "\n")  # line
    print("Question #14")
    print("It is a prelude to our program codes and it is a draft.")
    print("[1] Algorithm")
    print("[2] Pseudocode")
    print("[3] Notes")
    print("[4] Flowchart")
    answer(2)

    # Question no.15
    print("\u2500" * 80 + "\n")  # line
    print("Question #15")
    print("What does SDLC stands for?")
    print("[1] System Development Life Cycle")
    print("[2] Systematic Development Life Commission")
    print("[3] Systems Development Lifes Cycle")
    print("[4] System Development and Life Cycles")
    answer(1)

    quizEnd()


main()
