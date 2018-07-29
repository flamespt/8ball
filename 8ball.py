import random
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Application(Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent)

        self.frame_top=Frame(parent)
        self.frame_bottom=Frame(parent)
        self.frame_meio = Frame(parent)
        self.frame_top.pack(side = TOP)
        self.frame_meio.pack(side = LEFT)
        self.frame_bottom.pack(side=BOTTOM)



        self.graphic()



    def graphic(self):

        # Colocar a entrada de texto
        self.form = Entry(self.frame_meio)
        self.form.pack(side=RIGHT)

    #LABEL
        self.l = Label(self.frame_top, text="Default")
        self.l.pack()

    #progress bar
        self.mpb = ttk.Progressbar(self.frame_meio)
        self.mpb["maximum"] = 100
    #Botao
        bttn1=ttk.Button(self.frame_bottom,text="teste", command=self.pergunta)
        bttn1.pack(side=BOTTOM)

    def ballgenerator(self):
        print("pensando na sua resposta")
        x = random.randint(2, 5)


        for remaining in range(0, x+1, 1):
            time.sleep(1)
            soma = remaining *(100/x)
            print (soma)
            self.mpb.pack(side = RIGHT)

            self.mpb["value"] = soma
            self.update_idletasks()



        respostas = ['It is certain.', 'As I see it, yes.', 'Reply hazy, try again', 'Dont count on it.',
                     'It is decidedly so.']
        self.l['text'] = respostas[random.randint(0, respostas.__len__() - 1)]

    def pergunta(self):
            x = self.form.get()
            if re.match('^[A-Z][^?!.]*[?.!]$', x):
                self.ballgenerator()
            elif x != "exit":
                messagebox.showerror("Error", "Error message")

                print("ISSO NAO É UMA PERGUNTA MEU BOI")
            else:
                print("BYE BYE")
                rw.quit()
                return


if __name__ == "__main__":

    rw = Tk()
    var = StringVar()
    # window
    rw.title('8 Ball game!')
    rw.geometry('500x300')  # Size 500, 300

    app = Application(rw)
    rw.mainloop()
