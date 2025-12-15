import pyautogui
import keyboard
import time
import threading
import random
import tkinter as tk
from tkinter import ttk
import sys
import os

# ---------- Global Variables ----------
clicking = False
button = 'left'
interval = 0.1
repeat_mode = 'until_stopped'
repeat_count = 0
stop_after_seconds = 0
random_move = False
double_click = False
additional_keys = []

# ---------- Core Functions ----------

def random_mouse_move():
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(x, y, duration=0.1)

def click_action():
    """Performs a click or keyboard press depending on user selection."""
    global button, double_click, additional_keys
    
    # Handle additional keys
    for key in additional_keys:
        keyboard.press(key)
    
    if button == 'space':
        keyboard.press('space')
        keyboard.release('space')
        if double_click:
            keyboard.press('space')
            keyboard.release('space')
    else:
        pyautogui.click(button=button, clicks=2 if double_click else 1)
    
    # Release additional keys
    for key in additional_keys:
        keyboard.release(key)

def click_loop():
    global clicking
    start_time = time.time()
    count = 0

    while clicking:
        if random_move:
            random_mouse_move()
        click_action()
        count += 1
        time.sleep(interval)

        # Stop after certain number of repeats
        if repeat_mode == 'count' and count >= repeat_count:
            clicking = False
            break

        # Stop after certain time
        if repeat_mode == 'time' and (time.time() - start_time) >= stop_after_seconds:
            clicking = False
            break

def start_clicking():
    global clicking
    if not clicking:
        clicking = True
        threading.Thread(target=click_loop, daemon=True).start()
        btn_start.config(state='disabled')
        btn_stop.config(state='normal')

def stop_clicking():
    global clicking
    clicking = False
    btn_start.config(state='normal')
    btn_stop.config(state='disabled')

def toggle():
    if clicking:
        stop_clicking()
    else:
        start_clicking()

keyboard.add_hotkey('f6', toggle)

# ---------- GUI Setup ----------

root = tk.Tk()
root.title("asilEuyuma")

# --- Icon Setup ---
def get_resource_path(filename):
    """For PyInstaller compatibility."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

icon_path = r"C:\Users\sucar\OneDrive - COMPUTACENTER\Desktop\working directory\SaadetsScripts\creating stand alone app\gray_wave.ico"
try:
    root.iconbitmap(icon_path)
except Exception:
    pass  # Ignore if icon not found

# --- Interval Settings ---
ttk.Label(root, text="Click Interval").pack(pady=5)
frame_interval = ttk.Frame(root)
frame_interval.pack()
hours = tk.IntVar(value=0)
mins = tk.IntVar(value=0)
secs = tk.IntVar(value=0)
millis = tk.IntVar(value=100)

for text, var in [("Hours", hours), ("Mins", mins), ("Secs", secs), ("Millis", millis)]:
    f = ttk.Frame(frame_interval)
    f.pack(side=tk.LEFT, padx=5)
    ttk.Label(f, text=text).pack()
    ttk.Entry(f, textvariable=var, width=5).pack()

# --- Click Options ---
ttk.Label(root, text="Click Type").pack(pady=5)
button_var = tk.StringVar(value='left')
for name, val in [("Left Click", 'left'), ("Right Click", 'right'), ("Middle Click", 'middle'), ("Spacebar", 'space')]:
    ttk.Radiobutton(root, text=name, variable=button_var, value=val).pack(anchor='w', padx=30)

# --- Double Click Option ---
double_click_var = tk.BooleanVar(value=False)
ttk.Checkbutton(root, text="Double Click", variable=double_click_var).pack(pady=5)

# --- Additional Keys ---
ttk.Label(root, text="Additional Keys (comma separated, e.g., ctrl,alt)").pack(pady=5)
additional_keys_var = tk.StringVar()
ttk.Entry(root, textvariable=additional_keys_var, width=30).pack()

# --- Repeat Settings ---
ttk.Label(root, text="Repeat Options").pack(pady=5)
repeat_mode_var = tk.StringVar(value='until_stopped')
frame_repeat = ttk.Frame(root)
frame_repeat.pack()

def update_repeat_mode():
    global repeat_mode
    repeat_mode = repeat_mode_var.get()

ttk.Radiobutton(frame_repeat, text="Repeat until stopped", variable=repeat_mode_var, value='until_stopped', command=update_repeat_mode).pack(anchor='w')
ttk.Radiobutton(frame_repeat, text="Repeat X times", variable=repeat_mode_var, value='count', command=update_repeat_mode).pack(anchor='w')
repeat_count_var = tk.IntVar(value=10)
ttk.Entry(frame_repeat, textvariable=repeat_count_var, width=6).pack()

ttk.Radiobutton(frame_repeat, text="Stop after Y seconds", variable=repeat_mode_var, value='time', command=update_repeat_mode).pack(anchor='w')
stop_after_var = tk.DoubleVar(value=10)
ttk.Entry(frame_repeat, textvariable=stop_after_var, width=6).pack()

# --- Random Move ---
random_move_var = tk.BooleanVar(value=False)
ttk.Checkbutton(root, text="Move mouse randomly", variable=random_move_var).pack(pady=5)

# --- Start / Stop Buttons ---
def start_button():
    global interval, button, repeat_count, stop_after_seconds, random_move, double_click, additional_keys
    button = button_var.get()
    total_ms = (hours.get()*3600000) + (mins.get()*60000) + (secs.get()*1000) + millis.get()
    interval = max(total_ms / 1000, 0.001)
    repeat_count = repeat_count_var.get()
    stop_after_seconds = stop_after_var.get()
    random_move = random_move_var.get()
    double_click = double_click_var.get()
    additional_keys = [key.strip() for key in additional_keys_var.get().split(",") if key.strip()]
    start_clicking()

btn_start = ttk.Button(root, text="Start (F6)", command=start_button)
btn_start.pack(pady=10)
btn_stop = ttk.Button(root, text="Stop (F6)", command=stop_clicking, state='disabled')
btn_stop.pack(pady=5)

ttk.Label(root, text="Press F6 to start/stop clicking").pack(pady=5)

# --- Fix window size ---
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.resizable(False, False)

root.mainloop()
