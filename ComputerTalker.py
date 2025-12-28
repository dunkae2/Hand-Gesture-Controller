import os
import subprocess
from subprocess import call
import time
# Call the shell script
brighten_script = None
dim_script = None
with open("shellScripts/dim.applescript") as f:
    dim_script = f.read()
with open("shellScripts/brighten.applescript") as f:
    brighten_script = f.read()
# === Brightness Functions ===
def get_brightness():
    output = os.popen("brightness -l | grep brightness | awk '{print $4}'").read().strip()
    return float(output) if output else None

# def set_brightness(level):
#     level = max(0.0, min(1.0, level))
#     os.system(f"brightness {level}")

# def change_brightness(direction, step=0.1):
#     current = get_brightness()
#     if current is None:
#         print("Failed to get current brightness.")
#         return

#     if direction == "up":
#         set_brightness(current + step)
#         print(f"Increased brightness to {round(current + step, 2)}")
#     elif direction == "down":
#         set_brightness(current - step)
#         print(f"Decreased brightness to {round(current - step, 2)}")
#     else:
#         print("Invalid direction. Use 'up' or 'down'.")

# === Volume Functions ===
def get_volume():
    output = os.popen("osascript -e 'output volume of (get volume settings)'").read().strip()
    return int(output) if output else None

def set_volume(level):
    level = max(0, min(100, level))
    os.system(f"osascript -e 'set volume output volume {level}'")

def change_volume(direction, step=10):
    current = get_volume()
    if current is None:
        print("Failed to get current volume.")
        return

    if direction == "up":
        set_volume(current + step)
        print(f"Increased volume to {current + step}")
    elif direction == "down":
        set_volume(current - step)
        print(f"Decreased volume to {current - step}")
    else:
        print("Invalid direction. Use 'up' or 'down'.")

# === Command Handler ===
def command_handler(command):
    print("in command")
    if command == "brightness up":
        call(brighten_script, shell=True)
        # change_brightness("up")
    elif command == "brightness down":
        call(dim_script, shell=True)
    elif command == "volume up":
        # os.system("cliclick kp:volume-up")
        change_volume("up")
        time.sleep(0.8)
        # os.system("osascript -e set volume output volume 100")
        # os.system("""osascript -e 'tell application "System Events" to key code 72 using {shift down, control down}'""")


    elif command == "volume down":
        # os.system("cliclick kp:volume-down")
        change_volume("down")
        time.sleep(0.8)
    else:
        print("Invalid command.")

# === Run Interactive CLI ===
if __name__ == "__main__":
    while True:
        cmd = input("Command (brightness/volume up/down or 'exit'): ").strip().lower()
        if cmd == "exit":
            break
        command_handler(cmd)
