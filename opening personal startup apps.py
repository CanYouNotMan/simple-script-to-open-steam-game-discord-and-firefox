#code to turn on steam, dc, and firefox
import os
import pyautogui
import time

print("Starting script...")

# Move the mouse to open Forza Horizon 4
print("Opening Forza Horizon 4...")
pyautogui.click(200, 50)
pyautogui.click(200, 50)
time.sleep(53)

# Start up the menu
print("Pressing enter to start the menu...")
pyautogui.press('enter')
time.sleep(8)
print ("pressing enter to load in my save profile")
pyautogui.press('enter')

# Open Firefox


print("Opening Firefox...")
os.startfile(r"C:\Users\nickh\AppData\Local\Mozilla Firefox\firefox.exe")
time.sleep(5)

# Open Discord
print("Opening Discord...")
os.startfile(r"C:\Users\nickh\OneDrive\Desktop\Discord.lnk")
time.sleep(5)

print("Script finished.")








