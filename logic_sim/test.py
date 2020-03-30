import pin
import ttl_7408
import input
import switch
import connection as w
from time import sleep

u1 = ttl_7408.TTL_7408('u1')
in1 = input.Input('in1')
in2 = input.Input('in2')
sw1 = switch.Switch('sw1')
w1 = w.Connection('in1out', 'sw1a1')
w2 = w.Connection('in2out', 'u1b1')
w3 = w.Connection('sw1y1', 'u1a1')
# print(pin.pin)


in1.set('out', 1)
in2.set('out', 1)
sw1.set_state(True)

# print(pin.pin)


# u1.set('a1', 1)
# u1.set('b1', 1)
sleep(1)
print(u1.get('y1'))
print(pin.pin)
