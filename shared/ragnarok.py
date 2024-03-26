import time

import pyautogui


def press_f1_and_left_mouse_until_timeout(timeout):
    start_time = time.time()
    while True:
        # Check if 2 hours have elapsed
        if time.time() - start_time >= timeout:
            break
        # Simulate pressing the F1 key
        pyautogui.press('f1')
        # Simulate a left mouse click
        pyautogui.click()
        # Wait for 2 seconds before the next iteration
        time.sleep(2)


# Timeout in seconds (2 hours = 2 * 60 * 60 seconds)
two_hours_in_seconds = 2 * 60 * 60

# Call the function with the timeout
press_f1_and_left_mouse_until_timeout(two_hours_in_seconds)
