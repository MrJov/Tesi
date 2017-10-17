#!/bin/bash  
echo "************ LAUNCHING SCHOOL 2 EMPTY WORLD *********"
# Define a timestamp function
timestamp() {
	date +"%Y-%m-%d_%H:%M:%S.%3N"
} 
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=school_2_empty.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/School_2E/"$folder"
	cp -Ri ~/.gazebo/log/* ~/tesi_ws/src/log/School_2E/"$folder"
}
trap finish EXIT
