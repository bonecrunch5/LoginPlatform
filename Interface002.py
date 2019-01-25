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

def adminlogin():
    # Admin login
    pc = input('Primary Code: ')
    sc = input('Secondary Code: ')
    tc = input('Tertiary Code: ')
    ap = 'menfire' or 'alicization'
    if pc == '1337':
        if sc == '0138':
            if tc == '1975':
                if ap == 'menfire' or 'alicization':
                    print('How can I help Sir?')
                else:
                    print("Code(s) is/are incorrect!")
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