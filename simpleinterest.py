from tkinter import *

def calculateInterest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    i = round(i, 2)

    result.destroy()

    message = Label(resultFrame, text = 'Interest on Rs. ' + str(p)+ " at rate of interest " + str(r) + "% for " + str(t)+ " years is Rs. " + str(i), bg = 'lightcyan', font = ("Calibri", 12), width = 70)
    message.place(x = 20, y = 40)
    message.pack()

window = Tk()

window.title("Simple Interest Calculator")
window.geometry("600x400")
window.configure(bg = 'lightcyan')

appLabel = Label(window, text = 'SIMPLE INTEREST CALCULATOR', fg = 'black', bg = 'lightcyan', font = ("Calibri", 20), bd = 5)
appLabel.place(x = 20, y = 20)

principleLabel = Label(window, text = 'Principle in Rs.', fg = 'black', bg = 'lightcyan', font = ("Calibri", 12), bd = 5)
principleLabel.place(x = 20, y = 90)

principle = Entry(window, text = "", bd = 2, width = 22)
principle.place(x = 200, y = 90)

rateLabel = Label(window, text = "Rate of Interest %", fg = 'black', bg = 'lightcyan', font = ("Calibri", 12))
rateLabel.place(x = 20, y = 140)

rate = Entry(window, text = "", bd = 2, width = 15)
rate.place(x = 200, y = 140)

timeLabel = Label(window, text = "Time in years", fg = 'black', bg = 'lightcyan', font = ("Calibri", 12))
timeLabel.place(x = 20, y = 190)

time = Entry(window, text = "", bd = 2, width = 15)
time.place(x = 200, y = 190)

calculateButton = Button(window, text = 'CALCULATE', fg = 'black', bg = 'cyan', bd = 4, command = calculateInterest)
calculateButton.place(x = 20, y = 250)

resultFrame = LabelFrame(window, text = 'Result', bg = 'lightcyan', font = ("Calibri", 11), width = 450)
resultFrame.pack(padx = 20, pady = 20)
resultFrame.place(x = 20, y = 300)

result = Label(resultFrame, text = 'Your result will be displayed here', bg = 'lightcyan', font = ("Calibri", 12), width = 70)
result.place(x = 20, y = 20)
result.pack()

window.mainloop()
