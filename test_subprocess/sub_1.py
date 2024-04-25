import subprocess
from time import sleep

app_path = r"C:\Windows\write.exe"
app = subprocess.Popen(app_path, text=True, stdin=subprocess.PIPE)
sleep(3)
app.communicate("Salut", Timeout=1)
sleep((2))
app.communicate("Bonjour")