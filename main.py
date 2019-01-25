from tkinter import *
import os

root = Tk()
root.title('Prototype')
root.geometry('500x500+380+140')


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

        self.titulo = Label(self.primeiroContainer, text='Prometheus')
        self.titulo['font'] = ('Harlow Solid Italic', '25')
        self.titulo.pack()

        self.adminLabel = Label(self.segundoContainer, text='Admin', font=self.fontePadrao)
        self.adminLabel.pack(side=LEFT)

        self.admin = Entry(self.segundoContainer)
        self.admin['width'] = 29
        self.admin['font'] = self.fontePadrao
        self.admin.pack(side=LEFT)

        self.passwordLabel = Label(self.terceiroContainer, text='Pass ', font=self.fontePadrao)
        self.passwordLabel.pack(side=LEFT)

        self.password = Entry(self.terceiroContainer)
        self.password['width'] = 30
        self.password['font'] = self.fontePadrao
        self.password['show'] = '*'
        self.password.pack(side=LEFT)


        self.start = Button(self.quartoContainer)
        self.start['text'] = 'Start'
        self.start['font'] = ('Stencil', '10')
        self.start['width'] = 12
        self.start['command'] = self.verificaPassword
        self.start.configure(relief=GROOVE)
        self.start.pack()

        self.exit = Button(self.quartoContainer)
        self.exit['text'] = 'Exit'
        self.exit['font'] = ('Stencil', '10')
        self.exit['width'] = 12
        self.exit['command'] = self.exit.quit
        self.exit.configure(relief=GROOVE)
        self.exit.pack()


        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()


    # Método verificar password
    def verificaPassword(self):
        admin = self.admin.get()
        password = self.password.get()
        if admin == 'Prometheus' and password == 'menfire':
            root.destroy()
            os.system('Interface002.py')
        elif admin == 'Alice' and password == 'alicization':
            root.destroy()
            os.system('Interface002.py')

        else:
            self.mensagem['text'] = 'Entry denied'



Application(root)
root.mainloop()
