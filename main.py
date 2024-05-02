import tkinter as tk
import random
import time
import operator

# Define operations
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

# Track combinations
combinations = set()

# Initialize score
score = 0

# Start timer
start_time = time.time()

def new_question():
    global num1, num2, op
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    op = random.choice(list(operations.keys()))

    # Ensure division is valid
    if op == '/' and num2 == 0:
        return new_question()

    # Ensure combination hasn't been used
    if (num1, num2, op) in combinations:
        return new_question()

    # Add combination to set
    combinations.add((num1, num2, op))

    question_label.config(text=f"What's {num1} {op} {num2}? ")

def check_answer():
    global score
    user_answer = float(answer_entry.get())
    if user_answer == operations[op](num1, num2):
        score += 1
    else:
        score -= 1
    score_label.config(text=f"Score: {score}")
    answer_entry.delete(0, tk.END)
    new_question()

# Create a window
root = tk.Tk()

# Add widgets
question_label = tk.Label(root, text="")
question_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()

check_button = tk.Button(root, text="Check answer", command=check_answer)
check_button.pack()

score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Start game
new_question()

# Run the event loop
root.mainloop()
