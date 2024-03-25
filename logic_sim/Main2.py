import SN7404


u1 = SN7404.Sn_7404('u1')
u1.update()
print(u1.pin[2]['state'])
u1.pin[1]['state'] = 1
u1.update()
print(u1.pin[2]['state'])
