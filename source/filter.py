import customtkinter
import lang
from source.filter_state import filter_state

#set language
curlang = lang.english

def button_callback():
    print("button clicked")

class FilterFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        filter_red = filter_state.IGNORE
        filter_white = filter_state.IGNORE

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)

        text_red = customtkinter.CTkTextbox(self, width=100, height=20, corner_radius=0 )
        text_red.insert("0.0", curlang.check_red)
        text_red.pack(padx=20, pady=20)
        text_red.configure(state="disabled")

        button = customtkinter.CTkButton(self, text=curlang.search, command=button_callback)
        button.pack(padx=20, pady=20)
