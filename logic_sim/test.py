import ttl_7408
import switch_2
import connection_2 as con
import input
from time import sleep

u1 = ttl_7408.TTL_7408()
# u2 = ttl_7408.TTL_7408()
in1 = input.Input()
in2 = input.Input()
in3 = input.Input()
in1.set('out', 1)
in2.set('out', 1)
in3.set('out', 0)
sw1 = switch_2.Switch()
# sw1.set_state(True)

# w4 = con.Connection(in1.get('out'), u1, 'a2')
# w5 = con.Connection(in3.get('out'), u1, 'b2')
# w6 = con.Connection(u1.get('y2'), u1, 'b1')


w1 = con.Connection(in1.get('out'), u1, 'a1')
w2 = con.Connection(sw1.get('y1'), u1, 'b1')
# w2 = con.Connection(1, u1, 'b1')
w3 = con.Connection(in2.get('out'), sw1, 'a1')



sleep(0.5)
#
# print('sw1 pin in: %s, out: %s' %(sw1.get('in'), sw1.get('out')))
# print('w3 pin in: %s, out: %s' %(w3.get('in'), w3.get('out')))
# print('w2 pin in: %s, out: %s' %(w2.get('in'), w2.get('out')))
#
#
# print('u1 pin a1: %s, b1: %s' %(u1.get('a1'), u1.get('b1')))
# print('u1 y1: %s' %(u1.get('y1')))
print('u1 y1: %s' %(u1.get('y1')))

