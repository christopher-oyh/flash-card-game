import customtkinter as ctk

class SettingsView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        
        # Add Padding to Top
        self.top_padding = ctk.CTkLabel(self, text="", font=("Arial", 24))
        self.top_padding.pack(pady=50)
        
        # Title
        title = ctk.CTkLabel(self, text="Settings", font=("Arial", 24))
        title.pack(pady=10)
    
        # Text
        text = ctk.CTkLabel(self, font=("Arial", 12))
        # instructions = """
        # Settings:
        
        # 1. Timer: Set the timer duration for the game. The timer is set in seconds, and the default is 60 seconds.
        
        # 2. Number Range: Set the range of numbers for the game. The default range is from 0 to 12.
        
        # 3. Operations: Select the arithmetic operations to include in the game. The default operations are addition, subtraction, multiplication, and division.
        
        # 4. Number of Questions: Set the number of questions to include in the game. The default is 10 questions.
        
        # 5. Save Settings: Save the current settings for the game.
        
        # 6. Reset Settings: Reset the settings to the default values.
        # """
        text.configure(text="WORK IN PROGRESS", justify="left")
        text.pack(pady=10)
        
        # Button
        save_button = ctk.CTkButton(self, text="Save", font=("Arial", 18))
        save_button.pack(pady=10)
        
        # Button
        reset_button = ctk.CTkButton(self, text="Reset", font=("Arial", 18))
        reset_button.pack(pady=10)
        
        # Button
        back_button = ctk.CTkButton(self, text="Back", font=("Arial", 18), command=lambda: controller.show_view("start"))
        back_button.pack(pady=10)
        
        # Pack the frame
        # self.pack(fill="both", expand=True)