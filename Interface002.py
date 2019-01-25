from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10', 'bold')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 50
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 50
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 50
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 50
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='Welcome Sir')
        self.titulo['font'] = ('Arial', '25')
        self.titulo.pack()

        self.primaryCodeAsk = Label(self.segundoContainer, text='Primary Code: ')
        self.primaryCode = Entry(self.segundoContainer)

        self.primaryCode['width'] = 29
        self.primaryCode['font'] = self.fontePadrao
        self.primaryCode.pack(side=LEFT)

        self.secondaryCodeAsk = Label(self.terceiroContainer, text='Secondary Code: ')
        self.secondaryCode = Entry(self.terceiroContainer)

        self.secondaryCode['width'] = 29
        self.secondaryCode['font'] = self.fontePadrao
        self.secondaryCode.pack(side=LEFT)

        self.tertiaryCodeAsk = Label(self.terceiroContainer, text='Tertiary Code: ')
        self.tertiaryCode = Entry(self.quartoContainer)

        self.tertiaryCode['width'] = 29
        self.tertiaryCode['font'] = self.fontePadrao
        self.tertiaryCode.pack(side=LEFT)

        self.adminlogin

    def adminlogin(self):
        # Admin login
        pc = self.primaryCode.get()
        sc = self.secondaryCode()
        tc = self.tertiaryCode.get()

        # ap = 'menfire' or 'alicization'
        if pc == '1337':
            if sc == '0138':
                if tc == '1975':
                    print('How can I help Sir?')
                else:
                    print("Code(s) is/are incorrect!")
            else:
                print('Code(s) is/are incorrect!')
        else:
            print('Code(s) is/are incorrect!')


root = Tk()
root.title('Prototype')
root.geometry('500x500+380+140')
Application(root)
root.mainloop()
