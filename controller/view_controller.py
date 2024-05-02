import customtkinter as ctk
from view.start_view import StartView
from view.tutorial_view import TutorialView
from view.game_view import GameView
from view.settings_view import SettingsView

class ViewController(ctk.CTk):
    def __init__(self, *args, **kwargs):
        
        # Views
        self.views = {}
        self.views["start"] = StartView(self)
        self.views["tutorial"] = TutorialView(self)
        self.views["game"] = GameView(self)
        self.views["settings"] = SettingsView(self)
        
        # Show the start view
        self.show_view("start")
        
    def show_view(self, view_name):
        # Hide all views
        for view in self.views.values():
            view.pack_forget()
            
        # Show the selected view
        view = self.views[view_name]
        view.pack(fill="both", expand=True)
        