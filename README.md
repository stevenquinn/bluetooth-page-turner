 # Bluetooth Page Turner

This is the code for my bluetooth page turner project, which is intended to be used with the [ForScore](https://apps.apple.com/us/app/forscore/id363738376) app on my iPad. This project uses an Adafruit ItsyBitsy BLE board, their backpack for allowing it to be powered by a lipo battery, and a couple of buttons.


# Hardware setup

I've got the buttons connected to `board.D7` and `board.D9` on my project, but it can be to any of the digital IO pins on the board. This is also configurable in the main PageTurner class.

# Software setup

1. Clone this repo
2. Copy all files over to your CircuitPython board
3. It should immediately begin advertising as a BLE when it gets power. It'll show up as something like `CIRCUITPY855`. You can connect to it using your phone/tablet's bluetooth settings. 
4. Once connected, the two buttons will function as a bluetooth keyboard sending the arrow left or arrow right keys to the device.