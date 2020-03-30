# coding: utf-8
from time import sleep
import switch_2
import input
import connection_2
import ttl_7408

sw1 = switch_2.Switch()
in1 = input.Input()
in2 = input.Input()
u1 = ttl_7408.TTL_7408()
in1.set('out', 1)
in2.set('out', 1)
w1 = connection_2.Connection(in1.get('out'), sw1, 'a1')
w2 = connection_2.Connection(sw1.get('y1'), u1, 'a1')
w3 = connection_2.Connection(in2.get('out'), u1, 'b1')


print(sw1.get('y1'))
sw1.set_state(True)
sleep(.3)
print('sw1 y1: %s' %(sw1.get('y1')))
print('u1 a1: %s, b1: %s' %(u1.get('a1'), u1.get('b1')))
print('u1 y1: %s' %(u1.get('y1')))

