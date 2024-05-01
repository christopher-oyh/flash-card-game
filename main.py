import tkinter as tk
import random
import operator

class FlashCardGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flash Card Game")
        self.geometry("800x600")

        # Define operations
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        # Initialize score and timer
        self.score = 0
        self.time_left = 60

        # Add your code for creating widgets and setting up the app here
        self.question_label = tk.Label(self, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack()

        self.check_button = tk.Button(self, text="Check answer", command=self.check_answer)
        self.check_button.pack()

        self.score_label = tk.Label(self, text=f"Score: {self.score}")
        self.score_label.pack()

        self.timer_label = tk.Label(self, text=f"Time left: {self.time_left}")
        self.timer_label.pack()

        # Generate the first question
        self.new_question()

        # Start the timer
        self.update_timer()

    def new_question(self):
        self.num1 = random.randint(0, 12)
        self.num2 = random.randint(0, 12)
        self.op = random.choice(list(self.operations.keys()))

        # Ensure division is valid
        if self.op == '/' and self.num2 == 0:
            return self.new_question()

        self.question_label.config(text=f"What's {self.num1} {self.op} {self.num2}? ")

    def check_answer(self):
        user_answer = float(self.answer_entry.get())
        if user_answer == self.operations[self.op](self.num1, self.num2):
            self.score += 1
        else:
            self.score -= 1
        self.score_label.config(text=f"Score: {self.score}")
        self.answer_entry.delete(0, tk.END)
        self.new_question()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.after(1000, self.update_timer)  # Update the timer every 1 second
        else:
            self.check_button.config(state='disabled')  # Disable the button when time is up

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = FlashCardGameApp()
    app.run()