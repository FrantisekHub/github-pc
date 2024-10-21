from tkinter import *
import psycopg2

root = Tk()
root.title('Výpočet BMI')
root.geometry('250x250')
root.resizable(False, False)

# General Label
label_general = Label(root, text='Výpočet BMI')
label_general.grid(row=0, column=1)

# Weight section
label_weight = Label(root, text='Zadejte váhu (kg):')
label_weight.grid(row=1, column=0)

entry_weight = Entry(root)
entry_weight.grid(row=1, column=1)

# Height section
label_height = Label(root, text='Zadejte výšku (m):')
label_height.grid(row=2, column=0)

entry_height = Entry(root)
entry_height.grid(row=2, column=1)

# Button

button = Button(root, text='Vypočítat')
button.grid(row=3, column=1)




root.mainloop()