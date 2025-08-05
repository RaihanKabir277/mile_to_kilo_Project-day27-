# print("programs starts here")

from tkinter import *

Window = Tk()
Window.title("Mile to Km Converter")
Window.minsize(500, 500)
Window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")

# ----entry----
input = Entry(width=20)
input.grid(column=1 ,row=0)

label1 = Label(text="Miles", font=("Arial", 24, "bold"))
label1.grid(column=2, row=0)
label1.config(padx=20)

label2 = Label(text="is equal to", font=("Arial", 24, "bold"))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Arial", 24, "bold"))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 24, "bold"))
label4.grid(column=2, row=1)


def btn1_clicked():
    pass

btn1 = Button(text="Calculate", command=miles_to_km)
btn1.grid(column=1, row=2)
# btn1.config(pady=20) #this padding will work inside the button

Window.mainloop()

