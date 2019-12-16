path=`find "/tmp/" -mindepth 1 -print -quit 2>/dev/null`

scp -r $path $1@$2:/home/$1
