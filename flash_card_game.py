import customtkinter as ctk

# Import the AppConfig class from the app_config module
from model.app_config import AppConfig
from view.start_view import StartView
from view.tutorial_view import TutorialView
from view.game_view import GameView
from view.settings_view import SettingsView
from controller.view_controller import ViewController


class FlashCardGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(AppConfig.WINDOW_TITLE)
        self.geometry(f"{AppConfig.WINDOW_WIDTH}x{AppConfig.WINDOW_HEIGHT}")
        # self.configure(bg=AppConfig.BACKGROUND_COLOR)
        
        # # Root Frame
        # main_container = ctk.CTkFrame(self)
        # main_container.pack(fill="both", expand=True)
        
        # Views
        self.views = {}
        self.views["start"] = StartView(parent=self, controller=self)
        self.views["tutorial"] = TutorialView(parent=self, controller=self)
        self.views["game"] = GameView(parent=self, controller=self)
        self.views["settings"] = SettingsView(parent=self, controller=self)
        
        # Show the start view
        self.show_view("start")
        
    def show_view(self, view_name):
        # Hide all views
        for view in self.views.values():
            view.pack_forget()
            
        # Show the selected view
        view = self.views[view_name]
        view.pack(fill="both", expand=True)
        
        
        
        
        
        
        


def main():
    app = FlashCardGame()
    app.mainloop()
    
if __name__ == "__main__":
    main()
