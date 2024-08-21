import pyautogui as py
import time
import webbrowser

# Get the link from the user
link = input("Enter the link you want: ")

# Open the link in the web browser
webbrowser.open(link)
time.sleep(2)  # Wait for the browser to open

# Move and click the first target
py.moveTo(x=1341, y=876, duration=1)
py.click()

# Perform the repeated actions
NumberOfShorts=100
for _ in range(NumberOfShorts):
    py.moveTo(x=537, y=441, duration=1)
    py.click()
    py.moveTo(x=64, y=653, duration=1)
    py.click()


