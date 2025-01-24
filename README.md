## HyperX RGB Keyboard Protocol PoC

Written in Python, simple poc showing how to control every key (color, brightness) on HyperX keyboard.

## Supported Devices

- `HyperX Alloy Origins`

## Supported platforms

- Windows
- Mac (Tested on M1)
- Linux (not tested, should work)

## Requirements

- Hidapi
- Python3

## How to install

`pip install git+https://github.com/K4CZP3R/hyperx-keyboard-rgb.git`

## Tips

- You need to create function which gets the correct device (because path changes dynamically), you can identify valid device by its interface.
- On mac (and maybe other os) you need to run it as root, otherwise device can't be opened