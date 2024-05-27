import subprocess
from time import sleep
import pyautogui

def test():
    app_path = r"C:\WINDOWS\system32\cmd.exe"
    note_pad = r"C:\Windows\notepad.exe"
    # sp = subprocess.Popen(app_path, text=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # sp.communicate("dir")

    sp = subprocess.Popen(note_pad, text=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sleep(1)

    pyautogui.write("Allo ")
    pyautogui.keyDown("SHIFT")
    pyautogui.press(['w', 'x', 'y'], interval=0.2)
    pyautogui.keyUp("SHIFT")

    pyautogui.keyDown("altleft")
    pyautogui.keyDown("e")
    pyautogui.keyUp("altleft")
    pyautogui.keyUp("e")
    pyautogui.press("d")



def send_command_to_cmd(command):
    # Open Command Prompt
    cmd_process = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Send command to Command Prompt
    cmd_process.stdin.write(command.encode('utf-8') + b'\n')
    cmd_process.stdin.flush()

    # Get the output
    output, error = cmd_process.communicate()
    if output:
        print(output.decode('utf-8'))
    if error:
        print(error.decode('utf-8'))

# Call the function with the desired command
# send_command_to_cmd("echo Hello World")

test()
