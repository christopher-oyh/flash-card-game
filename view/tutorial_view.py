import customtkinter as ctk

class TutorialView(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg="blue")
        
        # Title
        title = ctk.CTkLabel(self, text="Tutorial", font=("Arial", 24))
        title.pack(pady=10)
        
        # Button
        start_button = ctk.CTkButton(self, text="Start", font=("Arial", 18))
        start_button.pack(pady=10)
        
        # Button
        quit_button = ctk.CTkButton(self, text="Quit", font=("Arial", 18))
        quit_button.pack(pady=10)
        
        # Pack the frame
        self.pack(fill="both", expand=True)
        
        