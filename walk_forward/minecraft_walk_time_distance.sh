x=31 # Distance in blocks
d=$($PWD/walk_time_distance ${x}) 

xdotool keydown Ctrl
xdotool keydown w && sleep $d && xdotool keyup w
xdotool keyup Ctrl
