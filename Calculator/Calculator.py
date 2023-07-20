import tkinter as tk
from tkinter import ttk

def numberClick(n):
    t = output.get()
    if (t == "0" or t == "+" or t == "-" or t == "*" or t == "/" or t == "%"):
        output.set(n)
    else:
        output.set(t+str(n))

def clear():
    output.set(0)
def one():
    numberClick(1)
def two():
    numberClick(2)
def three():
    numberClick(3)
def four():
    numberClick(4)
def five():
    numberClick(5)
def six():
    numberClick(6)
def seven():
    numberClick(7)
def eight():
    numberClick(8)
def nine():
    numberClick(9)
def zero():
    numberClick(0)
def dot():
    t = output.get()
    output.set(t+".")
    
def plus():
    t = float(output.get())
    global firstNum
    firstNum = t
    output.set("+")
    op = output.get()
    
    global operator
    operator = op
    
def minus():
    t = float(output.get())
    global firstNum
    firstNum = t
    output.set("-")
    op = output.get()
    global operator
    operator = op

def mul():
    t = float(output.get())
    global firstNum
    firstNum = t
    output.set("*")
    op = output.get()
    global operator
    operator = op

def div():
    t = float(output.get())
    global firstNum
    firstNum = t
    output.set("/")
    op = output.get()
    global operator
    operator = op
    
def mod():
    t = float(output.get())
    global firstNum
    firstNum = t
    output.set("%")
    op = output.get()
    global operator
    operator = op
    
def result():
    secondNum = float(output.get())
    if operator == "+":
        t = float(firstNum)+float(secondNum)
        output.set(t)
    elif operator == "-":
        t = float(firstNum)-float(secondNum)
        output.set(t)
    elif operator == "*":
        t = float(firstNum)*float(secondNum)
        output.set(t)
    elif operator == "/":
        t = float(firstNum)/float(secondNum)
        output.set(t)
    elif operator == "%":
        t = float(firstNum)%float(secondNum)
        output.set(t)
    
# window
window = tk.Tk()
window.title("Calculator")
# widgets
# row 1
operator =""
output = tk.StringVar()
output.set(0)
row1 = ttk.Frame(master = window)
entry = ttk.Entry(master = row1,width = "37",textvariable = output)
entry.pack(side = "left")
clearButton = ttk.Button(master = row1,text = "C",command = clear)
clearButton.pack(side = "left")
row1.pack(pady = 2)

# row 2
row2 = ttk.Frame(master = window)
button7 = ttk.Button(master = row2,text = "7",command = seven)
button8 = ttk.Button(master = row2,text = "8",command = eight)
button9 = ttk.Button(master = row2,text = "9",command = nine)
divButton = ttk.Button(master = row2, text = "/",command = div)
button7.pack(side = "left")
button8.pack(side = "left")
button9.pack(side = "left")
divButton.pack(side = "left")
row2.pack(pady = 2)

# row 3
row3 = ttk.Frame(master = window)
button4 = ttk.Button(master = row3,text = "4",command = four)
button5 = ttk.Button(master = row3,text = "5",command = five)
button6 = ttk.Button(master = row3,text = "6",command = six)
mulButton = ttk.Button(master = row3, text = "*",command = mul)
button4.pack(side = "left")
button5.pack(side = "left")
button6.pack(side = "left")
mulButton.pack(side = "left")
row3.pack(pady = 2)

# row 4
row4 = ttk.Frame(master = window)
button1 = ttk.Button(master = row4,text = "1",command = one)
button2 = ttk.Button(master = row4,text = "2",command = two)
button3 = ttk.Button(master = row4,text = "3",command = three)
minButton = ttk.Button(master = row4, text = "-",command = minus)
button1.pack(side = "left")
button2.pack(side = "left")
button3.pack(side = "left")
minButton.pack(side = "left")
row4.pack(pady = 2)

# row 5
row5 = ttk.Frame(master = window)
button0 = ttk.Button(master = row5,text = "0",width = "24",command = zero)
dotButton = ttk.Button(master = row5,text = ".",command = dot)
plusButton = ttk.Button(master = row5,text = "+",command = plus)
button0.pack(side = "left")
plusButton.pack(side = "left")
dotButton.pack(side = "left")
row5.pack(pady = 2)


# row 6
row6 = ttk.Frame(master = window)
resultButton = ttk.Button(master = row6, text = "=",width = "37",command = result)
modButton = ttk.Button(master = row6, text = "%",command = mod)
resultButton.pack(side = "left")
modButton.pack(side = "left")
row6.pack(pady = 2)

# run
window.mainloop()