from tkinter import *
from controller import pokaz_liste

root = Tk()
root.title("Portal randkowy")
root.geometry("1100x760")

Label(root, text="Wybierz moduł").pack()

Button(root, text="Klienci", command=pokaz_liste).pack()
Button(root, text="Pracownicy").pack()

root.mainloop()