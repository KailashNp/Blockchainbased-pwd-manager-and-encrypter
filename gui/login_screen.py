import tkinter as tk
from tkinter import messagebox
import os
import hashlib
from gui.main_window import launch_gui

HASH_FILE = "vault_hash.txt"

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def save_hash(hash_str: str):
    with open(HASH_FILE, "w") as f:
        f.write(hash_str)

def load_hash() -> str:
    if not os.path.exists(HASH_FILE):
        return None
    with open(HASH_FILE, "r") as f:
        return f.read().strip()

def open_login_screen():
    def handle_login():
        entered_password = entry.get()
        entered_hash = sha256(entered_password)
        stored_hash = load_hash()

        if stored_hash is None:
            save_hash(entered_hash)
            messagebox.showinfo("Vault Initialized", "Master password set.")
            root.destroy()
            launch_gui(entered_password)
        elif entered_hash == stored_hash:
            root.destroy()
            launch_gui(entered_password)
        else:
            messagebox.showerror("Access Denied", "Incorrect master password.")

    root = tk.Tk()
    root.title("BlockCrypt Login")
    root.geometry("350x180")

    tk.Label(root, text="Enter Master Password").pack(pady=10)
    entry = tk.Entry(root, width=30, show="*")
    entry.pack(pady=5)

    tk.Button(root, text="Login", command=handle_login).pack(pady=15)
    root.mainloop()
