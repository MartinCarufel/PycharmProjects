#coding-UTF8
from enum import Enum

class dei_feat(Enum):
    temperature = 0
    timer = 1
    cycle = 2
    unlock_priority = 3
    port = 4
    delay_start = 5
    runtime = 6
    turbo = 7
    smart_lock = 8
    safe = 9




string = "10 39 20 01 02 45 12 02 01 05"

array = string.split(" ")
print (string[dei_feat.runtime.value])
