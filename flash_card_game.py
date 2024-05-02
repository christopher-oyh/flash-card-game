import customtkinter as ctk

# Import the AppConfig class from the app_config module
from model.app_config import AppConfig

from view.start_view import StartView
from view.tutorial_view import TutorialView

class FlashCardGame(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(AppConfig.WINDOW_TITLE)
        self.geometry(f"{AppConfig.WINDOW_WIDTH}x{AppConfig.WINDOW_HEIGHT}")
        # self.configure(bg=AppConfig.BACKGROUND_COLOR)
        
        self.start_view = StartView(self)
        self.start_view.pack(fill="both", expand=True)
        
        # ctk container
        # container = ctk.CTkFrame(self)
        # container.pack(fill="both", expand=True)
        
        # Initializing views
        self.views = {}
        
        # for F in (StartView, TutorialView):
        #     # print("AA",F)
        #     frame = F(container, self)
        #     self.views[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")
        
        # print(self.views)
        
        # self.show_view(StartView)
    
        
        # Show the start view
        # start_view = StartView(self, )
        
        
    # def show_view(self, cont):
    #     view = self.views[cont]
    #     view.tkraise()

def main():
    app = FlashCardGame()
    app.mainloop()
    
if __name__ == "__main__":
    main()
