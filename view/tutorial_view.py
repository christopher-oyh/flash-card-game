import customtkinter as ctk
import random

class TutorialView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        # self.configure(bg="blue")
        
        # Title
        title = ctk.CTkLabel(self, text="How to Play", font=("Arial", 24))
        title.pack(pady=10)
    
        # Text
        text = ctk.CTkTextbox(self, font=("Arial", 12))
        instructions = """
        Welcome to the Flash Card Game! Here's how to play:

        1. Start the Game: Launch the Flash Card Game program. This game is designed to help you practice multiplication tables, as well as other basic arithmetic operations.

        2. First Question: The game will generate two random numbers between zero and 12 and display them on the screen, asking you to multiply them.

        3. Input Your Answer: Enter your answer into the input field and submit it.

        4. Check Your Answer: The game will check if your answer is correct or incorrect. If your answer is correct, you will be awarded one point and the game will generate two more numbers for the next question. If your answer is incorrect, one point will be subtracted from your score.

        5. Keep Playing: Continue answering the questions as quickly as you can. The game includes a timer, and the goal is to achieve the highest score in one minute of play. 

        6. Other Operations: As you progress, the game will also include questions involving addition (+), subtraction (-), and division (÷).

        7. Track Your Progress: The game keeps track of which number combinations have been shown to ensure that all 225 pairs are guaranteed to be shown eventually.

        8. End of Game: When the timer runs out, the game ends. Your final score is the total number of correct answers minus the total number of incorrect answers. Starting a new game resets the score to zero.

        Remember, the goal is to answer as many questions correctly as you can within the time limit. Good luck!
        """
        text.insert(ctk.END, instructions)
        text.pack(pady=10)
        
        
        # Button
        start_button = ctk.CTkButton(self, text="Start", font=("Arial", 18) , command=lambda: controller.show_view("game"))
        start_button.pack(pady=10)
        
        back_button = ctk.CTkButton(self, text="Back", font=("Arial", 18), command=lambda: controller.show_view("start"))
        back_button.pack(pady=10)
        
        # Pack the frame
        self.pack(fill="both", expand=True)
        
        