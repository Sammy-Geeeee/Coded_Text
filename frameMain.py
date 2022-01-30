# This is to define the main frame for the program


import tkinter as tk
from functions import *
import pyperclip


class FrameMain(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some variables for the sizing of various things
        int_padding = 2
        optionmenu_ext_padding_x = (10, 5)
        optionmenu_ext_padding_y = 5
        label_width = 10
        label_ext_padding = (15, 5)
        entry_width = 150
        entry_ext_padding = 10
        button_width = 10
        button_ext_padding = 10


        # Creating all the main frames
        self.frame_keys = tk.Frame(master=self.master)
        self.frame_decrypted = tk.Frame(master=self.master)
        self.frame_buttons = tk.Frame(master=self.master)
        self.frame_encrypted = tk.Frame(master=self.master)
        # Packing of each element
        self.frame_keys.pack(expand=1, fill=tk.BOTH)  
        self.frame_decrypted.pack(expand=1, fill=tk.BOTH)
        self.frame_buttons.pack(expand=1, fill=tk.BOTH)
        self.frame_encrypted.pack(expand=1, fill=tk.BOTH)


        # Defining setup for all the key options
        self.chosen_key_1 = tk.StringVar()
        self.chosen_key_2 = tk.StringVar()
        self.chosen_key_3 = tk.StringVar()
        self.chosen_key_4 = tk.StringVar()
        key_options = list(range(1, 25+1))  # To make the list of options for each key
        self.frame_keys.columnconfigure([1, 2, 3, 4], weight=1)  # To change the layout of each column
        
        # Creates all the widgets
        self.label_key = tk.Label(master=self.frame_keys, width=label_width, text='Keys')  
        self.option_key_1 = tk.OptionMenu(self.frame_keys, self.chosen_key_1, *key_options)
        self.option_key_2 = tk.OptionMenu(self.frame_keys, self.chosen_key_2, *key_options)
        self.option_key_3 = tk.OptionMenu(self.frame_keys, self.chosen_key_3, *key_options)
        self.option_key_4 = tk.OptionMenu(self.frame_keys, self.chosen_key_4, *key_options)
        # Positions all the widgets
        self.label_key.grid(row=0, column=0, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=label_ext_padding, pady=label_ext_padding)
        self.option_key_1.grid(row=0, column=1, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)
        self.option_key_2.grid(row=0, column=2, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)
        self.option_key_3.grid(row=0, column=3, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)
        self.option_key_4.grid(row=0, column=4, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)


        # Decryption frame widgets
        self.frame_decrypted.columnconfigure(1, weight=1)  # To change the layout of each column
          # Creates all the widgets
        self.label_input = tk.Label(master=self.frame_decrypted, width=label_width, text='Decrypted')
        self.entry_decrypted = tk.Entry(master=self.frame_decrypted, width=entry_width)
        self.button_de_copy = tk.Button(master=self.frame_decrypted, command=self.decryptCopy, text='Copy', width=button_width)
        self.button_de_paste = tk.Button(master=self.frame_decrypted, command=self.decryptPaste, text='Paste', width=button_width)
        # Positions all the widgets
        self.label_input.grid(row=0, column=0, ipadx=int_padding, ipady=int_padding, padx=label_ext_padding, pady=label_ext_padding)
        self.entry_decrypted.grid(row=0, column=1, ipadx=int_padding, ipady=int_padding, padx=entry_ext_padding, pady=entry_ext_padding)
        self.button_de_copy.grid(row=0, column=2, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
        self.button_de_paste.grid(row=0, column=3, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)


        # Button frame widgets
        self.frame_buttons.columnconfigure([0, 1], weight=1)
        self.button_encrypt = tk.Button(master=self.frame_buttons, command=self.encryptApply, text='Encrypt', width=button_width)
        self.button_decrypt = tk.Button(master=self.frame_buttons, command=self.decryptApply, text='Decrypt', width=button_width)
        # To position all these widgets
        self.button_encrypt.grid(row=0, column=0, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
        self.button_decrypt.grid(row=0, column=1, sticky='ew', ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)


        # Encryption frame widgets
        self.frame_encrypted.columnconfigure(1, weight=1)  # To change the layout of each column
        # Creates all the widgets
        self.label_output = tk.Label(master=self.frame_encrypted, width=label_width, text='Encrypted')
        self.entry_encrypted = tk.Entry(master=self.frame_encrypted, width=entry_width)
        self.button_en_copy = tk.Button(master=self.frame_encrypted, command=self.encryptCopy, text='Copy', width=button_width)
        self.button_en_paste = tk.Button(master=self.frame_encrypted, command=self.encryptPaste, text='Paste', width=button_width)
        # Positions all the widgets
        self.label_output.grid(row=0, column=0, ipadx=int_padding, ipady=int_padding, padx=label_ext_padding, pady=label_ext_padding)
        self.entry_encrypted.grid(row=0, column=1, ipadx=int_padding, ipady=int_padding, padx=entry_ext_padding, pady=entry_ext_padding)
        self.button_en_copy.grid(row=0, column=2, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
        self.button_en_paste.grid(row=0, column=3, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
    

    # Program Functions
    def encryptApply(self):
        text_input = str(self.entry_decrypted.get())
        keys = [int(self.chosen_key_1.get()), int(self.chosen_key_2.get()), int(self.chosen_key_3.get()), int(self.chosen_key_4.get())]

        text_output = encrypt(text_input, keys)
        self.entry_encrypted.delete(0, tk.END)
        self.entry_encrypted.insert(0, text_output)


    def decryptApply(self):
        text_input = str(self.entry_encrypted.get())
        keys = [int(self.chosen_key_1.get()), int(self.chosen_key_2.get()), int(self.chosen_key_3.get()), int(self.chosen_key_4.get())]

        text_output = decrypt(text_input, keys)
        self.entry_decrypted.delete(0, tk.END)
        self.entry_decrypted.insert(0, text_output)


    def decryptCopy(self):
        de_text = self.entry_decrypted.get()
        pyperclip.copy(self.entry_decrypted.get())


    def decryptPaste(self):
        clipboard_text = pyperclip.paste()
        self.entry_decrypted.delete(0, tk.END)
        self.entry_decrypted.insert(0, clipboard_text)


    def encryptCopy(self):
        en_text = self.entry_encrypted.get()
        pyperclip.copy(en_text)


    def encryptPaste(self):
        clipboard_text = pyperclip.paste()
        self.entry_encrypted.delete(0, tk.END)
        self.entry_encrypted.insert(0, clipboard_text)
