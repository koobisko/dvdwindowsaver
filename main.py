import time
import pygetwindow as gw
import win32gui
from screeninfo import get_monitors
win = gw.getActiveWindow()

if win is not None:
    move = [1, 1]
    screen = get_monitors()[0]
    sw,sh = screen.width, screen.height

    while True:
        win = gw.getActiveWindow()
        
        if win is not None:
            left, top, right, bottom = win.left, win.top, win.right, win.bottom
            
            if left <= 0 or right >= sw:
                move[0] = move[0] * -1
            if top <= 0 or bottom >= sh:
                move[1] = move[1] * -1
                       
            new_left = left + move[0] * 10
            new_top = top + move[1] * 10
            
            win32gui.MoveWindow(win._hWnd, new_left, new_top, right - left, bottom - top, True)

        time.sleep(0.03)        

