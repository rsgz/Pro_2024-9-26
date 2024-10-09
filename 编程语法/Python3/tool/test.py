import win32gui,win32con
import win32process

window_handle = 1115136  # 通常窗口句柄是动态分配的，这个值只是示例
window_class_name = "TkChild"
process_id = 10684  # 进程ID对于这个任务不是必须的，除非您需要额外的验证
set_text='6666\n9999'


# 获取子窗口句柄
def findSubWindow(hwndParent, ID = None,  wndClass=None, wndText=None):
    if ID:
        itmehwnd = win32gui.GetDlgItem(hwndParent, ID)
        print (itmehwnd)
        return itmehwnd
    hwnd = win32gui.FindWindowEx(hwndParent, None, wndClass, wndText)
    if not hwnd:
        print ('%s获取失败' % wndClass)
        return False
    return hwnd

# 获取父窗口句柄
def findParentWindow(wndClass=None, wndText=None):
    hwnd = win32gui.FindWindow(wndClass, wndText)
    #print(hwnd)
    return hwnd


#输入框输入字符串
def editSetText(hwndEdit, testStr):
    #WM_SETTEXT不能用PostMessage，PostMessage参数中不能有指针。异步消息，不等待
    rst = win32gui.SendMessageTimeout(hwndEdit, win32con.WM_SETTEXT, 0, testStr, win32con.SMTO_NORMAL, 5)
    if rst[0]==1 and rst[1]==1:
        return True
    return False




window = findParentWindow(wndClass=window_class_name, wndText=None)
print(window)

if window:
    window = findParentWindow(wndClass=window_class_name, wndText=None)
    # success = editSetText(hwndEdit=window, testStr=set_text)
    # print("Window value set successfully: {}".format(success))
else:
    print("Window not found.")