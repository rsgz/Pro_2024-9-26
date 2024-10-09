from pynput import keyboard
import pyperclip,pyautogui

r"""
pip install pynput -i https://mirrors.aliyun.com/pypi/simple
pip install pyautogui -i https://mirrors.aliyun.com/pypi/simple
"""

# 定义一个全局变量来跟踪快捷键的状态
hotkey_active = False

def on_press(key):
    global hotkey_active

    try:
        # 检查是否按下了 Ctrl 和 Alt
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            hotkey_active = True
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            hotkey_active = True
        # 检查是否在 Ctrl+Alt 被按下的情况下按下了 'C'
        elif hotkey_active and key.char == 'e':
            print('Ctrl+ALt+E')
            pyautogui.hotkey('alt', 'F3')

            # pyperclip.paste()

            # 这里你可以执行其他操作，例如保存到文件等
    except AttributeError:
        pass

def on_release(key):
    global hotkey_active

    # 检查释放的键是否是 Ctrl 或 Alt
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        hotkey_active = False
    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        hotkey_active = False

# 设置键盘监听器
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()