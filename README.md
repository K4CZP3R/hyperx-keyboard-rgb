## HyperX RGB Keyboard Protocol PoC

Written in Python, It is a early proof of concept.

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

## Supported Devices

- `HyperX Alloy Origins`

## Supported platforms

- Windows
- Mac (Tested on M1)
- Linux (not tested, should work)

## Requirements

- Hidapi
- Python3

## How to run

1. _(Optional)_ Create virtual environment: `python3 -m venv venv` and activate it `source venv/bin/activate`
2. Install requirements: `pip install -r requirements.txt`
3. Run device scanner to get your keyboard hid path: `python3 device_scanner.py`

   - Example output:

```
Getting all HID devices...
...
[*] HyperX Alloy Origins by Kingston (0x951/0x16e5) (subdevices 3):
>>>> Path='DevSrvsID:4295106613' Usages=0 Interface=0
>>>> Path='DevSrvsID:4295106619' Usages=0 Interface=2
>>>> Path='DevSrvsID:4295106617' Usages=5 Interface=1
...
```

4. Copy path to clipboard _(For me the path with interface=0 works)_ (**paths will change after unplugging keyboard!**)
5. Run the example: `python example.py` and pase the path from step 4
6. You should see keys 'K', 'S', 'P' being lit in red color.

## Tips

- You need to create function which gets the correct device (because path changes dynamically), you can identify valid device by its interface.
- On mac (and maybe other os) you need to run it as root, otherwise device can't be opened

[buymecoffee]: https://www.buymeacoffee.com/k4czp3r
[buymecoffeebadge]: https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png
