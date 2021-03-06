#!/bin/bash  
echo "************ LAUNCHING OFFICE 1 EMPTY WORLD *********" 
# Define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H:%M:%S.%3N"
}
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=office_1_empty.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/Office_1E
	mkdir ../src/log/Office_1E/"$folder"
	cp -Ri ~/.gazebo/log/* ~/tesi_ws/src/log/Office_1E/"$folder"
}
trap finish EXIT
