import string
import secrets
import tkinter as tk
from tkinter import messagebox
import pyperclip



def get_alphabet():
    password = ""
    chiffres = string.digits
    lettres = string.ascii_letters
    ponctuations = string.punctuation
    alphabet = chiffres + lettres + ponctuations
    password_length = int(len_entry.get())
    for x in range(password_length):
        password += secrets.choice(alphabet)
    messagebox.showinfo("Mot de passe généré", f"Votre mot de passe est : {password}")
    return password

def copy_password():
    password = get_alphabet()
    pyperclip.copy(password)


root = tk.Tk()
root.config(bg='grey')
root.title('PasswordMaker')
root.minsize(720, 480)
#root.iconbitmap('icon.ico')
frame1 = tk.Frame(root, bg='grey')
frame2 = tk.Frame(frame1, bg='grey')
frame3 = tk.Frame(root, bg='grey')
width = 500
height = 480
image = tk.PhotoImage(file="cadenas.png")
canvas = tk.Canvas(frame1, height=height, width=width, bg='grey', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()

label_len = tk.Label(frame3, text='Entrer la longeur du mot de passe souhaitez ', bg='grey', fg='white')
label_len.pack()

len_entry = tk.Entry(frame3, bg='white', fg='black')
len_entry.pack()


copy_pwd = tk.Button(frame1, text='Générer et Copier', font=('Courrier', 15), bg='grey', fg='black', padx=10, command=copy_password)
copy_pwd.pack()


frame3.pack()
frame1.pack()
frame2.pack()


root.mainloop()
