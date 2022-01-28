# Text Encoding Program

# This program is to take a string of text and then make it all different so it can't be read
# Then there will a decoding section to ensure that it can be reversed and read as per normal again


import tkinter as tk
from tkinter.ttk import *
from FrameMain import *
from functions import *
import pyperclip
from tkinter import ttk


class Window:
    def __init__(self, root, title, geometry):
        # This will set all the base info for the main window
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        
        # Universal variables
        int_padding = 2
        optionmenu_ext_padding_x = (10, 5)
        optionmenu_ext_padding_y = 5
        label_width = 10
        label_ext_padding = (15, 5)
        entry_width = 150
        entry_ext_padding = 10
        button_width = 10
        button_ext_padding = 10

        # # This will create the main notebook for the entire program
        # window = tk.Tk()
        # window.title('Text Cryptographer')
        # window.geometry('800x250')

        FrameMain(root)



        # # To create the frames for each main tab
        # tab_check = tk.Frame(master=window)
        # tab_recommend = tk.Frame(master=notebook_main)
        # # And to add them to the main notebook
        # notebook_main.add(tab_check, text='Check Geared Motor')
        # notebook_main.add(tab_recommend, text='Recommend Geared Motor')

        # # Putting all the frames into the main program now
       
        # FrameCheck(tab_check)



        self.root.mainloop()  # To actually run the program loop


def main():
    window = Window(tk.Tk(), 'Text Cryptographer', '800x250')  # Main window defined here


main()






















# # Universal Variables


# # Creating Main Window



