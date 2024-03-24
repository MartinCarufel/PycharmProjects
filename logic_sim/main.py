import pin
import input
import ttl_7408
import connection
import switch
p = pin.Pin()
sw1 = switch.Switch('sw1')
u1 = ttl_7408.TTL_7408('u1')
# w1 = connection.Connection(p, 'w1', sw1, 'sw1_out', 'u1_a1')
sw1.set_state(1)
print(p.pin)
print(p.pin['sw1_out'])
u1.set_input(a1=0)
u1.update()
print(p.pin['u1_y1'])
# print(pin.Pin()['sw1_out'])
# u1.set_input(a1=1, b1=1)
# u1.update()
# print(u1_y1)
# print(globals())