from time import sleep

import SN7404
import SN7408
from threading import Thread


update_chip = []
def out_update_thread():
    while True:
        for x in update_chip:
            x.update()
            # print('Update chip {}'.format(x.name))
            sleep(0.1)

update_chip = []

u1 = SN7404.Sn_7404('u1')
u1.update()
update_chip.append(u1)
tr = Thread(target=out_update_thread)
tr.start()
print(u1.pin[2]['state'])
u1.pin[1]['state'] = 1
u1.update()
print(u1.pin[2]['state'])

u2 = SN7408.Sn_7408('u2')
update_chip.append(u2)

print("\n ---- U2 pin state ----")
print(u2.pin[3]['state'])
u2.pin[1]['state'] = 1
sleep(.5)
print(u2.pin[3]['state'])
u2.pin[2]['state'] = 1
sleep(1)
print(u2.pin[3]['state'])
