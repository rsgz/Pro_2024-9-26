import pyautogui,time
import pyperclip
# import sublime
# import sublime_plugin


x,y,n=input("x y n=").split(' ')
time.sleep(3)
for i in range(int(n)):
    pyautogui.click(x=int(x), y=int(y), duration=0.1)
    pyautogui.hotkey('space')