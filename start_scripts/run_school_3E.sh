#!/bin/bash  
echo "************ LAUNCHING SCHOOL 3 EMPTY WORLD *********" 
# Define a timestamp function
timestamp() {
	date +"%Y-%m-%d_%H:%M:%S.%3N"
}
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=school_3_empty.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/School_3E
	mkdir ../src/log/School_3E/"$folder"
	cp -Ri ~/.gazebo/log/* ./tesi_ws/src/log/School_3E/"$folder"
}
trap finish EXIT
