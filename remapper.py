from pynput import mouse, keyboard
keybC = keyboard.Controller()

buttonPressed = mouse.Button.x1 
newButton = keyboard.Key.end 

def on_move(x, y): 
    listener._suppress = False

def on_click(x, y, button, pressed):
    if button == buttonPressed:
        listener._suppress = True

        keybC.press(newButton)

def on_scroll(x, y, dx, dy):
    listener._suppress = False

with mouse.Listener(
        suppress=True,
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
