import tkinter as tk
from tkinter import messagebox
from blockchain.contract_interact import get_passwords
from crypto.aes_cipher import decrypt
from crypto.hash_util import sha256
from gui.add_password import open_add_window

class VaultApp:
    def __init__(self, root, master_password):
        self.root = root
        self.root.title("BlockCrypt Vault")
        self.root.geometry("500x400")

        self.key = sha256(master_password)

        # UI Elements
        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(pady=20)

        self.refresh_btn = tk.Button(root, text="🔄 Refresh", command=self.refresh_passwords)
        self.refresh_btn.pack(pady=5)

        self.add_btn = tk.Button(root, text="➕ Add Password", command=lambda: open_add_window(self.key, self.refresh_passwords))
        self.add_btn.pack(pady=5)

        self.refresh_passwords()

    def refresh_passwords(self):
        self.listbox.delete(0, tk.END)
        try:
            entries = get_passwords()
            for label, encrypted_hex in entries:
                try:
                    decrypted = decrypt(bytes.fromhex(encrypted_hex), self.key)
                except Exception:
                    decrypted = "❌ Decryption Failed"
                self.listbox.insert(tk.END, f"{label}: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch passwords: {str(e)}")

def launch_gui(master_key):
    root = tk.Tk()
    app = VaultApp(root, master_key)
    root.mainloop()

