from tkinter import *
from tkinter import messagebox

def zaloguj():
    if entry_login.get() == "admin" and entry_haslo.get() == "1234":
        okno_logowania.destroy()
        from main import pokaz_program
        pokaz_program()
    else:
        messagebox.showerror("Błąd", "Niepoprawny login lub hasło")

# -------------------- OKNO LOGOWANIA --------------------
def pokaz_okno_logowania():
    global okno_logowania, entry_login, entry_haslo

    okno_logowania = Tk()
    okno_logowania.title("Logowanie")
    okno_logowania.geometry("300x160")

    Label(okno_logowania, text="Logowanie do systemu").grid(row=0, column=0, columnspan=2, pady=10)

    Label(okno_logowania, text="Login:").grid(row=1, column=0)
    entry_login = Entry(okno_logowania)
    entry_login.grid(row=1, column=1)

    Label(okno_logowania, text="Hasło:").grid(row=2, column=0)
    entry_haslo = Entry(okno_logowania, show="*")
    entry_haslo.grid(row=2, column=1)

    Button(okno_logowania, text="Zaloguj", command=zaloguj).grid(row=3, column=0, columnspan=2, pady=10)

    entry_login.insert(0, "admin")
    entry_haslo.insert(0, "")

    okno_logowania.mainloop()