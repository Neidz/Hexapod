# speed of command execution in miliseconds
speed = 100
# delay between each command in seconds, depends on the speed of command execution
command_delay = speed / 1000 + 0.1
# stops that prevent motors from smashing each other or trying to go further than possible
soft_stop_min = -30
soft_stop_max = 30