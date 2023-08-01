import tkinter as tk

from interface_game.main_menu import MainMenuPage
from .page import pages


class Aplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Битва Шести Королевств')
        self.geometry('800x600')
        self.resizable(height=False, width=False)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in pages:
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainMenuPage)
        self.mainloop()

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def close_window(self):
        self.destroy()

    def get_page(self, page_class):
        return self.frames[page_class]

    # def on_click(self, event):
    #     button_text = event.widget.cget('text')
