
#! Importing Required Modules 
from tkinter import *
import time 
import webbrowser as wb
import speedtest
import datetime

#! Making Functional Buttons
def click(event):

    global e1_value
    text = event.widget.cget("text")
    if text == "=":

        if e1_value.get().isdigit()  :
            value = int(e1_value.get())

        else:

            try:
                value = e1_value.get()
                value = eval(e1_value.get())

            except Exception as e:
                print(e)
                value = "Error"


        e1_value.set(value)
        calc.update()


    elif text == "C":
        e1_value.set("")
        calc.update()


    else:
        e1_value.set(e1_value.get() + text)
        calc.update()

#! Making A Calculator Gui
calc = Tk()


#! Defining Default Screen Height And Width
calc.geometry("500x400")


#! Setting Title 
calc.title('Calculator')


#! Setting Icon
c = PhotoImage(file = 'calculator.png')
calc.iconphoto(False, c)


#! Setting Frame 1 And Entry Widget
f1 = Frame(calc)

#! Setting Value for Entry Widget
e1_value = StringVar()
e1_value.set('')


#! Setting Entry Widget
e1 = Entry(f1, textvariable = e1_value, justify = CENTER, font = "hack 24" , relief = SOLID)
e1.pack(fill = X, pady = 10, padx = 45)
f1.pack(side = TOP)


#! Setting Status Bar  For Time And Date with Frame 2
current_time = time.strftime('%H : %M')
f2 = Frame(calc)
status = StringVar()
status.set(f"Time  ↔\t{current_time}")


#! Styling For Status Bar
status_bar = Label(f2, textvariable = status, borderwidth = 10,fg = 'cyan',bg = 'black', relief = FLAT, anchor = 'se')
status_bar.pack(side = BOTTOM, fill = X, anchor = 'sw')
f2.pack(side = BOTTOM, fill = X, anchor = 'sw')


#! Setting Buttons in Frame 3
f3 = Frame()


#! Setting Value for Entry Widget
b_value = StringVar()


#! Setting Buttons in Frame 3
b1 = Button(f3, text = "1",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b1.pack(side = LEFT, anchor = 'ne')
b1.bind('<Button-1>',click)


b2 = Button(f3, text = "2",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b2.pack(side = LEFT, anchor = 'ne', padx = 3)
b2.bind('<Button-1>',click)


b3 = Button(f3, text = "3",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b3.pack(side = LEFT, anchor = 'ne', padx = 3)
b3.bind('<Button-1>',click)


b_1 = Button(f3, text = "+",pady = 13, activebackground = 'purple', width = 10)
b_1.pack(side = LEFT, anchor = 'ne', padx = 3)
b_1.bind('<Button-1>',click)


f3.pack(pady = 10)


#! Setting Buttons in Frame 4
f4 = Frame()


b4 = Button(f4, text = "4",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b4.pack(side = LEFT, anchor = 'ne')
b4.bind('<Button-1>',click)


b5 = Button(f4, text = "5",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b5.pack(side = LEFT, anchor = 'ne',padx = 3)
b5.bind('<Button-1>',click)


b6 = Button(f4, text = "6",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b6.pack(side = LEFT, anchor = 'ne',padx = 3)
b6.bind('<Button-1>',click)


b_2 = Button(f4, text = "-",pady = 13, activebackground = 'purple', width = 10)
b_2.pack(side = LEFT, anchor = 'ne',padx = 3)
b_2.bind('<Button-1>',click)


f4.pack(pady = 10)


#! Setting Buttons in Frame 5
f5 = Frame()


b7 = Button(f5, text = "7",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b7.pack(side = LEFT, anchor = 'ne')
b7.bind('<Button-1>',click)


b8 = Button(f5, text = "8",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b8.pack(side = LEFT, anchor = 'ne', padx = 3)
b8.bind('<Button-1>',click)


b9 = Button(f5, text = "9",pady = 13, padx = 20, activebackground = 'purple', width = 10)
b9.pack(side = LEFT, anchor = 'ne', padx = 3)
b9.bind('<Button-1>',click)


b_3 = Button(f5, text = "*",pady = 13, activebackground = 'purple', width = 10)
b_3.pack(side = LEFT, anchor = 'ne', padx = 3)
b_3.bind('<Button-1>',click)


f5.pack(pady = 10)


#! Frame 6 For Extra Buttons
f6 = Frame()
b_c = Button(f6, text = "C",pady = 13,padx = 20, activebackground = 'purple', width = 10)
b_c.pack(side = LEFT, anchor = 'ne', padx = 3)
b_c.bind('<Button-1>',click)


b_4 = Button(f6, text = "0",pady = 13,padx = 20, activebackground = 'purple', width = 10)
b_4.pack(side = LEFT, anchor = 'ne', padx = 3)
b_4.bind('<Button-1>',click)


b_5 = Button(f6, text = "=",pady = 13,padx = 20, activebackground = 'purple', width = 10)
b_5.pack(side = LEFT, anchor = 'nw', padx = 3)
b_5.bind('<Button-1>',click)


b_5 = Button(f6, text = "%",pady = 13, activebackground = 'purple', width = 10)
b_5.pack(side = LEFT, anchor = 'nw', padx = 3)
b_5.bind('<Button-1>',click)


f6.pack()


#! Setting up the base of BMI
def bmi() : 
    """
    This function takes your height and weight as values. Then parses it in another function and then gives you your BMI(Body Mass Index) 
    """
    bmi_widget = Toplevel(calc)
    bmi_widget.geometry('290x200')
    bmi_widget.title('BMI')
    p1 =  PhotoImage(file = 'bmi.png')
    bmi_widget.iconphoto(False,p1)


    weight_frame = Frame(bmi_widget)
    weight_value = IntVar()
    weight_label = Label(weight_frame, text = 'Weight', font =  'comicsansms 12 italic' )
    weight_label.pack( side = LEFT, padx = 20)
    weight_entry = Entry(
    weight_frame,textvariable = weight_value, font = 'comicsansms 12 italic', justify = CENTER)
    weight_entry.pack()
    weight_frame.pack()
    weight_value.set(1)


    height_frame = Frame(bmi_widget)
    height_value = IntVar()
    height_label = Label(height_frame, text = 'Height', font =  'comicsansms 12 italic' )
    height_label.pack( side = LEFT, padx = 20)
    height_entry = Entry(
    height_frame,textvariable = height_value, font = 'comicsansms 12 italic', justify = CENTER)
    height_entry.pack(pady = 10)
    height_frame.pack()
    height_value.set(1)


    def calc_bmi() :
        """
        Parses the values of height and weight.
        """
        height = int((height_entry.get()))
        weight = int((weight_entry.get()))
        Label(bmi_widget, text = (f"Your BMI is {((weight * 703) / (height * height))}"), bg = 'grey', fg = 'cyan').pack(side = BOTTOM)
        calc.update()
    Button(bmi_widget, text = 'Calculate', command = calc_bmi).pack(anchor = 'nw', padx = 30)

#! Setting Up the base for Discount
def discount() :
    """
    This Function takes the amount of the thing you want to calculate the discount on and then the discount applie on it and then the another function parses it and calculates how much you saved on it. 
    """
    discount_widget = Toplevel(calc)
    discount_widget.geometry('290x200')
    discount_widget.title('Discount')
    discount_widget.iconbitmap('discount.ico')

    principal_frame = Frame(discount_widget)
    principal_value = IntVar()
    principal_label = Label(principal_frame, text = 'Amount')
    principal_label.pack(side = LEFT, anchor = 'nw')
    principal_entry = Entry(principal_frame,textvariable = principal_value, justify =LEFT)
    principal_entry.pack(padx = 50)
    principal_frame.pack()

    discount_frame = Frame(discount_widget)
    discount_value = IntVar()
    discount_label = Label(discount_frame, text = 'Discount')
    discount_label.pack(side = LEFT, anchor = 'nw',pady = 20)
    discount_entry = Entry(discount_frame, textvariable = discount_value, justify = LEFT)
    discount_entry.pack(padx = 50, pady = 20)
    discount_frame.pack()

#! Making Base for Discount
    def calc_dis() : 
        '''
        Parses the value of discount and amount applied on the thing.
        '''
        principal = principal_value.get()
        dis = discount_value.get()
        total_dis = principal / dis
        Label(discount_widget, text = (f"You Saved {total_dis}"), bg = 'grey', fg = 'cyan').pack(side = BOTTOM, fill = X)
    Button(discount_widget,text = 'Calculate Discount', command = calc_dis).pack(side = LEFT, anchor = 'nw')

#! Setting Up the base for Temperature
def temperature():
    """
    This function takes the value of any one parameter and converts it to another. 
    """    

    temperature_widget = Toplevel(calc)
    temperature_widget.geometry('290x200')
    temperature_widget.title('Temperature')
    temperature_widget.iconbitmap('temp.ico')


    celsius_frame = Frame(temperature_widget)
    celsius_value = IntVar()
    celsius_entry = Entry(celsius_frame, textvariable=celsius_value).pack(
        side=RIGHT, anchor='ne', pady=10)
    celsius_label = Label(
        celsius_frame, text='Celsius *C').pack(side=LEFT, anchor='nw', pady=10,padx = 20)
    celsius_frame.pack()


    farenheit_frame = Frame(temperature_widget)
    farenheit_value = IntVar()
    farenheit_entry = Entry(farenheit_frame, textvariable=farenheit_value).pack(
        side=RIGHT, anchor='ne', pady=10)
    farenheit_label = Label(
        farenheit_frame, text='Farenheit *F').pack(side=LEFT, anchor='nw', pady=10, padx = 14)
    farenheit_frame.pack()


    kelvin_frame = Frame(temperature_widget)
    kelvin_value = IntVar()
    kelvin_entry = Entry(kelvin_frame, textvariable=kelvin_value).pack(
        side=RIGHT, anchor='ne', pady=10)
    kelvin_label = Label(
        kelvin_frame, text='Kelvin *K').pack(side=LEFT, anchor='nw', pady=10, padx = 20)
    kelvin_frame.pack()


#! Function for Reseting the Calc(Temperature)
    def reset() : 

        """
        Resets the parameter.
        """        

        celsius_value.set(0)
        farenheit_value.set(0)
        kelvin_value.set(0)


#! Setting / Getting Values for Temperature
    def calc_temp() : 

        """
        Fetches the value of parameters and accordingly converts the values.
        """        

        c = celsius_value.get()
        f = farenheit_value.get()
        k = kelvin_value.get()


        if(c != None and c != 0) :
            f_temp = (c * (9/5) + 32)
            k_temp = c + 273.15
            farenheit_value.set(f_temp)
            kelvin_value.set(k_temp)
            temperature_widget.update()


        elif (f != None and f != 0) : 
            k_temp = ((f + 459.67) * (5/9))
            c_temp = ((f -32) * (5/9))
            celsius_value.set(c_temp)
            kelvin_value.set(k_temp)
            temperature_widget.update()


        elif (k != None and k != 0) : 
            c_temp = (k - 273.15)
            k_temp = ((k * 1.8) - (459.67))
            farenheit_value.set(k_temp)
            celsius_value.set(c_temp)


    Button(temperature_widget, text = "Convert", command = calc_temp).pack(side = LEFT, padx = 30)
    Button(temperature_widget, text = "Reset", command = reset).pack(side = RIGHT, padx = 30)


#! Help Widget 
def help_about () : 

    help_widget  = Toplevel(calc)
    help_widget.geometry('200x150')
    help_widget.title('Help')
    f1 = Frame(help_widget)
    Label(f1 , text = 'The Functions Are :  ', fg = 'black', bg = 'cadetblue3' ).pack(anchor = 'nw')
    Label(f1 , text = 'Number To Binary', fg = 'black', font = 'comicsans 10 italic bold' ).pack(padx = 30)
    Label(f1 , text = 'BMI ', fg = 'black', font = 'comicsans 10 italic bold'  ).pack(padx = 30)
    Label(f1 , text = 'Discount', fg = 'black', font = 'comicsans 10 italic bold'  ).pack(padx = 30)
    Label(f1 , text = 'Temperature ', fg = 'black', font = 'comicsans 10 italic bold').pack(padx = 30)
    Label(f1 , text = 'Speed Test', fg = 'black', font = 'comicsans 10 italic bold').pack(padx = 30)
    f1.pack()
    help_widget.configure(bg = 'cadetblue3')


#! Making Base for Number to Binary Function
def numToBinary() : 

    numtb = Toplevel(calc)
    numtb.title('Binary System')
    numtb.geometry('190x170')
    numtb.iconbitmap('binary.ico')
    numtb_widget = Frame(numtb)
    num_value = IntVar()
    Label(numtb_widget, text = 'Number:', bg = 'yellow').pack(side = LEFT,anchor = 'nw')
    num = Entry(numtb_widget, textvariable = num_value, justify = CENTER, font = 'comicsans 8 italic', bd = 3, bg = 'orange')
    num.pack(side = RIGHT,anchor = 'ne')
    numtb_widget.configure(bg = 'orange')
    numtb.configure(bg = 'coral2')
    numtb_widget.pack()


#! Setting Function for Convertion
    def convert() :
        x1 = Frame(numtb)
        bin_value = int(num_value.get())
        bin_num = bin(bin_value) 
        Label(x1, text = (f'The Binary Number is {bin_num}')).pack(side = BOTTOM, fill = X )
        x1.pack(side = BOTTOM)

    Button(numtb,text = 'Convert', command = convert).pack()


#! Base For Speedtest 
def speed_test() :
    spt = Toplevel(calc)
    spt.geometry('300x200')
    spt.title('Speed Test')
    a = PhotoImage(file = 'dashboard.png')
    spt.iconphoto(False, a)
    test = speedtest.Speedtest()


#! Testing Speed
    def st_main(): 
        d = (test.download() / 10 ** 6)
        u = (test.upload() / 10 ** 6)
    
        l1 = Label(spt, text = f'Download Speed : {round(d, 2)} Mbps', font = 'Arial 15 italic', fg = 'coral')
        l1.pack(padx = 10)

        l2 = Label(spt, text = f'Upload Speed : {round(u, 2)} Mbps', font = 'Arial 15 italic', fg = 'coral')
        l2.pack(padx = 20, pady = 15)

    Button(spt, text = 'Test',command = st_main, activeforeground = 'cyan').pack(pady = 30, ipadx = 30)
    spt.configure(bg = 'black')

def age_calc() : 
    date = datetime.datetime.now()
    agecalc = Toplevel(calc)
    agecalc.title('Age Calculator')
    agecalc.geometry('500x300')
    agecalc_img = PhotoImage(file = '')
    agecalc.iconphoto(False, agecalc_img)
    agecalc.configure(bg = 'False')


#! Reachme 
def reachme() : 

    rm = Toplevel(calc)
    rm.title('Reach Me')
    rm.geometry('300x200')
    rm_ph = PhotoImage(file = 'reachme.png')
    rm.iconphoto(False, rm_ph)
    rm.configure(bg = 'grey')

    def insta() : 
        wb.open('https://www.instagram.com/____piiyush____/')

    def twitter() : 
        wb.open('https://twitter.com/gulwani_piyush')

    rbf = Frame(rm)
    rb0 = Button(rbf, text = 'Instagram', fg  = 'cyan', bg = 'black', command = insta)
    rb0.pack(side = LEFT, ipadx = 20)

    rb1 = Button(rbf, text = 'Twitter', fg  = 'cyan', bg = 'black', command = twitter)
    rb1.pack(side = RIGHT, ipadx = 30)
    rbf.pack(side = TOP, pady = 30)


#! Adding Menu and Sub-Menus
mainmenu = Menu(calc)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="BMI", command=bmi)
m1.add_separator()
m1.add_command(label="Discount", command = discount)
m1.add_separator()
m1.add_command(label="Temperature", command = temperature)
m1.add_separator()
m1.add_command(label="Binary System", command = numToBinary)
m1.add_separator()
m1.add_command(label="Speed Test", command = speed_test)
m1.add_separator()
m1.add_command(label="Age Calc", command = age_calc)
calc.config(menu=mainmenu)
mainmenu.add_cascade(label="More", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_separator()
m2.add_command(label = 'Help', command = help_about)
m2.add_separator()
m2.add_command(label = 'Reach Me', command = reachme)
m2.add_separator()
mainmenu.add_cascade(label="About", menu=m2)

calc.configure(bg = 'orange')
calc.mainloop()