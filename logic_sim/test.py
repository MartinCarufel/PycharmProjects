import pin
import ttl_7408
import ttl_7432
import input
import switch
import connection as w
from time import sleep

u1 = ttl_7408.TTL_7408('u1')
u2 = ttl_7432.TTL_7432('u2')
in1 = input.Input('in1')
in2 = input.Input('in2')
in3 = input.Input('in3')
in4 = input.Input('in4')
sw1 = switch.Switch('sw1')
w1 = w.Connection('in1out', 'sw1a1')
w2 = w.Connection('in2out', 'u1b1')
w3 = w.Connection('sw1y1', 'u1a1')
w4 = w.Connection('in3out', 'u2a1')
w5 = w.Connection('in4out', 'u2b1')
# print(pin.pin)


in1.set('out', 1)
in2.set('out', 1)
in3.set('out', 1)
in4.set('out',0)
sw1.set_state(True)

# print(pin.pin)


# u1.set('a1', 1)
# u1.set('b1', 1)
sleep(1)
# print(u1.get('y1'))
print('U1 out: %s' %(pin.pin['u1y1']))
print('U2 out: %s' %(pin.pin['u2y1']))
# print(pin.pin)
