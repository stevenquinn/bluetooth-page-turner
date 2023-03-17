import time
import board
from digitalio import DigitalInOut, Direction, Pull

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode



class PageTurner:
    
    def __init__(self, button_1_pin, button_2_pin):
        
        self.setup_io(button_1_pin, button_2_pin)
        self.setup_ble()


    def setup_io(self, button_1_pin, button_2_pin):
        self.button_1 = DigitalInOut(button_1_pin)
        self.button_2 = DigitalInOut(button_2_pin)
        self.button_1.direction = Direction.INPUT
        self.button_2.direction = Direction.INPUT
        self.button_1.pull = Pull.UP
        self.button_2.pull = Pull.UP

    
    def setup_ble(self):
        self.hid = HIDService()
        self.advertisement = ProvideServicesAdvertisement(self.hid)
        self.advertisement.appearance = 961
        scan_response = Advertisement()
        self.ble = adafruit_ble.BLERadio()
        self.k = Keyboard(self.hid.devices)

        if not self.ble.connected:
            print("advertising")
            self.ble.start_advertising(self.advertisement, scan_response)
        else:
            print("already connected")
            print(self.ble.connections)
        

    def left_button_pressed(self):
        return self.button_1.value


    def right_button_pressed(self):
        return self.button_2.value


    def turn_page(self, direction):
        button_delay = 0.5
        keycode_to_send = Keycode.LEFT_ARROW if direction == "left" else Keycode.RIGHT_ARROW
        self.k.send(keycode_to_send)
        time.sleep(button_delay)


    def run(self):

        while True:
            while not self.ble.connected:
                pass

            while self.ble.connected:
                if self.left_button_pressed():
                    self.turn_page("left")

                if self.right_button_pressed():
                    self.turn_page("right")

            self.ble.start_advertising(self.advertisement)


page_turner = PageTurner(board.D7, board.D9)
page_turner.run()