import datetime
import serial
import struct


class GMC300eGeigerCounter:
    def __init__(self, path_to_serial: str):
        self.serial: serial.Serial = serial.Serial(path_to_serial, 57600)

    def version(self) -> str:
        """
        :return: The version of the GQ GMC unit. It includes hardware model and firmware version
        """
        self.serial.write("<GETVER>>".encode())
        return self.serial.read(14).decode("ascii")

    def cpm(self) -> int:
        """
        :return: Current CPM as integer
        """
        self.serial.write("<GETCPM>>".encode())
        cpm: int = int(struct.unpack(">H", self.serial.read(2))[0])
        return cpm

    def serial_number(self) -> bytes:
        """
        :return: The serial number of the device. It is funnily enough not encoded, meaning, you read the binary string,
            without the "slash-x".
            Example: b'\xf4\x88\xc4\x92\x04X,' => Serial Number: F488C49204582C

        Todo: This is a bit broken
        """
        self.serial.write("<GETSERIAL>>".encode())
        return self.serial.read(7)

    def power_off(self):
        """
        Power off the device. Use at your own risk
        """
        self.serial.write("<POWEROFF>>".encode())

    def power_on(self):
        """
        Power on the device. Use at your own risk
        """
        self.serial.write("<POWERON>>".encode())

    def reboot(self):
        """
        Reboot the device
        """
        self.serial.write("<REBOOT>>".encode())

    def set_datetime(self, time: datetime.datetime):
        """
        Set the realtime clock inside the device to the given time

        :param time: Datetime object of the time to set to
        :raises: AssertionError, if the setting did not succeed
        """
        raise NotImplemented("If you're interested, fix this.")
        # time_string = time.strftime("%Y%m%d%H%M%S")
        # print(time_string)
        # self.serial.write("<<SETDATETIME{}>>>>".format(time_string.lstrip("20")).encode())
        # assert self.serial.read(1) == b"\xaa"  # Check for ack by device

    def get_datetime(self) -> datetime.datetime:
        """
        I have no idea how this return the data. I get

        [b'E', b'\t', b'\x11', b'\t', b'\x1a', b'\x1d']
        for 2069-09-17 smth smth

        I expect the following from the specification:

        23. Get year date and time

        command: <GETDATETIME>>


        Return: Seven bytes data: YY MM DD HH MM SS 0xAA

        Firmware supported: GMC-280, GMC-300 Re.3.00 or later
        """
        raise NotImplemented("If you're interested, fix this.")
        # self.serial.write("<GETDATETIME>>".encode())
        # year = self.serial.read(1)
        # month = self.serial.read(1)
        # day = self.serial.read(1)
        # hour = self.serial.read(1)
        # minute = self.serial.read(1)
        # second = self.serial.read(1)
        # confirm = self.serial.read(1)
        # d = [year, month, day, hour, minute, second]
        # if not confirm == b"\xaa":
        #     print("Error")  # Todo


if __name__ == '__main__':
    gc = GMC300eGeigerCounter("/dev/ttyUSB0")
    print(gc.version())
    print(gc.cpm())
