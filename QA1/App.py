import sqlite3

def get_questions(cursor, table_name):
    cursor.execute(f"SELECT id, question, answer FROM {table_name}")
    return cursor.fetchall()

def conduct_quiz(questions):
    score = 0
    for question in questions:
        print(question[1])  # Print the question text
        user_answer = input("Your answer: ")
        if user_answer.lower() == question[2].lower():
            print("\033[92mCorrect!\033[0m")  # Green text
            score += 1
        else:
            print(f"\033[91mWrong! The correct answer is: {question[2]}\033[0m")  # Red text
        print()
    
    print(f"Quiz completed! Your score: {score}/{len(questions)}")

def main():
    connection = sqlite3.connect('questions_answers.db')
    cursor = connection.cursor()

    print("Select a topic for your quiz:")
    topics = {
        "1": "adv_finance_questions",
        "2": "database_questions",
        "3": "python_questions",
        "4": "computer_forensics_questions",
        "5": "financial_modeling_questions"
    }

    for key, value in topics.items():
        print(f"{key}: {value.replace('_questions', '').replace('_', ' ').title()}")

    topic_choice = input("Enter the number of your choice: ")
    if topic_choice not in topics:
        print("Invalid choice. Exiting the quiz.")
        return

    questions = get_questions(cursor, topics[topic_choice])
    if not questions:
        print("No questions found for the selected topic.")
    else:
        conduct_quiz(questions)

    connection.close()

if __name__ == "__main__":
    main()