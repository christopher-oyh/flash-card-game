import customtkinter as ctk

class StartView(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.configure(bg="red")
        
        # Title
        title = ctk.CTkLabel(self, text="Simple Flash Card Game", font=("Arial", 24))
        title.pack(pady=10)
        
        # Button
        start_button = ctk.CTkButton(self, text="Start", font=("Arial", 18))
        start_button.pack(pady=10)
        
        tutorial_button = ctk.CTkButton(self, text="Help", font=("Arial", 18))
        tutorial_button.pack(pady=10)
        
        settings_button = ctk.CTkButton(self, text="Settings", font=("Arial", 18))
        settings_button.pack(pady=10)
        
        # Button
        quit_button = ctk.CTkButton(self, text="Quit", font=("Arial", 18))
        quit_button.pack(pady=10)
        
        # Pack the frame
        # self.pack(fill="both", expand=True)
        
        