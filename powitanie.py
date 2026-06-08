from tkinter import *

def uruchom_program():
    okno_powitalne.destroy()

def pokaz_okno_powitalne():
    global okno_powitalne

    okno_powitalne = Tk()
    okno_powitalne.title("Portal randkowy")
    okno_powitalne.geometry("450x200")

    Label(okno_powitalne, text="WITAJ NA PORTALU RANDKOWYM", font=("Arial", 16, "bold")).pack(pady=30)
    Label(okno_powitalne, text="Naciśnij Rozpocznij aby uruchomić aplikację").pack()
    okno_powitalne.bind("<Return>", lambda event: uruchom_program())
    Button(okno_powitalne, text="Rozpocznij", command=uruchom_program).pack(pady=20)

    okno_powitalne.mainloop()