import os
import time
import logging
from pynput import mouse, keyboard
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Set up the folder to monitor
MONITOR_FOLDER = r'C:\Users\user\Desktop\Task 3'

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f'Suspicious activity detected: New file created - {event.src_path}')
        print(f'Suspicious activity detected: New file created - {event.src_path}')

    def on_moved(self, event):
        logging.info(f'Suspicious activity detected: File moved - {event.src_path} to {event.dest_path}')
        print(f'Suspicious activity detected: File moved - {event.src_path} to {event.dest_path}')

# Set up the mouse and keyboard listeners
def on_move(x, y):
    logging.info(f'Mouse moved to ({x}, {y})')
    print(f'Mouse moved to ({x}, {y})')

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f'Mouse button {button} pressed at ({x}, {y})')
        print(f'Mouse button {button} pressed at ({x}, {y})')
    else:
        logging.info(f'Mouse button {button} released at ({x}, {y})')
        print(f'Mouse button {button} released at ({x}, {y})')

def on_scroll(x, y, dx, dy):
    logging.info(f'Mouse scrolled at ({x}, {y}) with ({dx}, {dy})')
    print(f'Mouse scrolled at ({x}, {y}) with ({dx}, {dy})')

def on_press(key):
    logging.info(f'Key pressed: {key}')
    print(f'Key pressed: {key}')

def on_release(key):
    logging.info(f'Key released: {key}')
    print(f'Key released: {key}')

mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listeners
mouse_listener.start()
keyboard_listener.start()

# Set up the file system event handler
observer = Observer()
observer.schedule(MyHandler(), MONITOR_FOLDER, recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    # Stop the listeners
    mouse_listener.stop()
    keyboard_listener.stop()
    
    # Stop the observer
    observer.stop()
    observer.join()

    # Read the log file content
    with open('log.txt', 'r') as log_file:
        log_data = log_file.read()

    # Save the data into a new file
    with open('final_log.txt', 'w') as final_log_file:
        final_log_file.write(log_data)

    print('Monitoring completed and data saved to final_log.txt')
