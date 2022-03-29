#!/bin/bash
# Install ROS package first
if [ -d /opt/ros/melodic ]; then
    echo "remove old ros folder..." 
    sudo rm -rf /opt/ros/melodic
fi
echo "install new ros package..." 
sudo unzip -o ./melodic.zip -d /opt/ros
#install the req files
cmd=""
basepath=$(cd `dirname $0`; pwd)
dir=$(ls -l $basepath |awk '/^d/ {print $NF}')
for i in $dir
do
	cd $basepath/$i
	cat ./configure | while read line
	do
		#statements
		echo $line
		if [ $line == "[deb]" ]; then
			cmd="deb"
			continue
		elif [ $line == "[python2]" ]; then
			cmd="python2"
			continue
		elif [ $line == "[python3]" ]; then
			cmd="python3"
			continue
		elif [ $line == "<START>" ] || [ $line == "<END>" ]; then
			cmd=""
			continue
		fi
		if [ $cmd == "deb" ]; then
			sudo dpkg -i $line
		elif [ $cmd == "python2" ]; then
			pip2 install --no-deps $line
		elif [ $cmd == "python3" ] ; then
			pip3 install --no-deps $line
		fi
	done
done
