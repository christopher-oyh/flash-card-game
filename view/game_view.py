import customtkinter as ctk
import threading
import operator
import random
import time
from controller.game_controller import GameController

class GameView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        # # Initialize the GameController
        self.game_controller = GameController()    
        
        # Initialize score
        self.score = 0

        # Initialize timer
        self.time_limit = 10  # Set the time limit in seconds
        self.start_time = time.time()    
        
        self.num1 = 0
        self.num2 = 1
        self.op = "/"
        
        # Title
        self.title = ctk.CTkLabel(self, text="Flash Card Game", font=("Arial", 24))
        self.title.pack(pady=10)
        
        # Score
        self.score_label = ctk.CTkLabel(self, text="Score: {}".format(self.score), font=("Arial", 18))
        self.score_label.pack(pady=10)
        
        # Timer
        self.timer_label = ctk.CTkLabel(self, text="Time: {} seconds".format(self.time_limit), font=("Arial", 18))
        self.timer_label.pack(pady=10)
        
        # Question
        self.question_label = ctk.CTkLabel(self, text="Question: {} {} {}".format(self.num1, self.op, self.num2), font=("Arial", 18))
        self.question_label.pack(pady=10)
        
        # Answer Entry
        self.answer_entry = ctk.CTkEntry(self, font=("Arial", 18) )
        self.answer_entry.pack(pady=10)
        
        # Submit Button
        self.submit_button = ctk.CTkButton(self, text="Submit", font=("Arial", 18), command=self.check_answer)    
        self.submit_button.pack(pady=10)
        
        # End Button
        self.end_button = ctk.CTkButton(self, text="End Game", font=("Arial", 18) , command=lambda: controller.show_view("start"))
        self.end_button.pack(pady=10)
        
        # Start/Restart the game
        self.restart_button = ctk.CTkButton(self, text="Start/Restart", font=("Arial", 18), command=self.start_game)
        self.restart_button.pack(pady=10)
    
    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = int(self.time_limit - elapsed_time)
        self.timer_label.configure(text=f"Time: {remaining_time} seconds")
        print("Remaining Time: ", remaining_time)
        # Check if time is up
        if elapsed_time >= self.time_limit:
            # Return to the start view
            # self.controller.show_view("start")
            print("Time is up")
        else:
            # Call update_timer again after 1000 milliseconds (1 second)
            self.after(1000, self.update_timer)
    
    def start_game(self):
        self.time_limit = 10
        self.start_time = time.time()
        self.score = 0
        self.update_values()
        self.update_timer()
        

        
    def update_values(self):
        print("Updating values")
        # Update values to the GUI
        self.score_label.configure(text="Score: {}".format(self.score))
        self.answer = self.answer_entry.get()
        self.answer_entry.delete(0, ctk.END)
        self.new_question()
        
    def new_question(self):
        self.num1 = random.randint(0, 12)
        self.num2 = random.randint(0, 12)
        self.op = random.choice(list(self.game_controller.operations.keys()))
        
        # Ensure division is valid
        if self.op == '/' and self.num2 == 0:
            return self.new_question()
        # print("New Question", self.num1, self.op, self.num2)
        self.question_label.configure(text="Question: {} {} {}".format(self.num1, self.op, self.num2))

        
    def check_answer(self):
        # Compute the correct answer
        user_answer = int(self.answer_entry.get())
        correct_answer = None
        if self.op == '+':
            correct_answer = self.num1 + self.num2
        elif self.op == '-':
            correct_answer = self.num1 - self.num2
        elif self.op == '*':
            correct_answer = self.num1 * self.num2
        elif self.op == '/':
            correct_answer = self.num1 / self.num2
        
        # Check if the answer is correct
        # print("User Answer", user_answer)
        # print("Correct Answer", correct_answer)
        if user_answer == correct_answer:
            self.score += 1
        else:
            self.score -= 1
        self.score_label.configure(text="Score: {}".format(self.score)) 
        self.update_values()
        
        
    
    
        
    
    
 