import customtkinter as ctk
import random

class TutorialView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        
        # Add Padding to Top
        self.top_padding = ctk.CTkLabel(self, text="", font=("Arial", 24))
        self.top_padding.pack(pady=50)
        
        # Title
        title = ctk.CTkLabel(self, text="How to Play", font=("Arial", 24))
        title.pack(pady=10)
    
        # Text
        text = ctk.CTkLabel(self, font=("Arial", 12))
        instructions = """
        Welcome to the Flash Card Game! Here's how to play:
        
            1. Start the game by clicking the "Start" button.
            
            2. You will be presented with a series of math questions.
            
            3. Enter your answer in the text box and click the "Submit" button.
            
            4. You will earn points for each correct answer.
            
            5. The game will continue until the time runs out or you click the "End Game" button.
            
            6. Have fun and test your math skills!
    
        """
        text.configure(text=instructions, justify="left")
        text.pack(pady=10)
        
        
        # Button
        start_button = ctk.CTkButton(self, text="Start", font=("Arial", 18) , command=lambda: controller.show_view("game"))
        start_button.pack(pady=10)
        
        back_button = ctk.CTkButton(self, text="Back", font=("Arial", 18), command=lambda: controller.show_view("start"))
        back_button.pack(pady=10)
        
        # Pack the frame
        self.pack(fill="both", expand=True)
        
        