distance:
	python3 minecraft_walk_time_distance.py
	gcc -o walk_time_distance calculate_time.c minecraft_walk_time_distance.c

clean:
	rm -rf walk_time_distance calculate_time.c calculate_time.h
