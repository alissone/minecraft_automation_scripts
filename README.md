# minecraft_automation_scripts

Some random scripts written in Python or Bash to automate trivial and repetitive tasks on Minecraft

___

### Walking forward

To install execute **make** and to run simply replace **x** in the bash script with the distance (in blocks) you want the player to walk forward.
Depends on xdotool *(sudo apt install xdotool)*

`minecraft_walk_time_distance.py` will gather data from `minecraft_walk_time_distance.csv` and return a function to be bundled within `minecraft_walk_time_distance.c`, compiled and then executed with `minecraft_walk_time_distance.sh`
