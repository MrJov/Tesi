# Tesi v 0.7

## Install ROS
* sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
* sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
* sudo apt-get update
* sudo apt-get install ros-kinetic-desktop-full
* sudo rosdep init
* rosdep update
* echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
* source ~/.bashrc
* sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential

## Install nav2d
* sudo apt-get install ros-kinetic-nav2d

## Install other utils
* sudo apt-get install ros-kinetic-joy
* sudo apt-get install ros-kinetic-robot-state-publisher
* sudo apt-get install ros-kinetic-map-server
* sudo apt-get install ros-kinetic-ros-control ros-kinetic-ros-controllers

## Clone repository
* git clone https://github.com/MrJov/Tesi.git tesi_ws
* cd tesi_ws
* catkin_make

## Run simulations

### Launch scripts
* cd tesi_ws/start_scripts/
* ./run_[office|school]_[1|2|3|4][E|F].sh
#### In another terminal
* cd tesi_ws/start_scripts/
* ./start.sh
#### To save RVIZ map
* cd tesi_ws/start_scripts/
* ./save_map.sh [folder]

### Launch commands
* source tesi_ws/devel/setup.bash
* roslaunch p3dx nav2d.launch [world_file:=world_file_full_name]
#### In another terminal:
* rosservice call /StartMapping
* rosservice call /StartExploration

If there are problems with a bug regarding nan values reinstall gazebo7 to update it to the latest version.
