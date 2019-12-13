#!/bin/sh

ARGCNUM=1
if [ $# == $ARGCNUM ];then
	nc -lv $1
else
	echo "usuage: ./attacker.sh [bind_port]"
fi;
