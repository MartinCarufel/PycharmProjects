#coding:utf-8

from subprocess import run, PIPE, Popen
import pyautogui
from time import sleep
import io

commands = ["start", "cmd", "/k", "dir"]
p = Popen(commands, shell=True, stdin=PIPE, stdout=PIPE, universal_newlines=True)
sleep(0.3)
title = pyautogui.getWindow("system32")
title.set_foreground()
print(title)
pyautogui.typewrite("allo\n")
pyautogui.typewrite("cd..\n")
processId = p.pid
print("Le process id est: {}" .format(processId))

title = pyautogui.getWindow("system32")
title.set_foreground()
pyautogui.keyDown('altleft')
pyautogui.keyDown('F4')

pyautogui.keyUp('altleft')
pyautogui.keyUp('F4')
p.kill()

#f = "some initial text data\n"
#p.stdin.write(f)

#rear, err = p.communicate(input="bonjour\n", timeout=5)


#p = subprocess.Popen(["start", "cmd", "/k"], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

#p = run(['start', 'cmd', "/k"], stdout=PIPE, input='dir')

#p.communicate(input="dir")
#p.stdin.write(dir)
#coding:utf-8

