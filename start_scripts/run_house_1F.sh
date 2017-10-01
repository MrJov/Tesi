#!/bin/bash  
echo "************ LAUNCHING HOUSE 1 FURNITURE WORLD *********" 
# Define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H:%M:%S.%3N"
}
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=house_1_furniture.world
finish() {
	folder="$(timestamp)"
	mkdir ../src/log/House_1F
	mkdir ../src/log/House_1F/"$folder"
	cp -Ri ~/.gazebo/log/* ~/tesi_ws/src/log/House_1F/"$folder"
}
trap finish EXIT
