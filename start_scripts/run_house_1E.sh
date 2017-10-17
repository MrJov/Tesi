#!/bin/bash  
echo "************ LAUNCHING HOUSE 1 EMPTY WORLD *********" 
# Define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H:%M:%S.%3N"
}
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=house_1_empty.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/House_1E
	mkdir ../src/log/House_1E/"$folder"
	cp -Ri ~/.gazebo/log/* ~/tesi_ws/src/log/House_1E/"$folder"
}
trap finish EXIT
