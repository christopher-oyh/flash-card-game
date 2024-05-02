import customtkinter as ctk

class GameView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        
        # Title
        title = ctk.CTkLabel(self, text="Flash Card Game", font=("Arial", 24))
        title.pack(pady=10)
        
        # Score
        score_label = ctk.CTkLabel(self, text="Score: 0", font=("Arial", 18))
        score_label.pack(pady=10)
        
        # Timer
        timer_label = ctk.CTkLabel(self, text="Time: 60", font=("Arial", 18))
        timer_label.pack(pady=10)
        
        # Question
        question_label = ctk.CTkLabel(self, text="Question: 2 x 3", font=("Arial", 18))
        question_label.pack(pady=10)
        
        # Answer Entry
        answer_entry = ctk.CTkEntry(self, font=("Arial", 18))
        answer_entry.pack(pady=10)
        
        # Submit Button
        submit_button = ctk.CTkButton(self, text="Submit", font=("Arial", 18))
        submit_button.pack(pady=10)
        
        # Next Button
        end_button = ctk.CTkButton(self, text="End Game", font=("Arial", 18))
        end_button.pack(pady=10)
        
        # Pack the frame
        # self.pack(fill="both", expand=True)
        