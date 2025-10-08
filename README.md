<h1>🧠 Keylogger Dashboard (Python + Tkinter)</h1>

A GUI-based keylogger built with Python that logs keystrokes along with active window titles and timestamps. Designed for ethical use in debugging, productivity tracking, or educational purposes.

🚀 Features
- Real-time keystroke logging
- Timestamped entries with active application name
- Scrollable Tkinter dashboard interface
- Auto-scroll to latest log entry
- Stops logging when Esc key is pressed

🛠 Tech Stack
- Python 3
- tkinter – GUI interface
- pynput – Keyboard listener
- datetime – Timestamping
- win32gui – Active window detection (Windows only)

📦 How to Run
1. Install dependencies:
   `bash
   pip install pynput pywin32
   `
2. Save the script as keylogger_dashboard.py
3. Run the script:
   `bash
   python keylogger_dashboard.py
   `

⚠ Disclaimer
This tool is intended only for ethical and educational use. Do not use it to monitor others without consent. Unauthorized use may violate privacy laws and ethical standards.

✨ Future Enhancements
- Export logs to file
- Add filtering by application
- Support for Linux/macOS (with platform-specific window detection)
