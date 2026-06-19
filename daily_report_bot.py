import pyautogui
import pyperclip
import webbrowser
import subprocess
import time
import os
from datetime import datetime

# ----------------------------
# CONFIGURATION
# ----------------------------

WEBSITE_URL = "https://www.artificialintelligence-news.com/"
COMMENT = "Daily status generated automatically"

pyautogui.FAILSAFE = True

# ----------------------------
# HELPER FUNCTIONS
# ----------------------------

def wait(seconds):
    time.sleep(seconds)

def type_text(text):
    pyperclip.copy(str(text))
    pyautogui.hotkey("ctrl", "v")

# ----------------------------
# GENERATE DATE/TIME & FILES
# ----------------------------

now = datetime.now()

timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
date_string = now.strftime("%Y-%m-%d")

excel_filename = f"daily_report_{date_string}.xlsx"
screenshot_filename = f"daily_report_{date_string}.png"

# Create output folder
output_folder = "reports"
os.makedirs(output_folder, exist_ok=True)

excel_path = os.path.abspath(
    os.path.join(output_folder, excel_filename)
)

screenshot_path = os.path.abspath(
    os.path.join(output_folder, screenshot_filename)
)

# ----------------------------
# OPEN WEBSITE
# ----------------------------

print("Opening browser...")

webbrowser.open(WEBSITE_URL)
#webbrowser.open("about:blank")

#wait(5)

# Focus address bar
#pyautogui.hotkey("ctrl", "l")
#wait(1)

# Type URL visibly
#pyautogui.write(WEBSITE_URL, interval=0.05)

# Press Enter
#pyautogui.press("enter")

wait(5)

# ----------------------------
# COPY DATA FROM WEBSITE
# ----------------------------

print("Copying website data...")

pyautogui.hotkey("ctrl", "a")
wait(1)

pyautogui.hotkey("ctrl", "c")
wait(2)

page_text = pyperclip.paste()

if page_text.strip():
    headline = " ".join(page_text.split())[:100]
# Get first 50 chars as headline
else:
    headline = "Website data unavailable"

print("Data Captured:", headline)

# ----------------------------
# OPEN EXCEL
# ----------------------------

print("Opening Excel...")

try:
    subprocess.Popen("start excel", shell=True)
except Exception:
    print("Could not open Excel automatically.")
    raise

wait(3)
pyautogui.hotkey("ctrl", "n")  # New workbook
wait(2)

pyautogui.press("enter")  # focus sheet
pyautogui.press("enter")  # confirm new sheet

#wait(10)
#input("Is a blank Excel workbook open? Press Enter to continue...")

# ----------------------------
# ENTER DATA
# ----------------------------

print("Entering data into Excel...")
headers = [
    "Date & Time",
    "Website Data",
    "Comment"
]

# Row 1
for header in headers:
    type_text(header)
    wait(1)
    pyautogui.press("tab")

# Move to Row 2, Column A
pyautogui.press("enter")
pyautogui.press("home")

# Row 2
data_row = [
    timestamp,
    headline,
    COMMENT
]

for value in data_row:
    type_text(value)
    wait(2)
    pyautogui.press("tab")

wait(2)

# ----------------------------
# SAVE EXCEL FILE
# ----------------------------

print("Saving workbook...")

pyautogui.hotkey("ctrl", "s")

wait(5)

type_text(excel_filename)

wait(2)

pyautogui.press("enter")

wait(3)


# ----------------------------
# TAKE SCREENSHOT
# ----------------------------

print("Taking screenshot...")

screenshot = pyautogui.screenshot()

screenshot.save(screenshot_path)
print("Closing Excel...")
pyautogui.hotkey("alt", "f4")
wait(2)
print("Switching back to VS code...")
pyautogui.hotkey("alt", "tab")
# ----------------------------
# COMPLETE
# ----------------------------

print("\n===== REPORT GENERATED =====")
print("Excel File :", excel_path)
print("Screenshot :", screenshot_path)
print("============================")
print("Automation Process completed successfully.")