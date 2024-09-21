
# KeyLogger

KeyLogger is a Python-based tool that logs all keystrokes on a system and stores them in a text file. It captures keystrokes, including special keys, and helps in tracking user input on the machine.

### s4f3s4f4r1 
Developer of this keylogger tool.
## Overview

This KeyLogger runs in the background and logs every key pressed on the keyboard, including special keys (like Shift, Ctrl, etc.). The logged data is saved to a file for later analysis.

## Features

- **Keystroke Logging**: Captures all user inputs, including alphabets, numbers, and special keys.
- **Logs Special Keys**: Logs when keys like Shift, Ctrl, etc., are pressed.
- **File Output**: Saves keystrokes in a `key_log.txt` file for review.

## How to Use

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd Task04_Key_Logger
    ```

3. Run the KeyLogger script with `python3`:

    ```bash
    python3 Task_04_KeyLogger.py
    ```

4. The KeyLogger will start running in the background, capturing all keystrokes.

5. To view the logged keys, open the `key_log.txt` file in the same directory:

    ```plaintext
    [Key.ctrl] c [Key.shift_r] Nonehello keyloger [Key.shift_r] None [Key.shift_r] None
    ```

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your machine.
- **pynput Library**: Install the required library using:

    ```bash
    pip install pynput
    ```

## Sample Output

The logged keystrokes are saved in `key_log.txt`. Below is an example of the content:

```plaintext
[Key.ctrl] c [Key.shift_r] Nonehello keyloger [Key.shift_r] None [Key.shift_r] None
