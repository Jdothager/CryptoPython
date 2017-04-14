from tkinter import Tk, Label, Button, Scrollbar, StringVar, IntVar, Entry, Text, END, Menu, N, W, E, S
from tkinter.filedialog import askopenfilename, asksaveasfile
import caesar, vigenere, sys

"""
    TODO:
        - with caesar, self.rot_entry should only take integers
        - about menu/file/window
"""


class CryptoGUI:

    def __init__(self, master):
        self.master = master
        # title at top of window
        master.title('Crypto')
        # setup a menu bar
        top_menu = Menu(self.master)
        self.master.config(menu=top_menu)
        # add a file button to the menu
        file_menu = Menu(top_menu, tearoff=0)
        file_menu.add_command(label='Open', command=self.load_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Exit', command=sys.exit)
        top_menu.add_cascade(label='File', menu=file_menu)
        # add a cipher button to the menu
        cipher = Menu(top_menu, tearoff=0)
        cipher.add_command(label='Caesar', command=self.caesar_widgets)
        cipher.add_command(label='Vigenere', command=self.vig_widgets)
        top_menu.add_cascade(label='Cipher', menu=cipher)

        # keep track of caesar or vigenere
        self.caesar = False
        self.caesar_label = Label(master, text='Caesar cipher')
        self.vig_label = Label(master, text='Vigenere cipher')

        # widget setup
        # input label and input box
        self.input_text_label = Label(master, text='Enter Text Here:')
        self.input_text = Text(master, height='5')
        self.input_scroll = Scrollbar(master, command=self.input_text.yview)
        # rotation/key label and box
        self.rot_label = Label(master, text='Amount to rotate by:')
        self.rot = IntVar()
        self.rot.set(0)
        self.rot_entry = Entry(master, textvariable=self.rot)
        self.key = StringVar()
        self.key_label = Label(master, text='Enter Key:')
        self.key_entry = Entry(master, textvariable=self.key)
        # decrypt/encrypt button and output box
        self.encrypt_button = Button(master, text='ENCRYPT', command=self.encrypt_text)
        self.decrypt_button = Button(master, text='DECRYPT', command=self.decrypt_text)
        self.output_text_label = Label(master, text='Output:')
        self.output_text = Text(master, height='5')
        self.output_scroll = Scrollbar(master, command=self.output_text.yview)
        # caesar/vig switch
        self.choose_label = Label(master, text='Choose:', font=36)
        self.begin_button_c = Button(master, text='Caesar Cipher', command=self.caesar_widgets)
        self.begin_button_v = Button(master, text='Vigenere Cipher', command=self.vig_widgets)

        # start with begin_screen
        self.begin_screen()

    def begin_screen(self):
        self.choose_label.grid(row=0, column=1, ipady=50)
        self.begin_button_c.grid(row=1, column=0, padx=75, ipadx=80, ipady=20)
        self.begin_button_v.grid(row=1, column=2, padx=75, ipadx=80, ipady=20)

    def clear_buttons(self):
        self.choose_label.grid_forget()
        self.begin_button_c.grid_forget()
        self.begin_button_v.grid_forget()
        self.key_label.grid_forget()
        self.key_entry.grid_forget()
        self.rot_label.grid_forget()
        self.rot_entry.grid_forget()
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', END)
        self.output_text.config(state='disabled')
        self.caesar_label.grid_forget()
        self.vig_label.grid_forget()

    def set_shared_widgets(self):
        self.input_text_label.grid(row=0, column=0, pady=15, padx=20, sticky='es')
        self.input_text.grid(row=1, column=1, columnspan=3)
        self.input_scroll.grid(row=1, column=4, sticky='nsew')
        self.input_text['yscrollcommand'] = self.input_scroll.set
        self.encrypt_button.grid(row=4, column=1, ipady=25, sticky='nesw')
        self.decrypt_button.grid(row=4, column=3, ipady=25, sticky='nesw')
        self.output_text_label.grid(row=5, column=0, pady=15, padx=20, sticky='es')
        self.output_text.grid(row=6, column=1, columnspan=3)
        self.output_scroll.grid(row=6, column=4, sticky='nsew')
        self.output_text['yscrollcommand'] = self.output_scroll.set

    def caesar_widgets(self):
        self.caesar = True
        self.clear_buttons()
        self.set_shared_widgets()
        # widget layout
        self.caesar_label.grid(row=0, column=2)
        self.rot_label.grid(row=2, column=2, pady=10)
        self.rot_entry.grid(row=3, column=2)

    def vig_widgets(self):
        self.caesar = False
        self.clear_buttons()
        self.set_shared_widgets()
        # widget layout
        self.vig_label.grid(row=0, column=2)
        self.key_label.grid(row=2, column=2, pady=10)
        self.key_entry.grid(row=3, column=2)

    def output_results(self, output):
        self.output_text.config(state='normal')
        # clear the output text box
        self.output_text.delete('1.0', END)
        # fill with encrypted text
        self.output_text.insert('1.0', output)
        self.output_text.config(state='disabled')

    def encrypt_text(self):
        """ run the text from input_text through caesar.py or vigenere.py,
            display output in text box
        """
        if self.caesar:
            rot = self.rot.get()
            output = caesar.encrypt(self.input_text.get('1.0', END), rot)
            self.output_results(output)
        else:
            key = self.key.get()
            output = vigenere.encrypt(self.input_text.get('1.0', END), key)
            self.output_results(output)

    def decrypt_text(self):
        """ run the text from input_text through caesar.py or vigenere.py,
            display output in text box
        """
        if self.caesar:
            rot = self.rot.get()
            output = caesar.decrypt(self.input_text.get('1.0', END), rot)
            self.output_results(output)
        else:
            key = self.key.get()
            output = vigenere.decrypt(self.input_text.get('1.0', END), key)
            self.output_results(output)

    def load_file(self):
        file_path = askopenfilename(filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
        if file_path != '':
            f = open(file_path, 'r')
            file_str = f.read()
            self.input_text.delete('1.0', END)
            self.input_text.insert('1.0', file_str)
            f.close()

    def save_file(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return
        save_text = str(self.output_text.get('1.0', END))
        f.write(save_text)
        f.close()


def main():
    root = Tk()
    root.geometry('850x450')
    my_gui = CryptoGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
