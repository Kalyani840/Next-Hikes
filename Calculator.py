from tkinter import*



class Calculator:
    def __init__(self,calculate):
        self.calculate = calculate
        self.calculate .title('Calculator')
        self.calculate.geometry('615x690+400+100')
        self.calculate.configure(bg = 'cadet blue')

        self.Mainframe = Frame(self.calculate , border = 18 , width = 600, height = 670, relief = RIDGE, bg = 'powder blue')
        self.Mainframe.grid()
        self.Widgetframe = Frame(self.Mainframe , border = 18 , width = 590, height = 660, relief = RIDGE, backg = 'cadet blue')
        self.Widgetframe.grid()

        self.lblDisplay = Label(self.Widgetframe, width = 30, height = 2, bg = 'white', font = ('arial', 20, 'bold'), anchor = 'e')
        self.lblDisplay.grid (row=0, column=0, columnspan=4, padx = 10, pady = 10)

        self.input_button = ""

        self.create_button("←",1,0)
        self.create_button("CE",1,1)
        self.create_button("C",1,2)
        self.create_button("±",1,3)

        self.create_button("7",2,0)
        self.create_button("8",2,1)
        self.create_button("9",2,2)
        self.create_button("+",2,3)

        self.create_button("4",3,0)
        self.create_button("5",3,1)
        self.create_button("6",3,2)
        self.create_button("-",3,3)

        self.create_button("1",4,0)
        self.create_button("2",4,1)
        self.create_button("3",4,2)
        self.create_button("*",4,3)

        self.create_button("0",5,0)
        self.create_button(".",5,1)
        self.create_button("=",5,2)
        self.create_button("/",5,3)

    def create_button(self, text, row, column):
        btnWidget = Button(self.Widgetframe,width = 6,text=text, height=2,border=4, bg='powder blue', font = ("arial",20,"bold"), command = lambda: self.button_click(text))
        btnWidget.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self,text):

        if text == "←":
            self.input_button = self.input_button[:-1]
        elif text == "CE":
            self.input_button = ""
        elif text == "C":
            self.input_button = ""

        elif text == "=":
            try:
                self.input_button = str(eval(self.input_button))
            except:
                self.input_button = "Error"

        elif text == "±":
            self.input_button = str(float(self.input_button))
        else:
            self.input_button+= text
        self.lblDisplay.config(text = self.input_button)



        

calculate = Tk()
App = Calculator(calculate)
calculate.mainloop()