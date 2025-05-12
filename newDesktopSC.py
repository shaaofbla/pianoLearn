import os
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

def create_shortcut():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    # Define filename and content of the .desktop file
    desktop = Path.home() / "Desktop"
    desktop.mkdir(parents=True, exist_ok=True)
    shortcut_path = desktop / "WebShortcut.desktop"
    
    desktop_entry = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=Web Shortcut
Exec=firefox "{url}"
Icon=firefox
Terminal=false
"""

    try:
        with open(shortcut_path, "w") as f:
            f.write(desktop_entry)
        os.chmod(shortcut_path, 0o755)
        messagebox.showinfo("Success", f"Shortcut created:\n{shortcut_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not create shortcut:\n{e}")

# Build GUI
root = tk.Tk()
root.title("Website Shortcut Creator")
root.geometry("400x100")

tk.Label(root, text="Enter website URL:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
tk.Button(root, text="Create Shortcut", command=create_shortcut).pack(pady=5)

root.mainloop()
