'''
Simple quiz game that asks the user a series of questions and keeps track of their score. 
The user can choose to play again after completing the quiz.
'''

quiz_data = {
    "Space Quiz": [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": {
                "A": "Venus",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Mercury"
            },
            "answer": "B"
        },
        {
            "question": "Which planet is the largest in our Solar System?",
            "options": {
                "A": "Saturn",
                "B": "Earth",
                "C": "Jupiter",
                "D": "Neptune"
            },
            "answer": "C"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": {
                "A": "Venus",
                "B": "Mercury",
                "C": "Earth",
                "D": "Mars"
            },
            "answer": "B"
        },
        {
            "question": "Which planet is famous for its beautiful rings?",
            "options": {
                "A": "Uranus",
                "B": "Saturn",
                "C": "Jupiter",
                "D": "Neptune"
            },
            "answer": "B"
        },
        {
            "question": "What is the name of Earth's natural satellite?",
            "options": {
                "A": "Titan",
                "B": "Moon",
                "C": "Europa",
                "D": "Phobos"
            },
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Blue Planet?",
            "options": {
                "A": "Earth",
                "B": "Neptune",
                "C": "Uranus",
                "D": "Venus"
            },
            "answer": "A"
        },
        {
            "question": "How many planets are in the Solar System?",
            "options": {
                "A": "7",
                "B": "8",
                "C": "9",
                "D": "10"
            },
            "answer": "B"
        },
        {
            "question": "Which planet is famous for the Great Red Spot?",
            "options": {
                "A": "Saturn",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Neptune"
            },
            "answer": "C"
        },
        {
            "question": "Which planet is the hottest in our Solar System?",
            "options": {
                "A": "Mercury",
                "B": "Venus",
                "C": "Mars",
                "D": "Earth"
            },
            "answer": "B"
        },
        {
            "question": "The Sun is a...",
            "options": {
                "A": "Planet",
                "B": "Star",
                "C": "Galaxy",
                "D": "Comet"
            },
            "answer": "B"
        }
    ],
"General Knowledge Quiz": [
    {
        "question": "What is the capital of India?",
        "options": {
            "A": "Mumbai",
            "B": "New Delhi",
            "C": "Kolkata",
            "D": "Chennai"
        },
        "answer": "B"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": {
            "A": "364",
            "B": "365",
            "C": "366",
            "D": "367"
        },
        "answer": "C"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": {
            "A": "Atlantic",
            "B": "Indian",
            "C": "Pacific",
            "D": "Arctic"
        },
        "answer": "C"
    },
    {
        "question": "Who invented the telephone?",
        "options": {
            "A": "Thomas Edison",
            "B": "Nikola Tesla",
            "C": "Alexander Graham Bell",
            "D": "Isaac Newton"
        },
        "answer": "C"
    },
    {
        "question": "Which is the national animal of India?",
        "options": {
            "A": "Lion",
            "B": "Elephant",
            "C": "Tiger",
            "D": "Peacock"
        },
        "answer": "C"
    },
    {
        "question": "Which gas do humans breathe in to survive?",
        "options": {
            "A": "Nitrogen",
            "B": "Oxygen",
            "C": "Carbon Dioxide",
            "D": "Hydrogen"
        },
        "answer": "B"
    },
    {
        "question": "Which is the smallest continent?",
        "options": {
            "A": "Europe",
            "B": "Australia",
            "C": "Antarctica",
            "D": "South America"
        },
        "answer": "B"
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": {
            "A": "Holi",
            "B": "Diwali",
            "C": "Eid",
            "D": "Christmas"
        },
        "answer": "B"
    },
    {
        "question": "Which is the fastest land animal?",
        "options": {
            "A": "Lion",
            "B": "Tiger",
            "C": "Cheetah",
            "D": "Leopard"
        },
        "answer": "C"
    },
    {
        "question": "Which country is famous for the Eiffel Tower?",
        "options": {
            "A": "Germany",
            "B": "Italy",
            "C": "France",
            "D": "Spain"
        },
        "answer": "C"
    }
    ],
"Geography Quiz": [
    {
        "question": "Which is the longest river in the world?",
        "options": {
            "A": "Amazon",
            "B": "Nile",
            "C": "Ganga",
            "D": "Yangtze"
        },
        "answer": "B"
    },
    {
        "question": "Which is the highest mountain in the world?",
        "options": {
            "A": "Kanchenjunga",
            "B": "K2",
            "C": "Mount Everest",
            "D": "Annapurna"
        },
        "answer": "C"
    },
    {
        "question": "Which desert is the largest hot desert in the world?",
        "options": {
            "A": "Gobi",
            "B": "Sahara",
            "C": "Thar",
            "D": "Arabian"
        },
        "answer": "B"
    },
    {
        "question": "Which continent is India located in?",
        "options": {
            "A": "Europe",
            "B": "Asia",
            "C": "Africa",
            "D": "Australia"
        },
        "answer": "B"
    },
    {
        "question": "Which ocean lies to the south of India?",
        "options": {
            "A": "Atlantic",
            "B": "Arctic",
            "C": "Indian Ocean",
            "D": "Pacific"
        },
        "answer": "C"
    },
    {
        "question": "Which country has the largest population (2026)?",
        "options": {
            "A": "China",
            "B": "India",
            "C": "USA",
            "D": "Indonesia"
        },
        "answer": "B"
    },
    {
        "question": "What is the capital of Japan?",
        "options": {
            "A": "Osaka",
            "B": "Kyoto",
            "C": "Tokyo",
            "D": "Hiroshima"
        },
        "answer": "C"
    },
    {
        "question": "Which is the largest continent?",
        "options": {
            "A": "Africa",
            "B": "Asia",
            "C": "Europe",
            "D": "North America"
        },
        "answer": "B"
    },
    {
        "question": "Which line divides Earth into the Northern and Southern Hemispheres?",
        "options": {
            "A": "Tropic of Cancer",
            "B": "Equator",
            "C": "Prime Meridian",
            "D": "Tropic of Capricorn"
        },
        "answer": "B"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": {
            "A": "China",
            "B": "South Korea",
            "C": "Japan",
            "D": "Thailand"
        },
        "answer": "C"
    }
],
"History Quiz": [
    {
        "question": "Who was the first Prime Minister of India?",
        "options": {
            "A": "Mahatma Gandhi",
            "B": "Jawaharlal Nehru",
            "C": "Sardar Patel",
            "D": "Lal Bahadur Shastri"
        },
        "answer": "B"
    },
    {
        "question": "In which year did India gain independence?",
        "options": {
            "A": "1945",
            "B": "1947",
            "C": "1950",
            "D": "1930"
        },
        "answer": "B"
    },
    {
        "question": "Who built the Taj Mahal?",
        "options": {
            "A": "Akbar",
            "B": "Shah Jahan",
            "C": "Aurangzeb",
            "D": "Humayun"
        },
        "answer": "B"
    },
    {
        "question": "Who discovered America?",
        "options": {
            "A": "Vasco da Gama",
            "B": "Christopher Columbus",
            "C": "Ferdinand Magellan",
            "D": "James Cook"
        },
        "answer": "B"
    },
    {
        "question": "Which war ended in 1945?",
        "options": {
            "A": "World War I",
            "B": "World War II",
            "C": "Cold War",
            "D": "Crimean War"
        },
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": {
            "A": "Bhagat Singh",
            "B": "Mahatma Gandhi",
            "C": "Subhas Chandra Bose",
            "D": "Jawaharlal Nehru"
        },
        "answer": "B"
    },
    {
        "question": "Who was the first President of India?",
        "options": {
            "A": "Rajendra Prasad",
            "B": "A. P. J. Abdul Kalam",
            "C": "Jawaharlal Nehru",
            "D": "Sardar Vallabhbhai Patel"
        },
        "answer": "A"
    },
    {
        "question": "Which civilization built the pyramids?",
        "options": {
            "A": "Romans",
            "B": "Egyptians",
            "C": "Greeks",
            "D": "Persians"
        },
        "answer": "B"
    },
    {
        "question": "Who found the sea route to India in 1498?",
        "options": {
            "A": "Christopher Columbus",
            "B": "Vasco da Gama",
            "C": "Ferdinand Magellan",
            "D": "Marco Polo"
        },
        "answer": "B"
    },
    {
        "question": "The Great Wall is located in which country?",
        "options": {
            "A": "India",
            "B": "China",
            "C": "Japan",
            "D": "Mongolia"
        },
        "answer": "B"
    }
],
"Programming Quiz": [
    {
        "question": "Which programming language are you learning now?",
        "options": {
            "A": "Java",
            "B": "Python",
            "C": "C++",
            "D": "JavaScript"
        },
        "answer": "B"
    },
    {
        "question": "Which symbol is used to write comments in Python?",
        "options": {
            "A": "//",
            "B": "#",
            "C": "<!-- -->",
            "D": "%%"
        },
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": {
            "A": "display()",
            "B": "print()",
            "C": "output()",
            "D": "echo()"
        },
        "answer": "B"
    },
    {
        "question": "Which function is used to get user input in Python?",
        "options": {
            "A": "input()",
            "B": "read()",
            "C": "scan()",
            "D": "get()"
        },
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False values?",
        "options": {
            "A": "int",
            "B": "str",
            "C": "bool",
            "D": "float"
        },
        "answer": "C"
    },
    {
        "question": "Which loop repeats while a condition is True?",
        "options": {
            "A": "for",
            "B": "while",
            "C": "do-while",
            "D": "repeat"
        },
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "fun",
            "D": "define"
        },
        "answer": "B"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set"
        },
        "answer": "C"
    },
    {
        "question": "Which module is commonly used to generate random numbers?",
        "options": {
            "A": "math",
            "B": "random",
            "C": "os",
            "D": "time"
        },
        "answer": "B"
    },
    {
        "question": "Which operator checks if two values are equal?",
        "options": {
            "A": "=",
            "B": "==",
            "C": "!=",
            "D": ">="
        },
        "answer": "B"
    }
],
}

def run_quiz(category_name, questions):
    score = 0
    print(f"\nStarting the {category_name}...\n")
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question['question']}")
        for option, answer in question['options'].items():
            print(f"{option}: {answer}")
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            correct_option = question['options'][question['answer']]
            print(f"Wrong! The correct answer is {question['answer']} ({correct_option}).\n")
    print(f"You scored {score} out of {len(questions)}.\n")

def main():
    print("Welcome to the Quiz Game!")
    while True:
        print("\nAvailable Quiz Categories:")
        for i, category in enumerate(quiz_data.keys(), start=1):
            print(f"{i}. {category}")
        category_choice = input("Choose a category by number (or type 'exit' to quit): ").strip()
        if category_choice.lower() == 'exit':
            print("Thank you for playing! Goodbye!")
            break
        if not category_choice.isdigit() or int(category_choice) < 1 or int(category_choice) > len(quiz_data):
            print("Invalid choice. Please try again.")
            continue
        selected_category = list(quiz_data.keys())[int(category_choice) - 1]
        run_quiz(selected_category, quiz_data[selected_category])
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()