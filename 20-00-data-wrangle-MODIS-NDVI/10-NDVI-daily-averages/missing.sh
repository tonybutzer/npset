#! /bin/bash
year=2004
aws s3 ls --recur dev-et-data/t50n-90e/$year |wc 

aws s3 ls --recur dev-et-data/t50n-90e/$year >junk
cat junk | awk -F "_" '{print $NF}' > junk2
sleep 1

for day in $(seq -f "%03g" 1 366) ; do {
	match=false
	for line in `cat junk2` ; do {
		if [[ $line == *$day* ]]; then
  			#echo "It's there!" $line $day
			match=true
		else
			echo "Bummer" $line $day
			match=false
		fi
		
	} done
	if ! $match ; then
		echo $line not matched
	else
		break
	fi
	#cat junk2 | grep -v $day
} done
