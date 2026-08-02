'''
Quiz Game
'''
def Space_Quiz():
    print("Welcome to the Space Quiz!")
    
    question_bank = [
            {"question": "Which planet is known as the Red Planet?", "answer": "B. Mars"},
            {"question": "Which planet is the largest in our Solar System?", "answer": "C. Jupiter"},
            {"question": "Which planet is closest to the Sun?", "answer": "B. Mercury"},
            {"question": "Which planet is famous for its beautiful rings?", "answer": "B. Saturn"},
            {"question": "What is the name of Earth's natural satellite?", "answer": "B. Moon"},
            {"question": "Which planet is known as the Blue Planet?", "answer": "A. Earth"},
            {"question": "How many planets are in the Solar System?", "answer": "B. 8"},
            {"question": "Which planet is famous for the Great Red Spot?", "answer": "C. Jupiter"},
            {"question": "Which planet is the hottest in our Solar System?", "answer": "B. Venus"},
            {"question": "The Sun is a...", "answer": "B. Star"}
        ]

    options = [
            ["A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"],
            ["A. Saturn", "B. Earth", "C. Jupiter", "D. Neptune"],
            ["A. Venus", "B. Mercury", "C. Earth", "D. Mars"],
            ["A. Uranus", "B. Saturn", "C. Jupiter", "D. Neptune"],
            ["A. Titan", "B. Moon", "C. Europa", "D. Phobos"],
            ["A. Earth", "B. Neptune", "C. Uranus", "D. Venus"],
            ["A. 7", "B. 8", "C. 9", "D. 10"],
            ["A. Saturn", "B. Mars", "C. Jupiter", "D. Neptune"],
            ["A. Mercury", "B. Venus", "C. Mars", "D. Earth"],
            ["A. Planet", "B. Star", "C. Galaxy", "D. Comet"]
        ]
    points = 0
    for question_num in range(len(question_bank)):
            print(f"Question {question_num + 1}: {question_bank[question_num]['question']}")
            for option in options[question_num]:
                print(option)
            user_answer = input("Enter your answer (A, B, C, or D): ")
            if user_answer.upper() == question_bank[question_num]['answer'][0]:
                print("Correct!")
                points += 1
            else:
                print(f"Incorrect! The correct answer is: {question_bank[question_num]['answer']}")
            print()
    print(f"Quiz completed! Your score is: {points}/{len(question_bank)}")

def general_knowledge_quiz():
    print("Welcome to the General Knowledge Quiz!")
    question_bank = [
        {"question": "What is the capital of India?", "answer": "B. New Delhi"},
        {"question": "How many days are there in a leap year?", "answer": "C. 366"},
        {"question": "Which is the largest ocean on Earth?", "answer": "C. Pacific"},
        {"question": "Who invented the telephone?", "answer": "C. Alexander Graham Bell"},
        {"question": "Which is the national animal of India?", "answer": "C. Tiger"},
        {"question": "Which gas do humans breathe in to survive?", "answer": "B. Oxygen"},
        {"question": "Which is the smallest continent?", "answer": "B. Australia"},
        {"question": "Which festival is known as the Festival of Lights?", "answer": "B. Diwali"},
        {"question": "Which is the fastest land animal?", "answer": "C. Cheetah"},
        {"question": "Which country is famous for the Eiffel Tower?", "answer": "C. France"}
    ]

    options = [
        ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        ["A. 364", "B. 365", "C. 366", "D. 367"],
        ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        ["A. Thomas Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Isaac Newton"],
        ["A. Lion", "B. Elephant", "C. Tiger", "D. Peacock"],
        ["A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"],
        ["A. Europe", "B. Australia", "C. Antarctica", "D. South America"],
        ["A. Holi", "B. Diwali", "C. Eid", "D. Christmas"],
        ["A. Lion", "B. Tiger", "C. Cheetah", "D. Leopard"],
        ["A. Germany", "B. Italy", "C. France", "D. Spain"]
    ]
    points = 0
    for question_num in range(len(question_bank)):
                print(f"Question {question_num + 1}: {question_bank[question_num]['question']}")
                for option in options[question_num]:
                    print(option)
                user_answer = input("Enter your answer (A, B, C, or D): ")
                if user_answer.upper() == question_bank[question_num]['answer'][0]:
                    print("Correct!")
                    points += 1
                else:
                    print(f"Incorrect! The correct answer is: {question_bank[question_num]['answer']}")
                print()
    print(f"Quiz completed! Your score is: {points}/{len(question_bank)}")

def geography_quiz():
    print("Welcome to the Geography Quiz!")

    question_bank = [
        {"question": "Which is the longest river in the world?", "answer": "B. Nile"},
        {"question": "Which is the highest mountain in the world?", "answer": "C. Mount Everest"},
        {"question": "Which desert is the largest hot desert in the world?", "answer": "B. Sahara"},
        {"question": "Which continent is India located in?", "answer": "B. Asia"},
        {"question": "Which ocean lies to the south of India?", "answer": "C. Indian Ocean"},
        {"question": "Which country has the largest population?", "answer": "B. India"},
        {"question": "What is the capital of Japan?", "answer": "C. Tokyo"},
        {"question": "Which is the largest continent?", "answer": "B. Asia"},
        {"question": "Which line divides Earth into the Northern and Southern Hemispheres?", "answer": "B. Equator"},
        {"question": "Which country is known as the Land of the Rising Sun?", "answer": "C. Japan"}
    ]

    options = [
        ["A. Amazon", "B. Nile", "C. Ganga", "D. Yangtze"],
        ["A. Kanchenjunga", "B. K2", "C. Mount Everest", "D. Annapurna"],
        ["A. Gobi", "B. Sahara", "C. Thar", "D. Arabian"],
        ["A. Europe", "B. Asia", "C. Africa", "D. Australia"],
        ["A. Atlantic Ocean", "B. Arctic Ocean", "C. Indian Ocean", "D. Pacific Ocean"],
        ["A. China", "B. India", "C. United States", "D. Indonesia"],
        ["A. Osaka", "B. Kyoto", "C. Tokyo", "D. Hiroshima"],
        ["A. Africa", "B. Asia", "C. Europe", "D. North America"],
        ["A. Tropic of Cancer", "B. Equator", "C. Prime Meridian", "D. Tropic of Capricorn"],
        ["A. China", "B. South Korea", "C. Japan", "D. Thailand"]
    ]

    points = 0
    for question_num in range(len(question_bank)):
                print(f"Question {question_num + 1}: {question_bank[question_num]['question']}")
                for option in options[question_num]:
                    print(option)
                user_answer = input("Enter your answer (A, B, C, or D): ")
                if user_answer.upper() == question_bank[question_num]['answer'][0]:
                    print("Correct!")
                    points += 1
                else:
                    print(f"Incorrect! The correct answer is: {question_bank[question_num]['answer']}")
                print()
    print(f"Quiz completed! Your score is: {points}/{len(question_bank)}")

def history_quiz():
    print("Welcome to the History Quiz!")

    question_bank = [
        {"question": "Who was the first Prime Minister of India?", "answer": "B. Jawaharlal Nehru"},
        {"question": "In which year did India gain independence?", "answer": "B. 1947"},
        {"question": "Who built the Taj Mahal?", "answer": "B. Shah Jahan"},
        {"question": "Who discovered America?", "answer": "B. Christopher Columbus"},
        {"question": "Which war ended in 1945?", "answer": "B. World War II"},
        {"question": "Who is known as the Father of the Nation in India?", "answer": "B. Mahatma Gandhi"},
        {"question": "Who was the first President of India?", "answer": "A. Rajendra Prasad"},
        {"question": "Which civilization built the pyramids?", "answer": "B. Egyptians"},
        {"question": "Who found the sea route to India in 1498?", "answer": "B. Vasco da Gama"},
        {"question": "The Great Wall is located in which country?", "answer": "B. China"}
    ]

    options = [
        ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Sardar Patel", "D. Lal Bahadur Shastri"],
        ["A. 1945", "B. 1947", "C. 1950", "D. 1930"],
        ["A. Akbar", "B. Shah Jahan", "C. Aurangzeb", "D. Humayun"],
        ["A. Vasco da Gama", "B. Christopher Columbus", "C. Ferdinand Magellan", "D. James Cook"],
        ["A. World War I", "B. World War II", "C. Cold War", "D. Crimean War"],
        ["A. Bhagat Singh", "B. Mahatma Gandhi", "C. Subhas Chandra Bose", "D. Jawaharlal Nehru"],
        ["A. Rajendra Prasad", "B. A. P. J. Abdul Kalam", "C. Jawaharlal Nehru", "D. Sardar Vallabhbhai Patel"],
        ["A. Romans", "B. Egyptians", "C. Greeks", "D. Persians"],
        ["A. Christopher Columbus", "B. Vasco da Gama", "C. Ferdinand Magellan", "D. Marco Polo"],
        ["A. India", "B. China", "C. Japan", "D. Mongolia"]
    ]

    points = 0
    for question_num in range(len(question_bank)):
                print(f"Question {question_num + 1}: {question_bank[question_num]['question']}")
                for option in options[question_num]:
                    print(option)
                user_answer = input("Enter your answer (A, B, C, or D): ")
                if user_answer.upper() == question_bank[question_num]['answer'][0]:
                    print("Correct!")
                    points += 1
                else:
                    print(f"Incorrect! The correct answer is: {question_bank[question_num]['answer']}")
                print()
    print(f"Quiz completed! Your score is: {points}/{len(question_bank)}")

def programming_quiz():
    print("Welcome to the Programming Quiz!")

    question_bank = [
        {"question": "Which programming language are you learning now?", "answer": "B. Python"},
        {"question": "Which symbol is used to write comments in Python?", "answer": "B. #"},
        {"question": "Which function is used to display output in Python?", "answer": "B. print()"},
        {"question": "Which function is used to get user input in Python?", "answer": "A. input()"},
        {"question": "Which data type stores True or False values?", "answer": "C. bool"},
        {"question": "Which loop repeats while a condition is True?", "answer": "B. while"},
        {"question": "Which keyword is used to define a function in Python?", "answer": "B. def"},
        {"question": "Which collection stores key-value pairs?", "answer": "C. Dictionary"},
        {"question": "Which module is commonly used to generate random numbers?", "answer": "B. random"},
        {"question": "Which operator checks if two values are equal?", "answer": "B. =="}
    ]

    options = [
        ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
        ["A. //", "B. #", "C. <!-- -->", "D. %%"],
        ["A. display()", "B. print()", "C. output()", "D. echo()"],
        ["A. input()", "B. read()", "C. scan()", "D. get()"],
        ["A. int", "B. str", "C. bool", "D. float"],
        ["A. for", "B. while", "C. do-while", "D. repeat"],
        ["A. function", "B. def", "C. fun", "D. define"],
        ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        ["A. math", "B. random", "C. os", "D. time"],
        ["A. =", "B. ==", "C. !=", "D. >="]
    ]

    points = 0
    for question_num in range(len(question_bank)):
                print(f"Question {question_num + 1}: {question_bank[question_num]['question']}")
                for option in options[question_num]:
                    print(option)
                user_answer = input("Enter your answer (A, B, C, or D): ")
                if user_answer.upper() == question_bank[question_num]['answer'][0]:
                    print("Correct!")
                    points += 1
                else:
                    print(f"Incorrect! The correct answer is: {question_bank[question_num]['answer']}")
                print()
    print(f"Quiz completed! Your score is: {points}/{len(question_bank)}")


def menu():
    while True:
        print("----------------------------")
        print("Welcome to the Quiz Game!")
        print("----------------------------")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            print("Which category would you like to choose?")
            print("1. Space Quiz")
            print("2. General Knowledge Quiz")
            print("3. Geography Quiz")
            print("4. History Quiz")
            print("5. Programming Quiz")
            category_choice = input("Enter your choice (1-5): ")
            if category_choice == '1':
                print("Starting Space Quiz...")
                Space_Quiz()
            elif category_choice == '2':
                print("Starting General Knowledge Quiz...")
                general_knowledge_quiz()
            elif category_choice == '3':
                print("Starting Geography Quiz...")
                geography_quiz()
            elif category_choice == '4':
                print("Starting History Quiz...")
                history_quiz()
            elif category_choice == '5':
                print("Starting Programming Quiz...")
                programming_quiz()
            else:
                print("Invalid choice. Please try again.")
        elif choice == "2":
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def main():
    menu()

main()