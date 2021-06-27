This is 3D printed hexapod that I build, it runs on Raspberry Pi, uses 18 servo motors for movement and is controlled from app on the phone. I started this project about year ago and didn't visit it for quite some time but I decided that it's still worth sharing because someone might want find models or code (communication between Raspberry Pi and servo control board was kinda tricky for me) useful. 

Main goals of this project were:
-building hexapod that is running on Raspberry Pi (there are a lot of them running on arduinos but I wanted to try building one on RPi and that project was my way of learning python)
-creating really affordable robot (most of the things used in my robot are really cheap, even 18 servo motors shouldn't be something out of reach for hobbyist)


//3D printed parts//

If you want to print that hexapod you will have to print:
-Base in 3 parts (Split_base_1.stl, Split_base_2.stl, Split_base_3.stl) or if you have large 3d printer you can connect parts in any program that allows stl manipulations and print is as one
-Cover in 2 parts (Split_cover_1.stl, Split_cover_2.stl), the same things as with base here, if you are able then you can print it as one after connecting it in any program
-First_part_of_the_leg.stl x3
-First_part_of_the_leg.stl x3 after mirroring
-Second_part_of_the_leg.stl x3
-Second_part_of_the_leg.stl x3 after mirroring
-Third_part_of_the_leg.stl x3
-Third_part_of_the_leg.stl x3 after mirroring

You have to print all leg parts 3 times and then print them 3 more times after mirroring
I printed all the parts with PLA, 0,1mm layer height worked best for overhangs but you can probably go with 0,2mm, all parts other than cover sadly need some supports

//Software//

I wrote the code in python and it's meant to be run on Raspberry Pi (i used 3b+), I'm uploading this project some time after I actually created it so the way robot is getting all the commands is quite weird but basically:
-raspberry pi runs 2 programs, one is called Hexapod_server.py and it starts requestHandler which constantly writes all requests it's getting into Requests.txt, 
after that Hexapod_final.py grabs them from the file and executes functions connected to those requests

Not the best solution but at the time this was the best things that I came up with while being absolute python noob. To send requests I also created app with Mit app inventorr (not the most elegant thing but once again it was all I could make at the time)

Setup:
-in Hexapod_server.py you have to change "Change it to your ip" in line 30 to... well, your ip
-in app you have to also pass your ip and click "Set"

//Hardware//

-raspberry pi of your choice (I used 3b+ here)
-buck converter that can handle at least 10A at 6,5V for all 18 servos (I used 300W 20A buck converter from aliexpress and it worked fine)
-suitable powerbank or next buck converter to power up raspberry pi
-MG995 55g servo x18
-25T M3 Metal RC Servo Arm Horn x18 (I used this one aliexpress.com/item/4000957433782.html?spm=a2g0s.9042311.0.0.adbd5c0fBZJcos)
-at least 18 channel servo control board that is able to handle previously mentioned power (I used this 32 channel board aliexpress.com/item/32272674301.html?spm=a2g0s.9042311.0.0.27425c0f2JeqpC)
-battery, preferably 3S, at least 2000mAhm and if you want to also power up raspberry pi from the same battery then I would go for 3000mAh+ (with 2000mAh 3S battery i was able to use hexapod for about 20 minutes while powering raspberry pi from separate powerbank)
-cables and connectors of your choice, I wouldn't use jumper wires for main power to servo control board because they are very thin but if you are feeling spicy and like the smell of burning insulation then go ahead 
-a lot of m3 bolts and preferably m3 locknuts (vibrations cause normal nuts to slowly unscrew)
