import tkinter as tk
from tkinter import messagebox

def slice_email():
    email=email_entry.get()

    if "@" in email:
        username,domain=email.split("@")
        result.set(f"Username : {username} \n Domain : {domain}")

    else:
        messagebox.showerror("Error", "Invalid email, please enter a valid email")


root=tk.Tk()
root.title("Email slicer")
root.geometry("400x250") 
root.config(bg="#48086d")

heading=tk.Label(root,text="Email slicer Project",font=("Poppins",16,"bold"),bg="#48086d", fg="white")
heading.pack(pady=10)

email_label=tk.Label(root,text="Enter your email : ",font=("Poppins",12),bg="#48086d", fg="white")
email_label.pack(pady=10)

email_entry=tk.Entry(root,width=30,font=("Arial",12))
email_entry.pack()

slice_button=tk.Button(root,text="Slice email",font=("Arial",12,"bold"),bg="#1d68ca", fg="white",command=slice_email)
slice_button.pack(pady=15)

result=tk.StringVar()
result_label=tk.Label(root,textvariable=result,font=("Poppins",12),bg="#48086d", fg="white")
result_label.pack(pady=10)

root.mainloop()