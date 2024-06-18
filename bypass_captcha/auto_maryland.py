# import pyautogui
# print(pyautogui.position())

#Point(x=793, y=27)
#chrome Point(x=178, y=61)
#Point(x=508, y=57)
#Point(x=334, y=547)
#Point(x=369, y=576)

import pyautogui
import time

# Function to double click at a specific position
def double_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()

# Function to type text
def type_text(text):
    pyautogui.typewrite(text, interval=0.1)

# Coordinates of the Chrome icon on the desktop (you need to find these manually)
chrome_icon_x = 793  # Replace with the actual x-coordinate
chrome_icon_y = 27  # Replace with the actual y-coordinate

# Step 1: Double click the Chrome icon
double_click(chrome_icon_x, chrome_icon_y)

# Wait for Chrome to open
time.sleep(5)  # Adjust this based on your system's performance

# Step 2: Move to the URL bar (usually at the top of the screen)
pyautogui.moveTo(178, 61)  # Replace with the actual coordinates of the URL bar
pyautogui.click()

# Step 3: Type the URL
type_text('https://casesearch.courts.state.md.us/casesearch/')
pyautogui.press('enter')

#checkbox
pyautogui.moveTo(334, 547)  # Replace with the actual coordinates of the URL bar
pyautogui.click()

pyautogui.moveTo(334, 547)  # Replace with the actual coordinates of the URL bar
pyautogui.click()

#agree
pyautogui.moveTo(369, 576)  # Replace with the actual coordinates of the URL bar
pyautogui.click()

# Wait for the page to load
time.sleep(5)