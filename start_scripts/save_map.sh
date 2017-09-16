#!/bin/bash  
echo "************ SAVING MAP *********"
# Define a timestamp function
timestamp() {
	date +"%Y-%m-%d_%H:%M:%S.%3N"
}
folder="$(timestamp)"
echo $folder
mkdir ../src/log/"$1"
mkdir ../src/log/"$1"/"$folder"
rosrun map_server map_saver -f /home/jov/tesi_ws/src/log/"$1"/"$folder"/"$1"
