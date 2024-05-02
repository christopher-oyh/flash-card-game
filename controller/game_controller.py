import operator
import time

class GameController:
    def __init__(self):
        # Define operations
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        # Track combinations
        self.combinations = set()
        

        # Initialize score
        self.score = 0

        # Initialize timer
        self.time_limit = 60  # Set the time limit in seconds
        self.start_time = time.time()
    
    def new_question(self):
        global num1, num2, op
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        op = random.choice(list(self.operations.keys()))

        # Ensure division is valid
        if op == '/' and num2 == 0:
            return self.new_question()

        # Ensure combination hasn't been used
        if (num1, num2, op) in self.combinations:
            return self.new_question()

        # Add combination to set
        self.combinations.add((num1, num2, op))

        self.question_label.config(text=f"What's {num1} {op} {num2}? ")

    def check_answer(self):
        print("Checking answer")
        self.score += 1
        print(f"Score: {self.score}")
        # user_answer = float(self.answer_entry.get())
        # if user_answer == self.operations[op](num1, num2):
        #     self.score += 1
        # else:
        #     self.score -= 1
        # self.score_label.config(text=f"Score: {self.score}")
        # self.answer_entry.delete(0, ctk.END)
        # self.new_question()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = int(self.time_limit - elapsed_time)
        self.timer_label.config(text=f"Time: {remaining_time} seconds")

        # Check if time is up
        if elapsed_time >= self.time_limit:
            # Return to the start view
            self.controller.show_view("start")
        else:
            # Call update_timer again after 1000 milliseconds (1 second)
            self.after(1000, self.update_timer)
    
    def start_game(self):
        self.new_question()
        self.update_timer()
        
        self.pack(fill="both", expand=True)