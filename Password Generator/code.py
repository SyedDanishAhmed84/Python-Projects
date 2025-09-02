import tkinter as tk
import string
import random

def password_generator():
    length=int(length_entry.get())
    characters=string.ascii_letters+string.digits
    password="".join(random.choice(characters) for _ in range(length))
    result_label.config(text="Password : "+password)

root=tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="darkblue")

label=tk.Label(root,text="Enter the password length",bg="darkblue",fg="white",font=("Poppins",10,"bold"))
label.pack(pady=5)
length_entry=tk.Entry(root)
length_entry.pack(pady=5)

button=tk.Button(root,text="Generate the Password",command=password_generator,bg="lightblue",fg="black")
button.pack(pady=10)

result_label=tk.Label(root,bg="darkblue",fg="white")
result_label.pack(pady=5)

root.mainloop()
