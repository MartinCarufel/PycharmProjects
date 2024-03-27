import sys
import unittest
from unittest import main
import sys
sys.path.append(r"D:\user_data\Martin\OneDrive\Documents\git\PycharmProjects\logic_sim")
from time import sleep, time_ns
import SN7404
import SN7408

from wire import Wire
from switch import Switch_SPDT, Push_SPNO
from updater import Updater
from bus import Bus

class Testsuite(unittest.TestCase):

    def setUp(self):
        self.updater = Updater()
    def tearDown(self):
        self.updater.stop_updater()
    def test_wire_same_type(self):
        u1 = SN7404.Sn_7404('U1')
        u2 = SN7408.Sn_7408('U2')
        w1 = Wire('w1', [u1, 1, u2, 1])
        self.assertEqual(0, w1.status, "The wire status is not fail (0)")

    def test_wire_diff_type(self):
        u1 = SN7404.Sn_7404('U1')
        u2 = SN7408.Sn_7408('U2')
        w1 = Wire('w1', [u1, 2, u2, 1])
        self.assertEqual(1, w1.status, "The wire status is not PASS (1)")

    def test_sequence_1(self):
        u1 = SN7404.Sn_7404('U1')    # Default input is 0, out is 1
        self.updater.add_device(u1)
        u2 = SN7408.Sn_7408('U2')     # default both input is 0 both connected to invert so both in = 1 out =1
        self.updater.add_device(u2)
        w1 = Wire('w1', [u1, 2, u2, 1])
        self.updater.add_device(w1)
        w2 = Wire('w1', [u1, 4, u2, 2])
        self.updater.add_device(w2)
        self.updater.start_update()
        sleep(1)
        with self.subTest(msg='Test initial state'):
            self.assertEqual(1, u2.get_pin_state(3), f'FAIL output of {u2.name} is {u2.get_pin_state(3)} but shall be 1')
        u1.set_pin_state(1, 1)
        sleep(1)
        with self.subTest(msg='Test after pin change'):
            self.assertEqual(0, u2.get_pin_state(3), f'FAIL output of {u2.name} is {u2.get_pin_state(3)} but shall be 0')

    def test_swtich_SPDT_1(self):
        sw1 = Switch_SPDT('SW1', ['IN', 'ouT', 'In'], 1)
        self.updater.add_device(sw1)
        self.updater.start_update()
        sw1.set_pin_state(1, 0)
        sw1.set_pin_state(3, 1)
        sw1.switch_pos(1)
        # print('Sw1 pin 1 = {} and pin 3 == {}'.format(sw1.get_pin_state(1), sw1.get_pin_state(3)))
        print(sw1.get_pin_state(2))
        with self.subTest('Switch at position 1'):
            self.assertEqual(0, sw1.get_pin_state(2))

        sw1.switch_pos(2)
        sleep(0.1)
        with self.subTest('Switch at position 2'):
            self.assertEqual(1, sw1.get_pin_state(2))
        print(sw1.get_pin_state(2))

    def test_push_button_1(self):
        # updater = Updater()
        b1 = Bus('Vcc', 1)
        # print('Bus VCC logic value = {}'.format(b1.pin[1]['state']))
        sw1 = Push_SPNO('SW1', 'down')
        self.updater.add_device(sw1)
        wr1 = Wire('wr1', [b1, 1, sw1, 1])
        self.updater.add_device(wr1)
        self.updater.start_update()
        prev_time_ms = 0
        activate_push = 0
        stop = round(time_ns() / 1000000) + 10000
        push_time = round(time_ns() / 1000000)
        print("")
        while True:
            current_time_ms = round(time_ns() / 1000000)
            if current_time_ms >= prev_time_ms + 100:
                (sw1.get_pin_state(2))
                print('Sw1 output: {}'.format(sw1.get_pin_state(2)), end='\r')

            if current_time_ms >= push_time + 2000 and activate_push == 0:
                sw1.activate(200)
                activate_push = 1

            if current_time_ms < push_time + 2000:
                self.assertEqual(0, sw1.get_pin_state(2), "FAIL - Wrong pin state before press button")

            if push_time + 2000 <= current_time_ms < push_time + 2000 + 200:
                self.assertEqual(1, sw1.get_pin_state(2), "FAIL - Wrong pin state on press button")

            if current_time_ms >= push_time + 2000 + 250:
                self.assertEqual(0, sw1.get_pin_state(2), "FAIL - Wrong pin state when button release")

            if current_time_ms >= stop:
                self.updater.stop_updater()
                break
