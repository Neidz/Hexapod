<b>Update 20.03.2022: What the hell is that code. If you want to use it then go ahead, it will work... kinda. No idea what past me was thinking writing it.</b>

<p>This is 3D printed hexapod that I build, it runs on Raspberry Pi, uses 18 servo motors for movement and is controlled from app on the phone. I started this project about year ago and didn't visit it for quite some time but I decided that it's still worth sharing because someone might want find models or code (communication between Raspberry Pi and servo control board was kinda tricky for me) useful.</p>

<h4>Here are some pictures:</h4>
<a>https://imgur.com/a/LP6Iy2R?nc=1</a>

<h4>And here are some videos</h4>
<a>https://www.youtube.com/watch?v=-9L5q-5OcWs</a>
<a>https://www.youtube.com/watch?v=_HX3u8fKZZM</a>

<h4>Main goals of this project were:</h4>
<ul>
<li>building hexapod that is running on Raspberry Pi (there are a lot of them running on arduinos but I wanted to try building one on RPi and that project was my way of learning python)</li>
<li>creating really affordable robot (most of the things used in my robot are really cheap, even 18 servo motors shouldn't be something out of reach for hobbyist</li>
</ul>

<h1>3D printed parts</h1>

<h4>If you want to print that hexapod you will have to print:</h4>
<ul>
<li>Base in 3 parts (Split_base_1.stl, Split_base_2.stl, Split_base_3.stl) or if you have large 3d printer you can connect parts in any program that allows stl manipulations and print is as one</li>
<li>Cover in 2 parts (Split_cover_1.stl, Split_cover_2.stl), the same things as with base here, if you are able then you can print it as one after connecting it in any program</li>
<li>First_part_of_the_leg.stl x3</li>
<li>First_part_of_the_leg.stl x3 after mirroring</li>
<li>Second_part_of_the_leg.stl x3</li>
<li>Second_part_of_the_leg.stl x3 after mirroring</li>
<li>Third_part_of_the_leg.stl x3</li>
<li>Third_part_of_the_leg.stl x3 after mirroring</li>
  </ul><br>
<p>You have to print all leg parts 3 times and then print them 3 more times after mirroring
I printed all the parts with PLA, 0,1mm layer height worked best for overhangs but you can probably go with 0,2mm, all parts other than cover sadly need some supports</p>

<h1>Hardware</h1>
<ul>
<li>raspberry pi of your choice (I used 3b+ here)</li>
<li>buck converter that can handle at least 10A at 6,5V for all 18 servos (I used 300W 20A buck converter from aliexpress and it worked fine)</li>
<li>suitable powerbank or next buck converter to power up raspberry pi</li>
<li>MG995 55g servo x18</li>
<li>25T M3 Metal RC Servo Arm Horn x18 (I used this one aliexpress.com/item/4000957433782.html?spm=a2g0s.9042311.0.0.adbd5c0fBZJcos)</li>
<li>at least 18 channel servo control board that is able to handle previously mentioned power (I used this 32 channel board aliexpress.com/item/32272674301.html?spm=a2g0s.9042311.0.0.27425c0f2JeqpC)</li>
<li>battery, preferably 3S, at least 2000mAhm and if you want to also power up raspberry pi from the same battery then I would go for 3000mAh+ (with 2000mAh 3S battery i was able to use hexapod for about 20 minutes while powering raspberry pi from separate powerbank)</li>
<li>cables and connectors of your choice, I wouldn't use jumper wires for main power to servo control board because they are very thin but if you are feeling spicy and like the smell of burning insulation then go ahead </li>
<li>a lot of m3 bolts and preferably m3 locknuts (vibrations cause normal nuts to slowly unscrew)</li>
</ul>
