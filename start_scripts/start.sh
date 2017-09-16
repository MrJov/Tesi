#!/bin/bash  
echo "************ STARTING MAPPING AND EXPLORATION *********" 
gnome-terminal -e rqt_console
gz log -d 0
gz log -d 1
rosservice call /StartMapping
sleep 60s
rosservice call /StartExploration
sleep 30s
rosservice call /StartExploration
sleep 30s
rosservice call /StartExploration
sleep 30s
rosservice call /StartExploration
