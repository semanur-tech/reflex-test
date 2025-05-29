# Reaction Time Tester with PySide6

## Description  
This project is a GUI-based reaction time tester built using **PySide6** (Qt for Python). The app prompts users to click as quickly as possible once a colored dot appears on the screen, measuring their reaction time in milliseconds. It also provides emoji-based feedback and logs results for future reference.

## Features

- **Name Input:** Personalized greeting based on the user's name.
- **Random Delay:** A dot appears after a random short delay to avoid anticipation.
- **Reaction Measurement:** Time is measured in milliseconds from dot appearance to mouse click.
- **Emoji Feedback:** Get different emojis based on your reaction speed.
- **Result Log:** View previous results in the UI and save to a local file (`sonuclar.txt`).
- **Audio Cue:** A sound is played when the dot appears.
- **Custom UI Styling:** Visually appealing interface with themed widgets.

## Installation

Make sure you have Python 3.9 or later installed.

1. Clone this repository:
```bash
git clone https://github.com/semanur-tech/reaction-time-tester.git

2. Navigate to the project directory:
cd reaction-time-tester

3.Install required dependencies:
pip install PySide6

💡 Make sure ding.wav (audio file) and ui_form.py (generated from Qt Designer .ui file) are present in the project directory.

Usage
Run the application with the following command:
python main.py

1. Enter your name.

2. Click the Start button.

3. Wait until the dot appears and click anywhere on the screen as fast as possible.

4. Your reaction time will be displayed along with a fun emoji.

5. Click Retry to take the test again.

Dependencies

- PySide6

- Python 3.9+

Notes

The ui_form.py file must be generated using Qt Designer and pyside6-uic if it's not included:

pyside6-uic form.ui -o ui_form.py

Screenshots

![sema ](reflex-test/blob/main/screenshot1.PNG)





