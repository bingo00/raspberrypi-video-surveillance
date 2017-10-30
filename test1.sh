#!/bin/bash

if [ -f oldfiles.log ]
then 
	newfile=`ls -t *.mp4 | head -1`
	cat oldfiles.log | grep $newfile >/dev/null
	if [ $? -eq 1 ]
	then 
		echo "there is a new file: $newfile uploading"
		echo $newfile >> oldfiles.log
		result=`python oss_test.py $newfile`
		echo $result
	else 
		echo "no new files"
	fi
else
echo "hello world!"
ls -t -r > oldfiles.log
fi
