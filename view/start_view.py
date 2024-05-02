import customtkinter as ctk

class StartView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        # self.configure(bg="red")
        
        # Button
        start_button = ctk.CTkButton(self, text="Start", font=("Arial", 18), command=lambda: controller.show_view("game"))
        start_button.pack(pady=10)
        
        tutorial_button = ctk.CTkButton(self, text="Help", font=("Arial", 18), command=lambda: controller.show_view("tutorial"))
        tutorial_button.pack(pady=10)
        
        settings_button = ctk.CTkButton(self, text="Settings", font=("Arial", 18), command=lambda: controller.show_view("settings"))
        settings_button.pack(pady=10)
        
        quit_button = ctk.CTkButton(self, text="Quit", font=("Arial", 18), command=parent.quit)
        quit_button.pack(pady=10)
        # Pack the frame
        # self.pack(fill="both", expand=True)
        
        