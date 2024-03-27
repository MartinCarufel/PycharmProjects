from threading import Thread
from time import sleep

class Updater:
    def __init__(self):
        self.update_list = []
        self.tr = Thread(target=self._update_state)
        self._run = True

    def _update_state(self):
        while self._run:
            for x in self.update_list:
                x.update()
                # print('Update chip {}'.format(x.name))
                # sleep(0.2)

    def add_device(self, device):
        self.update_list.append(device)
        # print(self.update_list)

    def start_update(self):
        self.tr.start()

    def stop_updater(self):
        self._run = False