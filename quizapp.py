import time

# A dictionary to store users' credentials (username: password)
users = {}

# A function for registration
def register():
    print("Registration")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try another one.")
        return None, None
    password = input("Enter a password: ")
    users[username] = password
    print(f"Registration successful! Welcome, {username}.")
    return username, password

# A function for login
def login():
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print(f"Login successful! Welcome back, {username}.")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

# A function for the quiz
def take_quiz(username):
    print(f"\n{username}, let's start the quiz! Answer the following questions.\n")
    
    questions = [
        ("What is the time complexity of binary search in the worst case?", 
         ["O(n)", "O(log n)", "O(n log n)", "O(1)"], 1),
        ("Which data structure uses LIFO (Last In, First Out)?", 
         ["Queue", "Stack", "Array", "Hash Table"], 1),
        ("What is the output of `print(2**3)` in Python?", 
         ["6", "8", "9", "16"], 1),
        ("Which of the following is mutable in Python?", 
         ["Tuple", "String", "List", "Integer"], 2),
        ("What is the SQL command to retrieve data from a database?", 
         ["INSERT", "UPDATE", "SELECT", "DELETE"], 2),
        ("Which algorithm is used to find the shortest path in a graph?", 
         ["DFS", "Dijkstra's", "Merge Sort", "Prim's"], 1),
        ("What does `len([1, 2, 3, 4])` return in Python?", 
         ["3", "4", "5", "Error"], 1),
        ("What is the primary key in a database?", 
         ["A unique identifier", "A duplicate entry", "A secondary key", "None of these"], 0),
        ("Which of the following is a Python tuple?", 
         ["[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", "None of these"], 2),
        ("Which sorting algorithm has the best average case time complexity?", 
         ["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"], 2),
        ("What is the role of a foreign key in a database?", 
         ["To uniquely identify each record", "To link tables", "To store indices", "None of these"], 1),
        ("What does `time.sleep(2)` do in Python?", 
         ["Halts execution for 2 seconds", "Pauses input for 2 seconds", "Stops program", "None of these"], 0),
        ("Which of the following is used for joining tables in SQL?", 
         ["GROUP BY", "JOIN", "ORDER BY", "WHERE"], 1),
        ("What is the default return type of `input()` in Python?", 
         ["Integer", "String", "Float", "Boolean"], 1),
        ("Which traversal technique is used for depth-first search in a graph?", 
         ["Level-order", "In-order", "Post-order", "Pre-order"], 3)
    ]
    
    score = 0

    for idx, (question, options, correct_answer_idx) in enumerate(questions):
        print(f"Q{idx + 1}: {question}")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        
        while True:
            try:
                answer = int(input("Choose your answer (1-4): ")) - 1
                if 0 <= answer <= 3:
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
        
        if answer == correct_answer_idx:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {options[correct_answer_idx]}\n")
        
        time.sleep(1)  # A small delay between questions

    print(f"Quiz finished! Your score is {score} out of {len(questions)}.")

# Main program loop
def main():
    print("Welcome to the Quiz Program!")
    
    while True:
        choice = input("Do you want to [1] Register, [2] Login, or [3] Exit: ").strip()

        if choice == '1':
            username, password = register()
            if username:
                take_quiz(username)
        elif choice == '2':
            username = login()
            if username:
                take_quiz(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
