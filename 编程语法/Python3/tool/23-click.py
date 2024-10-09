import pyautogui
import pyperclip
# import sublime
# import sublime_plugin

xx=int(input('x='))
for i in range(29):
    click_point=(xx,90+i*33)
    pyautogui.click(x=click_point[0], y=click_point[1], duration=0.1)
    pyautogui.hotkey('space')