import time
from pynput import keyboard

def on_key_press(key):
    print("Key pressed: ", key)
    if hasattr(key, "char") and key.char == "z":
        print("Z PRESSED!")

def on_key_release(key):
    print("Key released: ", key)
    if key == keyboard.Key.shift:
        print("SHIFT KEY RELEASED!")

keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)

print("Starting the keyboard listener, will run for 5 seconds..")
keyboard_listener.start()

time.sleep(30)
print("Time's up, stopping the keyboard listener")

keyboard_listener.stop()
keyboard_listener.join()