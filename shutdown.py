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
