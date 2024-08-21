import webbrowser
import pyautogui as py
import time

# Open the link
link = "https://fantasy.premierleague.com/squad-selection"
webbrowser.open(link)

# Helper function to perform repetitive click actions
def perform_click_sequence(positions):
    for pos in positions:
        py.moveTo(x=pos[0], y=pos[1], duration=1)
        py.click()
        py.moveTo(x=940, y=550, duration=1)
        py.click()
    time.sleep(1)

# Select Forward
def select_forward():
    Forward = 'Forward.png'
    location1 = py.locateCenterOnScreen(Forward)
    if location1:
        py.moveTo(location1, duration=1)
        py.click()
    perform_click_sequence([(1415, 300), (1415, 330), (1415, 375)])
    print("Finished selecting forwards")

# Select Midfielder
def select_midfielder():
    py.moveTo(x=780, y=635, duration=1)
    py.click()
    perform_click_sequence([(1415, 280), (1415, 330), (1415, 375), (1415, 415), (1415, 460)])
    print("Finished selecting midfielders")

# Select Defender
def select_defender():
    py.moveTo(x=780, y=440, duration=1)
    py.click()
    perform_click_sequence([(1415, 280), (1415, 330), (1415, 375), (1415, 415), (1415, 460)])
    print("Finished selecting defenders")

# Select Keeper
def select_keeper():
    py.moveTo(x=900, y=260, duration=1)
    py.click()
    perform_click_sequence([(1415, 280), (1415, 330)])
    print("Finished selecting keeper")

# Final clicks and scrolling
py.moveTo(x=1385, y=807, duration=1)
py.click()

time.sleep(1)
py.moveTo(x=1442, y=406, duration=1)
py.click()

py.scroll(-700)

# Run the selection functions
select_forward()
select_midfielder()
select_defender()
select_keeper()
