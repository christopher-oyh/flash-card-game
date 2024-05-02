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

# Initialize timer
time_limit = 60  # Set the time limit in seconds
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

def update_timer():
    elapsed_time = time.time() - start_time
    remaining_time = int(time_limit - elapsed_time)
    timer_label.config(text=f"Time: {remaining_time} seconds")

    # Check if time is up
    if elapsed_time >= time_limit:
        root.quit()  # Exit the application when time is up
    else:
        # Call update_timer again after 1000 milliseconds (1 second)
        root.after(1000, update_timer)

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

timer_label = tk.Label(root, text=f"Time: {time_limit} seconds")
timer_label.pack()

# Start game and timer
new_question()
update_timer()

# Run the event loop
root.mainloop()