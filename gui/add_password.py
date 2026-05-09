import tkinter as tk
from tkinter import messagebox
from crypto.aes_cipher import encrypt
from blockchain.contract_interact import store_password

def open_add_window(aes_key, on_add_callback=None):
    def save():
        label = entry_label.get()
        raw_pass = entry_password.get()

        if not label or not raw_pass:
            messagebox.showerror("Input Error", "Please enter both label and password.")
            return

        try:
            encrypted = encrypt(raw_pass, aes_key)
            store_password(label, encrypted.hex())
            messagebox.showinfo("Success", "Password saved securely.")
            window.destroy()
            if on_add_callback:
                on_add_callback()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")

    window = tk.Toplevel()
    window.title("Add New Password")
    window.geometry("350x200")

    tk.Label(window, text="Label").pack(pady=5)
    entry_label = tk.Entry(window, width=40)
    entry_label.pack()

    tk.Label(window, text="Password").pack(pady=5)
    entry_password = tk.Entry(window, width=40, show="*")
    entry_password.pack()

    tk.Button(window, text="Save", command=save).pack(pady=10)
