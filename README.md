# asilEuyuma — Auto Clicker Tool

**Created by:** Asil E.M  
**Version:** 1.0  
**Platform:** Windows 10 / 11  
**Build Type:** Standalone `.exe` (no Python required)

---

## 🧩 Overview

Your support means the world to me! If you’d like to help me continue my work, please consider 
making a donation via PayPal: https://paypal.me/essu66. Every contribution, big or small, makes a difference—thank you for being part of this journey!

**asilEuyuma** is a lightweight and reliable auto clicker and key presser tool designed for productivity, testing, and automation tasks.  
It allows users to automate mouse clicks or keyboard presses with flexible intervals, repeat options, and even random mouse movements.

The app features an easy-to-use graphical interface built with Tkinter.

---

## ⚙️ Features

- ✅ Left, Right, Middle, or Spacebar clicking  
- ✅ Adjustable click interval (hours, minutes, seconds, milliseconds)  
- ✅ Option to **double-click** automatically  
- ✅ “Repeat until stopped”, “Repeat X times”, or “Stop after Y seconds” modes  
- ✅ Random mouse movement option  
- ✅ Press additional key combinations (e.g., `Ctrl`, `Alt`, `Shift`, etc.)  
- ✅ Start/Stop using the **F6** key or on-screen buttons  
- ✅ Compact, fixed-size interface  
- ✅ Custom icon on taskbar (`gray_wave.ico`)

---

## 🖱️ How to Use

1. **Launch** the application by double-clicking `asilEuyuma.exe`.  
   (No Python installation is required.)

2. **Set your click interval:**
   - Enter values for Hours, Minutes, Seconds, and Milliseconds.

3. **Choose your click type:**
   - Left Click, Right Click, Middle Click, or Spacebar.

4. **(Optional) Enable double-clicking** by checking “Double Click”.

5. **(Optional) Add extra keys** to press together.  
   - Example: `ctrl,alt` or `shift,a`

6. **Select your repeat mode:**
   - Repeat until stopped  
   - Repeat X times  
   - Stop after Y seconds  

7. **(Optional) Enable random mouse movement** to simulate human-like behavior.

8. **Start/Stop automation:**
   - Press the **“Start (F6)”** button or the **F6 key** to begin.  
   - Press **“Stop (F6)”** or hit **F6** again to stop.  
   - When active, the Start button will turn gray (disabled), and the Stop button will become available.

---

## 💡 Notes

- To stop clicking instantly, press **F6** anytime.  
- The app runs quietly in the background (windowed mode).  
- Ensure your mouse cursor is positioned correctly before starting clicks.

---

## 🧰 Building the `.exe` (for developers)

If you wish to rebuild the program from the Python source (`asilEuyuma.py`):

1. Open Command Prompt in the source folder.
2. Run the following command:

   ```bash
   py -m PyInstaller --onefile --windowed --clean --icon="gray_wave.ico" asilEuyuma.py
   ```

3. The compiled `.exe` will appear in the `dist` folder.

---

## 🧑‍💻 Author

**Created by:** Asil E.M  
© 2025 Asil E.M. All rights reserved.
