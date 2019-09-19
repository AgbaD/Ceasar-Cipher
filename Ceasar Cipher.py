# =================== Message Cipher .py =============

from tkinter import *


class Cipher:

    def __init__(self):
        HEIGHT = 600
        WIDTH = 700

        self.root = Tk()
        self.root.title("Ceasar Cipher")

        canvas = Canvas(self.root, height=HEIGHT, width=WIDTH, bg="#696969")
        canvas.pack()

        frame1 = Frame(self.root, bg='#000000')
        frame1.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        label12 = Label(frame1, text="Input Plaintext:", bg='#4169E1', font=40)
        label12.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.19)

        self.msgvar = StringVar()
        entry11 = Entry(frame1, textvariable=self.msgvar, bg="#4169E1",
                        borderwidth=3, font=40)
        entry11.place(relx=0.33, rely=0.1, relwidth=0.6, relheight=0.19)

        label13 = Label(frame1, text="Key:", bg='#4169E1', font=40)
        label13.place(relx=0.05, rely=0.33, relwidth=0.13, relheight=0.19)

        self.keyvar = IntVar()
        entry12 = Entry(frame1, textvariable=self.keyvar, bg='#4169E1',
                        borderwidth=3, font=40)
        entry12.place(relx=0.2, rely=0.33, relwidth=0.1, relheight=0.19)

        button11 = Button(frame1, text="Encrypt", bg="gray", command=self.encrypt,
                          font=40, borderwidth=3, activebackground='#000000')
        button11.place(relx=0.1, rely=0.57, relwidth=0.17, relheight=0.19)

        label14 = Label(frame1, text="Ciphertext",bg='#4169E1', font=40)
        label14.place(relx=0.33, rely=0.33, relwidth=0.6, relheight=0.1)

        self.label15 = Label(frame1, bg='#4169E1', font=40)
        self.label15.place(relx=0.33, rely=0.43, relwidth=0.6, relheight=0.5)

        frame2 = Frame(self.root, bg='#2F4F4F')
        frame2.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

        label22 = Label(frame2, text="Input Ciphertext:", bg='#4169E1', font=40)
        label22.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.19)

        self.msg2var = StringVar()
        entry21 = Entry(frame2, textvariable=self.msg2var, bg="#4169E1",
                        borderwidth=3, font=40)
        entry21.place(relx=0.33, rely=0.1, relwidth=0.6, relheight=0.19)

        label23 = Label(frame2, text="Key:", bg='#4169E1', font=40)
        label23.place(relx=0.05, rely=0.33, relwidth=0.13, relheight=0.19)

        self.key2var = IntVar()
        entry22 = Entry(frame2, textvariable=self.key2var, bg='#4169E1',
                        borderwidth=3, font=40)
        entry22.place(relx=0.2, rely=0.33, relwidth=0.1, relheight=0.19)

        button21 = Button(frame2, text="Decrypt", bg="gray", command=self.decrypt,
                          font=40, borderwidth=3, activebackground='#2F4F4F')
        button21.place(relx=0.1, rely=0.57, relwidth=0.17, relheight=0.19)

        label24 = Label(frame2, text="Plaintext", bg='#4169E1', font=40)
        label24.place(relx=0.33, rely=0.33, relwidth=0.6, relheight=0.1)

        self.label25 = Label(frame2, bg='#4169E1', font=40)
        self.label25.place(relx=0.33, rely=0.43, relwidth=0.6, relheight=0.5)

        self.root.mainloop()

    def encrypt(self):
        key = self.keyvar.get()
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        crypt = ''

        msg = self.msgvar.get()
        msg = msg.upper()

        for char in msg:
            if char in alphabet:
                x = self.get_index(char, alphabet)
                code = x + key
                if code > 25:
                    code -= 26

                crypt += alphabet[code]
            else:
                crypt += char
        self.label15['text'] = crypt

    def get_index(self, char, alphabet):
        ind = 0
        while alphabet[ind] != char:
            ind += 1
        return ind

    def decrypt(self):
        key = self.key2var.get()
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        crypt = ''

        msg = self.msg2var.get()
        msg = msg.upper()

        for char in msg:
            if char in alphabet:
                x = self.get_index(char, alphabet)
                code = x - key
                if code < 0:
                    code += 26

                crypt += alphabet[code]
            else:
                crypt += char
        self.label25['text'] = crypt


Cipher()