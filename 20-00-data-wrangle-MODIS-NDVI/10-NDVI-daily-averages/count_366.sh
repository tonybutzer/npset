#! /bin/bash

for year in {2001..2018};  do {
	echo $year
	aws s3 ls --recur dev-et-data/t50n-90e/$year |wc 
} done
