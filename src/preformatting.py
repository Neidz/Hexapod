import time
import config

# import serial

# ser = serial.Serial(
#     "/dev/ttyACM0",
#     baudrate=115200,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
# )

# limits each axis angle in command to not crash into each other
def apply_limits(command):
    for axis, value in command.items():
        if value > config.soft_stop_max:
            command[axis] = config.soft_stop_max
        elif value < config.soft_stop_min:
            command[axis] = config.soft_stop_min
    return command


# changes each angle in command to pwm which is 500 for -180 degrees and 2500 for 180 degrees
def translate_command(command):
    for axis, value in command.items():
        command[axis] = 1500 + (value / 360) * 2000
    return command


def preformat(command):
    apply_limits(command)
    translate_command(command)
    return command


# def execute_command(command):
#     # 1P doesn't mean it motor number 1, instead it's channel on servo control board that is used for motor connected to it
#     # and since it's easier to connect motors to control board that way, order might be weird
#     encoded_command = f"#1P{command['axis6']}#2P{command['axis5']}#3P{command['axis4']}#5P{command['axis1']}#7P{command['axis2']}#8P{command['axis3']}#9P{command['axis9']}#10P{command['axis8']}#11P{command['axis7']}#15P{command['axis12']}#17P{command['axis11']}#18P{command['axis10']}#21P{command['axis15']}#22P{command['axis14']}#23P{command['axis13']}#29P{command['axis18']}#30P{command['axis17']}#31P{command['axis16']}T{self.speed}D0\r\n".encode()
#     ser.write(encoded_command)
#     time.sleep(command_delay)
