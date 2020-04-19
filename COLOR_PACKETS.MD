#  RGB Keys Protocol

* This protocol does have 10 packets in it.
  * 1st is the instruction packet
  * 2nd-9th are the color packets



## Instruction packet

* Size: `64 bytes`
* Description: `Needs to be sent before 9 color packets`

| Index | Value | Description |
| ----- | ----- | ----------- |
| 0 | 0x04 | ? |
| 1 | 0x02 | ? |
| 2 - 63 | 0x00 | Pad out to 64 bytes |

## Color instruction

* Size: `4 bytes`

* Example: `0x08 0xaa 0xbb 0xcc`
  * `0xaa` is the red value
  * `0xbb` is the green value
  * `0xcc` is the blue value

## Color packet

* Size: `64 bytes`
* Content: `Filled with color instructions`

| Index | Value | Description       |
| ----- | ----- | ----------------- |
| 0     | 0x08  | Key color start   |
| 1     | 0-255 | Red value (Rgb)   |
| 2     | 0-255 | Green value (rGb) |
| 3     | 0-255 | Blue value (rgB)  |

At offset 4, it starts again (`0x08`) and repeats like this to the end of the packet. 

* Index where it starts is the button index (`Going from top-left to bottom-right of your keyboard keys (down-right)`)
  * Example: Color packet at `i=0` will set the color of the `ESC` key
    * Color packet at `i=4` will set the color of the `TILDA` key
    * Color packet at `i=8` will set the color of the `TAB` key

* To see offsets of `HyperX Alloy Origins` look at `config.py`