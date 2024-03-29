
def display_intro():
    print("Welcome to my Python quiz!")

def play_game():
    playing = input("Do you want to play my game? (yes/no) ")
    return playing.lower() == "yes"


def ask_questions():
    
    questions = {
        "Is python a programming language?": "Yes",
        "What created python?": "Guido van Rossum",
        "Which year was python released?": "1991",
        "What can python be used for?": "Web Development, Software Development, Mathematics",
        "Many PCs and Macs will have python already installed.": "True",
        "Python syntax can be executed by writing directly in the Command Line.": "True",
        "The indentation in Python is very important.": "True",
        "In Python, variables are created when you assign a value to it?": "True",
        "Comments can be used to explain Python code.": "True",
        "Variables are containers for storing data values": "True",
        "String variables can be declared either by using single or double quotes?": "Yes"
    }

    
    score = 0

    print("Okay! Let's play :)\n")

    
    for question, correct_answer in questions.items():
        answer = input(question + " ").strip()

        if answer.lower() == correct_answer.lower():
            print("That's Correct!")
            score += 1
        else:
            print("That's Incorrect! The correct answer is:", correct_answer)

    return score


def display_results(score, total_questions):
    print("\nYou got", score, "out of", total_questions, "questions correct.")
    


def main():
    display_intro()
    
    if not play_game():
        quit()

    
    score = ask_questions()
    
    display_results(score, (ask_questions))


if __name__ == "__main__":
    main()