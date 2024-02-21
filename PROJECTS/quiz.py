
def new_game():
    guesses = []
    correct_guess = 0
    current_question = 1

    for question in questions:
        print("-----------------------------")
        print(question)

        for option in options[current_question - 1]:
            print(option)

        guess = input("Enter (A/B/C/D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guess += check_bot(questions.get(question), guess)
        current_question += 1

    display_score(correct_guess, guesses)

def check_bot(answer, guess):
    if answer == guess:
        print("Correct.")
        return 1
    else:
        return 0

def display_score(correct_guess, guesses):
    print("------------------------")
    print("RESULTS")
    print("------------------------")
    print("Answers: ", end = " ")
    for i in questions:
        print(questions.get(i), end = " ")
    print(" ")

    print("Guesses: ", end = " ")
    for i in guesses:
        print(i, end = " ")
    print(" ")

    score = int((correct_guess/len(questions)) * 100)
    print("You score is: " + str(score) + "%")

def play_again():
    response = input("'Re-quiz' again?")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

# dictionary of quesions
questions = {
    "Question: What is the capital city of Australia?": "B",
    "Question: Who wrote the play 'Romeo and Juliet'?": "C",
    "Question: What is the chemical symbol for gold?": "D",
    "Question: In which year did the first manned moon landing occur?": "B",
    "Question: What is the largest mammal on Earth?": "D"
}

options = [
    ["A. Africa", "B. Canberra", "C. Tbilisi", "D. Vietnam"],
    ["A. George Washington", "B. Bill Gates", "C. William Shakespeare", "D. Robert Prost"],
    ["A. Ho2", "B. Mag", "C. None", "D. Au"],
    ["A. 1980", "B. 1969", "C. 1970", "D. 2000"],
    ["A. Elephant", "B. Mammont", "C. Dinosaur", "D. Blue Whale"]
]

new_game()
while play_again():
    new_game()

print("Bye then.")