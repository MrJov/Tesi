#!/bin/bash 
echo "************ LAUNCHING OFFICE 2 FURNITURE WORLD *********"
# Define a timestamp function
timestamp() {
	date +"%Y-%m-%d_%H:%M:%S.%3N"
} 
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=office_2_furniture.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/Office_2F
	mkdir ../src/log/Office_2F/"$folder"
	cp -Ri ~/.gazebo/log/* ~/tesi_ws/src/log/Office_2F/"$folder"
}
trap finish EXIT
