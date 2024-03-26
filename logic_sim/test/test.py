import unittest
from time import sleep

import SN7404
import SN7408
import wire
from updater import Updater
class Testsuite(unittest.TestCase):
    def test_wire_same_type(self):
        u1 = SN7404.Sn_7404('U1')
        u2 = SN7408.Sn_7408('U2')

        w1 = wire.Wire([u1, u1.pin[1], u2, u2.pin[1]])
        print(w1)
        self.assertEqual(w1.status, 0, "The wire status is not fail (0)")

    def test_wire_diff_type(self):
        u1 = SN7404.Sn_7404('U1')
        u2 = SN7408.Sn_7408('U2')

        w1 = wire.Wire([u1, u1.pin[2], u2, u2.pin[1]])
        print(w1)
        self.assertEqual(w1.status, 1, "The wire status is not PASS (1)")

    def test_sequence_1(self):
        updater = Updater()
        u1 = SN7404.Sn_7404('U1')
        updater.add_device(u1)
        u2 = SN7408.Sn_7408('U2')
        updater.add_device(u2)
        w1 = wire.Wire([u1, u1.pin[2], u2, u2.pin[1]])
        updater.add_device(w1)
        w2 = wire.Wire([u1, u1.pin[4], u2, u2.pin[2]])
        updater.add_device(w2)
        updater.start_update()
        sleep(1)
        print(u2.pin[3]['state'])
        u1.set_pin_state(1, 1)
        sleep(1)
        print(u2.pin[3]['state'])
        pass