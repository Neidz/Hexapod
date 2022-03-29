import serial
import time


class Hexapod:
    def __init__(self):
        # speed of command execution in miliseconds
        self.speed = 100
        # delay between each command in seconds, depends on the speed of command execution
        self.command_delay = self.speed / 1000 + 0.1

    def execute_command(self, command):
        # 1P doesn't mean it motor number 1, instead it's channel on servo control board that is used for motor connected to it
        # and since it's easier to connect motors to control board that way, order might be weird
        encoded_command = f"#1P{command['axis6']}#2P{command['axis5']}#3P{command['axis4']}#5P{command['axis1']}#7P{command['axis2']}#8P{command['axis3']}#9P{command['axis9']}#10P{command['axis8']}#11P{command['axis7']}#15P{command['axis12']}#17P{command['axis11']}#18P{command['axis10']}#21P{command['axis15']}#22P{command['axis14']}#23P{command['axis13']}#29P{command['axis18']}#30P{command['axis17']}#31P{command['axis16']}T{self.speed}D0\r\n".encode()
        ser.write(encoded_command)
        time.sleep(self.command_delay)


robot = Hexapod()

if __name__ == "__main__":
    ser = serial.Serial(
        "/dev/ttyACM0",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )
