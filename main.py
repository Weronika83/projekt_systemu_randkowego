from tkinter import *

root = Tk()
root.title("Portal randkowy")
root.geometry("1100x760")

Label(root, text="Wybierz moduł").pack()

Button(root, text="Klienci").pack()
Button(root, text="Pracownicy").pack()

root.mainloop()