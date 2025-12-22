from tkinter import *

window = Tk()

count = 0


def click():
    global count
    count += 1


def button_click(x):
    entry.insert(count, x)


def action():
    global first_number
    total = entry.get()
    first_number = float(total[:-1])   #gets number after sign


def backspace():
    entry.delete(len(entry.get())-1, END)


def calculate():
    global second_number
    total = entry.get()
    if '+' in total:                                         # Gets number after signs
        second_number = float(total.split('+')[1])
        result = first_number+second_number
    elif '-' in total:
        second_number = float(total.split('-')[1])
        result = first_number-second_number
    elif '/' in total:
        second_number = float(total.split('/')[1])
        result = first_number/second_number
    elif '*' in total:
        second_number = float(total.split('*')[1])
        result = first_number*second_number

    entry.delete(0, END)
    entry.insert(0, result)


entry = Entry(window, width=20, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=3)

button_back = Button(window,
                     text="<-",
                     padx=20,
                     pady=10,
                     command=lambda: backspace())
button_back.grid(row=0, column=3, sticky=NSEW)

button_1 = Button(window,
                  text="1",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(1), click()])
button_1.grid(row=1, column=0, sticky=NSEW)

button_2 = Button(window,
                  text="2",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(2), click()])
button_2.grid(row=1, column=1, sticky=NSEW)

button_3 = Button(window,
                  text="3",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(3), click()])
button_3.grid(row=1, column=2, sticky=NSEW)

button_div = Button(window,
                    text="/",
                    padx=20,
                    pady=10,
                    command=lambda: [button_click("/"), action(), click()])
button_div.grid(row=1, column=3, sticky=NSEW)

button_4 = Button(window,
                  text="4",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(4), click()])
button_4.grid(row=2, column=0, sticky=NSEW)

button_5 = Button(window,
                  text="5",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(5), click()])
button_5.grid(row=2, column=1, sticky=NSEW)

button_6 = Button(window,
                  text="6",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(6), click()])
button_6.grid(row=2, column=2, sticky=NSEW)

button_mul = Button(window,
                    text="x",
                    padx=20,
                    pady=10,
                    command=lambda: [button_click("*"), action(), click()])
button_mul.grid(row=2, column=3, sticky=NSEW)

button_7 = Button(window,
                  text="7",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(7), click()])
button_7.grid(row=3, column=0, sticky=NSEW)

button_8 = Button(window,
                  text="8",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(8), click()])
button_8.grid(row=3, column=1, sticky=NSEW)

button_9 = Button(window,
                  text="9",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(9), click()])
button_9.grid(row=3, column=2, sticky=NSEW)

button_sub = Button(window,
                    text="-",
                    padx=20,
                    pady=10,
                    command=lambda: [button_click("-"), action(), click()])
button_sub.grid(row=3, column=3, sticky=NSEW)

button_0 = Button(window,
                  text="0",
                  padx=20,
                  pady=10,
                  command=lambda: [button_click(0), click()])
button_0.grid(row=4, column=0, sticky=NSEW)

button_dot = Button(window,
                    text=".",
                    padx=20,
                    pady=10,
                    command=lambda: [button_click("."), click()])
button_dot.grid(row=4, column=1, sticky=NSEW)

button_equal = Button(window,
                      text="=",
                      padx=20,
                      pady=10,
                      command=lambda: calculate())
button_equal.grid(row=4, column=2, sticky=NSEW)

button_add = Button(window,
                    text="+",
                    padx=20,
                    pady=10,
                    command=lambda: [button_click("+"), action(), click()])
button_add.grid(row=4, column=3, sticky=NSEW)

window.title("Calculator")
# img = PhotoImage(file="calc.png")
# window.iconphoto(True, img)


window.mainloop()
