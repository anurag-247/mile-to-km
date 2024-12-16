from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = entry.get()
    km = float(miles)*1.689
    entry2.config(text=f"{km}")


entry = Entry()
entry.grid(column=1, row=0)
# entry.config(padx=20, pady=20)

text1 = Label(text="Miles")
text1.grid(column=2, row=0)

entry2 = Label(text="0")
entry2.grid(column=1, row=1)

text2 = Label(text="is equal to")
text2.grid(column=0, row=1)

text3 = Label(text="Km")
text3.grid(column=2, row=1)

button = Button(text="calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
