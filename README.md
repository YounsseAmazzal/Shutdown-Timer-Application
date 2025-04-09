# 🔴 Shutdown Button

A simple app that shuts down your computer with one click. Works on Windows, Mac, and Linux.

## ✨ What it does

This tiny application provides a single button that shuts down your computer immediately when clicked.

## 🚀 How to use

1. Run `python shutdown_app.py`
2. Click the "Shutdown" button
3. Your computer will shut down

## 📋 Requirements

- Python 3
- Tkinter (included with most Python installations)

## ⚠️ Notes

- Be careful! The app shuts down immediately without confirmation
- Unsaved work will be lost
- Mac and Linux users may need to enter their password

## 💻 Code

```python
import os
import tkinter as tk
import platform

def shutdown():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("shutdown /s /t 0")
    elif system_platform == "Darwin":  # macOS
        os.system("sudo shutdown -h now")
    elif system_platform == "Linux":
        os.system("shutdown now")
    else:
        print("Unsupported OS")

# Create a Tkinter window
window = tk.Tk()
window.title("Shutdown Button")

# Create a button and link it to the shutdown function
shutdown_button = tk.Button(window, text="Shutdown", command=shutdown)
shutdown_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
```

## 🌟 Customize

- Change button text
- Add confirmation dialog
- Add restart or sleep options

## 👤 Created by

Younnse Amazzal
