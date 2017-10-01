#!/bin/bash  
echo "************ LAUNCHING OFFICE 3 FURNITURE WORLD *********" 
# Define a timestamp function
timestamp() {
	date +"%Y-%m-%d_%H:%M:%S.%3N"
}
source ../devel/setup.bash
rm -rf ~/.gazebo/log/*
roslaunch p3dx nav2d.launch world_file:=office_3_furniture.world
finish() {
	folder="$(timestamp)"
<<<<<<< HEAD
	mkdir ../src/log/Office_3F
=======
>>>>>>> origin
	mkdir ../src/log/Office_3F/"$folder"
	cp -Ri ~/.gazebo/log/* ./tesi_ws/src/log/Office_3F/"$folder"
}
trap finish EXIT
