from tkinter import *
from controller import pokaz_liste
from controller import wybierz_klientow, wybierz_pracownikow

root = Tk()
root.title("Portal randkowy")
root.geometry("1100x760")

Label(root, text="Wybierz moduł").pack()

Button(root, text="Klienci", command=wybierz_klientow).pack()
Button(root, text="Pracownicy", command=wybierz_pracownikow).pack()

root.mainloop()