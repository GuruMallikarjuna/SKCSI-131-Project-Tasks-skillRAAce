**Keylogger**

Keylogger is a Python script designed to monitor and log various types of activities on a computer, including file system changes, mouse movements, mouse clicks, mouse scrolls, and keyboard activity. It provides a comprehensive logging mechanism to track these events for security monitoring or debugging purposes.

How It Works**

**1. File System Monitoring**

The script uses the watchdog library to monitor a specified folder (MONITOR_FOLDER) on your computer. It tracks two types of file system events:

File Creation: Whenever a new file is created within the monitored folder, the script logs a message indicating the path of the newly created file.

File Movement: If any file is moved or renamed within the monitored folder, the script logs the source path and destination path of the file movement.

**2. Mouse and Keyboard Monitoring**

The script also captures and logs mouse and keyboard events using the pynput library. It tracks the following events:

Mouse Movements: Logs the coordinates (x, y) whenever the mouse is moved.

Mouse Clicks: Logs when a mouse button (left, right, or middle) is pressed and released at specific coordinates (x, y).

Mouse Scrolls: Logs scrolling events with details about the scroll position and movement (dx, dy).

Keyboard Presses: Logs each key press with details about the key pressed.

Keyboard Releases: Logs each key release with details about the key released.

**3. Logging and Output**

All captured events are logged using Python's logging module. Each event is timestamped with the format %Y-%m-%d %H:%M:%S,%f and written to a file named log.txt in the same directory as the script.

**4. Running the Script**

To use the script:

Modify the MONITOR_FOLDER variable to point to the folder you want to monitor.

Run the script (keylogger.py).

The script will start logging events in real-time.

To stop monitoring, press Ctrl+C in the terminal.

**5. Final Log File**

Upon stopping the script, all logged events from log.txt are saved to final_log.txt. This file contains a consolidated record of all activities monitored during the session.

**Requirements**

Python 3.6 or higher

pynput library (pip install pynput)

watchdog library (pip install watchdog)
