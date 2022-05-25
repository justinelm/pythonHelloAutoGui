# import pyautogui
import pyautogui

# run shift + F10
# call position function to get position of the mouse
# Log the result
# Result: Point(x=394, y=70)

print(pyautogui.position())

# click to focus on the searchbar
pyautogui.click(394, 70)

# type hello world
pyautogui.typewrite("Hello world")

# click enter
pyautogui.typewrite(["enter"])
