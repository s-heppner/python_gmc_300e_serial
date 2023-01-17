# python_gmc_300e_serial

A python serial interface to a GMC 300E Plus Geiger Counter and other 
[GQ Electronics](https://www.gqelectronicsllc.com/) Geiger Counters.

It is based on the specification of the Communication Protocol by GQ Electronics "[GQ-RFC1201](https://www.gqelectronicsllc.com/download/GQ-RFC1201.txt)" and tries to implement
Python wrapper functions for the commands presented there. 

Currently, this is very limited, since I am too stupid to figure out how some of the responses are encoded.

## How to Use

- Install the package `pip3 install -e .`
- Plug in the Geiger Counter
- Check `lsusb` for the new device and remember the ID, e.g. `1a86`
- `ls -l /dev/serial/by-id` will print out something like this:

```bash
lrwxrwxrwx 1 root root 13 Jun 22 14:11 usb-1a86_USB_Serial-if00-port0 -> ../../ttyUSB0
```

- Remember the `../../ttyUSB0` part and navigate to `/dev`
- Change the owner of the serial interface to your python user: `chown sebastian:sebastian /dev/ttyUSB0`
- Run the code:

```python
import  pygmc300e

geiger_counter = pygmc300e.GMC300eGeigerCounter("/dev/ttyUSB0")
print(geiger_counter.version())
```

```bash
> GMC-300Re 4.54
```
