## HyperX RGB Keyboard Protocol PoC

Written in Python, It is a early proof of concept.

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]


## Supported Devices

* `HyperX Alloy Origins - confirmed by me`

## Requirements

* Cython interface to HIDAPI library: https://github.com/trezor/cython-hidapi
* Python 3

## How to run

`python simple_script.py` or `python simple_module.py`

## Configure

* If you want to test it on other device than *Alloy Origins*, then you will need to change PID and VID here: `KspHidHelper.get_interface_path_for_pidvid(0x0951, 0x16e5, 3)`

---
[buymecoffee]: https://www.buymeacoffee.com/k4czp3r
[buymecoffeebadge]: https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png
