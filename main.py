# import pyautogui
import pyautogui

# run shift + F10
# call position function to get position of the mouse
# Log the outcome
# Result: Point(x=394, y=70)

print(pyautogui.position())

# click to focus on the searchbar
pyautogui.click(394, 70)

# type hello world
pyautogui.typewrite("Hello world")

# click enter
pyautogui.typewrite(["enter"])

# get the Google URL
# focus on the input
pyautogui.click(394, 70)

# copy
pyautogui.hotkey("ctrl", "c")

# open new tab using ctrl + t
pyautogui.hotkey("ctrl", "t")

# focus on new search bar
pyautogui.click(394, 70)

# paste the URL
pyautogui.hotkey("ctrl", "v")

# click enter
pyautogui.typewrite(["enter"])
