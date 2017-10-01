#!/bin/bash  
echo "************ LAUNCHING OFFICE 2 EMPTY WORLD *********"
# Define a timestamp function
timestamp() {
	date +"%Y-%m-%d_%H:%M:%S.%3N"
} 
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=office_2_empty.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/Office_2E
	mkdir ../src/log/Office_2E/"$folder"
	cp -Ri ~/.gazebo/log/* ~/tesi_ws/src/log/Office_2E/"$folder"
}
trap finish EXIT
