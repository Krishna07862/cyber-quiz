
import random

questions = [
    ("What does CPU stand for?",
     ["Central Processing Unit", "Computer Power Utility",
      "Central Program User", "Control Processing User"], 0),

    ("Which keyword defines a function in Python?",
     ["func", "define", "def", "function"], 2),

    ("Which symbol starts a comment in Python?",
     ["//", "#", "/*", "--"], 1),

    ("What is the output of print(2 + 3)?",
     ["23", "6", "5", "Error"], 2),

    ("Which data type stores True or False?",
     ["str", "int", "list", "bool"], 3),

    ("Which Python function displays output?",
     ["input()", "print()", "show()", "output()"], 1),

    ("Which keyword repeats code while a condition is true?",
     ["repeat", "loop", "while", "again"], 2),

    ("Which collection stores multiple items in order?",
     ["list", "integer", "boolean", "float"], 0),

    ("Which operator checks equality in Python?",
     ["=", "==", "!=", ":="], 1),

    ("Which keyword is used to make a decision?",
     ["if", "loop", "def", "import"], 0),

    ("What does IP stand for?",
     ["Internet Protocol", "Internal Program",
      "Information Port", "Internet Password"], 0),

    ("Which IP address is a private IPv4 address?",
     ["8.8.8.8", "1.1.1.1", "192.168.1.10", "142.250.1.1"], 2),

    ("What is the main purpose of DNS?",
     ["Encrypt files", "Translate domain names to IP addresses",
      "Remove viruses", "Create passwords"], 1),

    ("Which protocol is commonly used to load secure websites?",
     ["FTP", "HTTP only", "HTTPS", "SMTP"], 2),

    ("What does a router commonly do?",
     ["Route traffic between networks", "Write Python code",
      "Store passwords only", "Scan documents"], 0),

    ("Which command displays your current directory in Termux?",
     ["where", "pwd", "showdir", "current"], 1),

    ("Which command lists files in a directory?",
     ["ls", "cd", "pwd", "clear"], 0),

    ("Which command changes your directory?",
     ["mv", "mkdir", "cd", "cat"], 2),

    ("Which command installs packages in Termux?",
     ["aptweb", "pkg install", "python install", "getpkg"], 1),

    ("Which command runs a Python file named quiz.py?",
     ["run quiz.py", "start quiz.py", "python quiz.py",
      "open python"], 2),

    ("What is phishing?",
     ["A method of compressing files",
      "A trick to steal information by impersonation",
      "A Python data type", "A network cable"], 1),

    ("What is the purpose of multi-factor authentication?",
     ["Make passwords public", "Disable updates",
      "Add another layer of account verification",
      "Remove usernames"], 2),

    ("Which is the strongest password practice?",
     ["Reuse one password everywhere",
      "Use a long, unique password for each account",
      "Use your name only", "Share passwords with friends"], 1),

    ("What does a firewall help do?",
     ["Control network traffic using rules",
      "Increase screen brightness", "Write programs",
      "Recover deleted photos automatically"], 0),

    ("What is ethical hacking?",
     ["Accessing any system without permission",
      "Testing security with authorization",
      "Stealing account details", "Hiding malware"], 1),

    ("What is the main purpose of Nmap?",
     ["Edit photos", "Create spreadsheets",
      "Explore hosts and network services",
      "Generate music"], 2),

    ("What does a software vulnerability mean?",
     ["A weakness that could be exploited",
      "A strong password", "A system backup",
      "A programming language"], 0),

    ("What should you do before testing someone else's system?",
     ["Start scanning immediately", "Get clear authorization",
      "Guess their password", "Disable their firewall"], 1),

    ("What is a hash commonly used for in security?",
     ["Reversibly encrypt every file",
      "Create a fixed-length digest of data",
      "Find a person's exact location",
      "Increase internet speed"], 1),

    ("What should you do if you discover a security flaw?",
     ["Exploit it on other systems",
      "Publish private user data",
      "Report it responsibly to the owner",
      "Sell stolen credentials"], 2)
]


def play_game():
    score = 0
    random.shuffle(questions)

    print("\n" + "=" * 42)
    print("   PYTHON & CYBERSECURITY QUIZ")
    print("=" * 42)
    print("30 Questions | Beginner Level")
    print("Choose A, B, C or D.\n")

    for number, (question, options, answer) in enumerate(questions, 1):
        print(f"\nQuestion {number}/30")
        print(question)

        for i, option in enumerate(options):
            print(f"  {chr(65 + i)}. {option}")

        while True:
            choice = input("Your answer (A/B/C/D): ").strip().upper()
            if choice in ("A", "B", "C", "D"):
                break
            print("Please enter A, B, C or D.")

        selected = ord(choice) - ord("A")

        if selected == answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect.")
            print("Correct answer:", chr(65 + answer) + ".", options[answer])

    print("\n" + "=" * 42)
    print("             QUIZ RESULTS")
    print("=" * 42)
    print(f"Your score: {score}/30")
    print(f"Percentage: {score / 30 * 100:.1f}%")

    if score >= 27:
        print("Excellent! Outstanding work!")
    elif score >= 21:
        print("Great job! Keep learning.")
    elif score >= 15:
        print("Good start. Practise a little more.")
    else:
        print("Keep going! Review the basics and try again.")

    print("=" * 42)

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        play_game()
    else:
        print("Thanks for playing. Keep learning ethically!")


if __name__ == "__main__":
    play_game()

