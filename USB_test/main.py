import usb.core
import usb.util


class Usb_device:
    def __init__(self):

        print("Start")



    def find_usbdev(self, id_vendor, id_product):
        self.dev = usb.core.find(idVendor=id_vendor, idProduct=id_product)
        if self.dev  is None:
            raise ValueError('Device not found')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

dusb = Usb_device()

dusb.find_usbdev(0x0951, 0x1666)


# # was it found?
# if dev is None:
#     raise ValueError('Device not found')
