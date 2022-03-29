import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS
                        )

fastsleep = 0.5
base = 1500
p2 = p3 = p5 = p6 = p8 = p9 = p11 = p12 = p14 = p15 = p17 = p18 = 1500
p1 = p4 = p7 = 1650
p10 = p16 = p13 = 1350
change = 350
change2 = 170
change3 = change2*2
change4 = 350
change5 = 300
speed = 70
sleep = speed / 1000 + 0.1
slow = 1000
delay = 0
t = 5
hight = "normal"
Request = "base\n"
Request2 = "boop"

def Prepare():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    base = int(base)
    speed = int(speed)
    slow = int(slow)
    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18 = int(p1), int(p2), int(p3), int(
        p4), int(p5), int(p6), int(p7), int(p8), int(p9), int(p10), int(p11), int(p12), int(p13), int(p14), int(
        p15), int(p16), int(p17), int(p18)


def Reset():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    base = 1500
    speed = 500
    slow = 1000
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = p14 = p15 = p16 = p17 = p18 = 1500


def BasePosition():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    if hight == "normal":
        Prepare()
        p2 = p3 = p5 = p6 = p8 = p9 = p11 = p12 = p14 = p15 = p17 = p18 = 1500
        p1 = p4 = p7 = 1650
        p10 = p16 = p13 = 1350
        basep = f"#1P{p10}#2P{p11}#3P{p12}#5P{p3}#7P{p2}#8P{p1}#9P{p4}#10P{p5}#11P{p6}#15P{p13}#17P{p14}#18P{p15}#21P{p7}#22P{p8}#23P{p9}#29P{p16}#30P{p17}#31P{p18}T{speed}D{delay}\r\n".encode()
        ser.write(basep)
    if hight == "low":
        Prepare()
        p3 = p6 = p9 = p12 = p15 = p18 = 1500
        p2 = p5 = p8 = 1200
        p1 = p4 = p7 = 1950
        p11 = p14 = p17 = 1800
        p10 = p16 = p13 = 1050
        basep = f"#1P{p10}#2P{p11}#3P{p12}#5P{p3}#7P{p2}#8P{p1}#9P{p4}#10P{p5}#11P{p6}#15P{p13}#17P{p14}#18P{p15}#21P{p7}#22P{p8}#23P{p9}#29P{p16}#30P{p17}#31P{p18}T{speed}D{delay}\r\n".encode()
        ser.write(basep)
    if hight == "high":
        Prepare()
        p3 = p6 = p9 = p12 = p15 = p18 = 1500
        p2 = p5 = p8 = 1800
        p1 = p4 = p7 = 1350
        p11 = p14 = p17 = 1200
        p10 = p16 = p13 = 1650
        basep = f"#1P{p10}#2P{p11}#3P{p12}#5P{p3}#7P{p2}#8P{p1}#9P{p4}#10P{p5}#11P{p6}#15P{p13}#17P{p14}#18P{p15}#21P{p7}#22P{p8}#23P{p9}#29P{p16}#30P{p17}#31P{p18}T{speed}D{delay}\r\n".encode()
        ser.write(basep)





def Movement():
    movement = f"#1P{p10}#2P{p11}#3P{p12}#5P{p3}#7P{p2}#8P{p1}#9P{p4}#10P{p5}#11P{p6}#15P{p13}#17P{p14}#18P{p15}#21P{p7}#22P{p8}#23P{p9}#29P{p16}#30P{p17}#31P{p18}T{speed}D{delay}\r\n".encode()
    ser.write(movement)


def HalfUp():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
def HalfUp2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8 = p1 + change, p2 - change, p7 + change, p8 - change
    p13, p14 = p13 - change, p14 + change
    Movement()
    time.sleep(sleep)
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p4, p5 = p4 + change, p5 - change
    p10, p11, p16, p17 = p10 - change, p11 + change, p16 - change, p17 + change
    Movement()
    time.sleep(sleep)
    BasePosition()
    LineCheck()

def Dance():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
def Dance2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    time.sleep(sleep)
    Prepare()
    p1, p2, p3, p16, p17, p18 = p1 + change, p2 - change, p3 + change4, p16 - change, p17 + change, p18 + change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p16, p17 = p1 - change, p2 + change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p3, p16, p17, p18 = p1 + change, p2 - change, p3 - change4, p16 - change, p17 + change, p18 - change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p16, p17 = p1 - change, p2 + change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p12, p7, p8, p9 = p10 - change, p11 + change, p12 - change4, p7 + change, p8 - change, p9 - change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p7, p8, = p10 + change, p11 - change, p7 - change, p8 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p12, p7, p8, p9 = p10 - change, p11 + change, p12 + change4, p7 + change, p8 - change, p9 + change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p7, p8, = p10 + change, p11 - change, p7 - change, p8 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    LineCheck()


def Forward():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p7, p8, p9 = p7 + change, p8 - change, p9 - change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p7, p8 = p7 - change, p8 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p16, p17, p18 = p16 - change, p17 + change, p18 + change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p16, p17 = p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8, p13, p14, p15 = p1 + change, p2 - change, p7 + change, p8 - change, p13 - change, p14 + change, p15 + change2
    p6, p12, p18 = p6 + change2, p12 - change4, p18 - change4
    Movement()
    time.sleep(sleep)
def Forward2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p1, p2, p7, p8, p13, p14 = p1 - change, p2 + change, p7 - change, p8 + change, p13 + change, p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p15 = p3 + change4, p9 + change4, p15 - change3
    p6, p12, p18 = p6 - change3, p12 + change4, p18 + change4
    p4, p5, p10, p11, p16, p17 = p4 + change, p5 - change, p10 - change, p11 + change, p16 - change, p17 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p4, p5, p10, p11, p16, p17 = p4 - change, p5 + change, p10 + change, p11 - change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p6, p12, p18 = p6 + change3, p12 - change4, p18 - change4
    p3, p9, p15 = p3 - change4, p9 - change4, p15 + change3
    p1, p2, p7, p8, p13, p14 = p1 + change, p2 - change, p7 + change, p8 - change, p13 - change, p14 + change
    Movement()
    time.sleep(sleep)
    LineCheck()

def Back():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p1, p2, p3 = p1 + change, p2 - change, p3 + change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2 = p1 - change, p2 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p12 = p10 - change, p11 + change, p12 - change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11 = p10 + change, p11 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8, p13, p14, p15 = p1 + change, p2 - change, p7 + change, p8 - change, p13 - change, p14 + change, p15 - change2
    p6, p12, p18 = p6 - change2, p12 + change4, p18 + change4
    Movement()
    time.sleep(sleep)
def Back2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p1, p2, p7, p8, p13, p14 = p1 - change, p2 + change, p7 - change, p8 + change, p13 + change, p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p15 = p3 - change4, p9 - change4, p15 + change3
    p6, p12, p18 = p6 + change3, p12 - change4, p18 - change4
    p4, p5, p10, p11, p16, p17 = p4 + change, p5 - change, p10 - change, p11 + change, p16 - change, p17 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p4, p5, p10, p11, p16, p17 = p4 - change, p5 + change, p10 + change, p11 - change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p6, p12, p18 = p6 - change3, p12 + change4, p18 + change4
    p3, p9, p15 = p3 + change4, p9 + change4, p15 - change3
    p1, p2, p7, p8, p13, p14 = p1 + change, p2 - change, p7 + change, p8 - change, p13 - change, p14 + change
    Movement()
    time.sleep(sleep)
    LineCheck()

def TurnLeft():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8, p13, p14 = p1 + change, p2 - change, p7 + change, p8 - change, p13 - change, p14 + change
    p3, p15 = p3 + change4, p15 + change2
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8, p13, p14 = p1 - change, p2 + change, p7 - change, p8 + change, p13 + change, p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p15 = p3 - change4, p9 - change4, p15 - change3
    p4, p5, p10, p11, p16, p17 = p4 + change, p5 - change, p10 - change, p11 + change, p16 - change, p17 + change
    p6, p18 = p6 + change2, p18 + change4
    Movement()
    time.sleep(sleep)
def TurnLeft2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p4, p5, p10, p11, p16, p17 = p4 - change, p5 + change, p10 + change, p11 - change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p15 = p3 + change4, p9 + change4, p15 + change4
    p6, p12, p18 = p6 - change4, p12 - change4, p18 - change4
    p1, p2, p7, p8, p13, p14 = p1 + change, p2 - change, p7 + change, p8 - change, p13 - change, p14 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8, p13, p14 = p1 - change, p2 + change, p7 - change, p8 + change, p13 + change, p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p15 = p3 - change4, p9 - change4, p15 - change4
    p6, p12, p18 = p6 + change3, p12 + change4, p18 + change4
    p4, p5, p10, p11, p16, p17 = p4 + change, p5 - change, p10 - change, p11 + change, p16 - change, p17 + change
    Movement()
    time.sleep(sleep)
    LineCheck()


def TurnRight():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p10, p11, p16, p17, p4, p5 = p10 - change, p11 + change, p16 - change, p17 + change, p4 + change, p5 - change
    p12, p6 = p12 - change4, p6 - change2
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p16, p17, p4, p5 = p10 + change, p11 - change, p16 + change, p17 - change, p4 - change, p5 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p12, p18, p6 = p12 + change4, p18 + change4, p6 + change3
    p13, p14, p1, p2, p7, p8 = p13 - change, p14 + change, p1 + change, p2 - change, p7 + change, p8 - change
    p15, p9 = p15 - change2, p9 - change4
    Movement()
    time.sleep(sleep)
def TurnRight2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p13, p14, p1, p2, p7, p8 = p13 + change, p14 - change, p1 - change, p2 + change, p7 - change, p8 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p12, p18, p6 = p12 - change4, p18 - change4, p6 - change4
    p15, p3, p9 = p15 + change4, p3 + change4, p9 + change4
    p10, p11, p16, p17, p4, p5 = p10 - change, p11 + change, p16 - change, p17 + change, p4 + change, p5 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p16, p17, p4, p5 = p10 + change, p11 - change, p16 + change, p17 - change, p4 - change, p5 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p12, p18, p6 = p12 + change4, p18 + change4, p6 + change4
    p15, p3, p9 = p15 - change3, p3 - change4, p9 - change4
    p13, p14, p1, p2, p7, p8 = p13 - change, p14 + change, p1 + change, p2 - change, p7 + change, p8 - change
    Movement()
    time.sleep(sleep)
    LineCheck()

def FrontLegsDance():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p4, p5, p6, p13, p14, p15 = p4 + change, p5 - change, p6 - change2, p13 - change, p14 + change, p15 + change2
    Movement()
    time.sleep(sleep)
    Prepare()
    p4, p5, p13, p14 = p4 - change, p5 + change, p13 + change, p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p8, p7, p17, p16 = p8 - change5, p7 + change5, p17 + change5, p16 - change5
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p3, p10, p11, p12 = p1 - change*2.5, p2 - change*2.5, p3 - change4, p10 + change*2, p11 + change*2, p12 - change4
    Movement()
    time.sleep(sleep)
def FrontLegsDance2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p3, p12 = p3 + change4*1.5, p12 + change4*1.5
    Movement()
    time.sleep(sleep*3)
    Prepare()
    p3, p12 = p3 - change4*1.5, p12 - change4*1.5
    Movement()
    time.sleep(sleep*3)
    LineCheck()

def GoLeft():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p13, p14 = p13 - change, p14 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p14 = p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p13 = p3 - change4, p9 + change4, p13 + change
    p4, p5, p10, p11, p12, p16, p17, p18 = p4 + change, p5 - change, p10 - change, p11 + change, p12 + change4, p16 - change, p17 + change, p18 - change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p4, p5, p10, p11, p16, p17 = p4 - change, p5 + change, p10 + change, p11 - change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
def GoLeft2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p4, p12, p18 = p4 + change, p12 - change4, p18 + change4
    p1, p2, p3, p7, p8, p9, p13, p14 = p1 + change, p2 - change, p3 + change4, p7 + change, p8 - change, p9 - change4, p13 - change, p14 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p1, p2, p7, p8, p14 = p1 - change, p2 + change, p7 - change, p8 + change, p14 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p3, p9, p13 = p3 - change4, p9 + change4, p13 + change
    p4, p5, p10, p11, p12, p16, p17, p18 = p4 - change, p5 - change, p10 - change, p11 + change, p12 + change4, p16 - change, p17 + change, p18 - change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p5, p10, p11, p16, p17 = p5 + change, p10 + change, p11 - change, p16 + change, p17 - change
    Movement()
    time.sleep(sleep)
    LineCheck()

def GoRight():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    BasePosition()
    time.sleep(sleep)
    Prepare()
    p4, p5 = p4 + change, p5 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p5 = p5 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p12, p18, p4 = p12 + change4, p18 - change4, p4 - change
    p13, p14, p1, p2, p3, p7, p8, p9 = p13 - change, p14 + change, p1 + change, p2 - change, p3 - change4, p7 + change, p8 - change, p9 + change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p13, p14, p1, p2, p7, p8 = p13 + change, p14 - change, p1 - change, p2 + change, p7 - change, p8 + change
    Movement()
    time.sleep(sleep)
def GoRight2():
    global base, speed, slow, delay, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    Prepare()
    p13, p3, p9 = p13 - change, p3 + change4, p9 - change4
    p10, p11, p12, p16, p17, p18, p4, p5 = p10 - change, p11 + change, p12 - change4, p16 - change, p17 + change, p18 + change4, p4 + change, p5 - change
    Movement()
    time.sleep(sleep)
    Prepare()
    p10, p11, p16, p17, p5 = p10 + change, p11 - change, p16 + change, p17 - change, p5 + change
    Movement()
    time.sleep(sleep)
    Prepare()
    p12, p18, p4 = p12 + change4, p18 - change4, p4 - change
    p13, p14, p1, p2, p3, p7, p8, p9 = p13 + change, p14 + change, p1 + change, p2 - change, p3 - change4, p7 + change, p8 - change, p9 + change4
    Movement()
    time.sleep(sleep)
    Prepare()
    p14, p1, p2, p7, p8 = p14 - change, p1 - change, p2 + change, p7 - change, p8 + change
    Movement()
    time.sleep(sleep)
    LineCheck()




def LineCheck():
    global line, Request
    with open("Request.txt", "r") as file:
        for line in file:
            pass
        Request = line.strip("\n")
        print(line)
        file.close()

line = "boop"
while True:
    LineCheck()
    if Request == Request2:
        print("all good")
        time.sleep(0.1)
    elif Request is not Request2:
        Request2 = Request
        Request3 = Request2
        if Request3 == 'forward':
            Forward()
            LineCheck()
            while Request == 'forward':
                Forward2()
        elif Request3 == 'back':
            print(Request3)
            Back()
            LineCheck()
            while Request == 'back':
                Back2()
        elif Request3 == 'turnleft':
            print(Request3)
            TurnLeft()
            LineCheck()
            while Request == 'turnleft':
                TurnLeft2()
        elif Request3 == 'turnright':
            TurnRight()
            LineCheck()
            while Request == 'turnright':
                TurnRight2()
        elif Request3 == 'base':
            BasePosition()
        elif Request3 == 'dance':
            Dance()
            LineCheck()
            while Request == 'dance':
                Dance2()
        elif Request3 == 'halfup':
            HalfUp()
            LineCheck()
            while Request == 'halfup':
                HalfUp2()
        elif Request3 == 'frontlegsdance':
            print(Request3)
            FrontLegsDance()
            LineCheck()
            while Request == 'frontlegsdance':
                FrontLegsDance2()
        elif Request3 == 'goleft':
            print(Request3)
            GoLeft()
            LineCheck()
            while Request == 'goleft':
                GoLeft2()
        elif Request3 == 'goright':
            print(Request3)
            GoRight()
            LineCheck()
            while Request == 'goright':
                GoRight2()
        elif Request3 == 'basehigh':
            hight = "high"
        elif Request3 == 'basemiddle':
            hight = "normal"
        elif Request3 == 'baselow':
            hight = "low"
        else:
            Request3 = Request
            Request3 = float(Request3)
            if Request3 < 10000:
                s = Request3
                s = float(s)
                speed = s
                sleep = speed / 1000 + 0.1
            else:
                print("wut")
    else:
        print("No idea why")
    time.sleep(0.1)


