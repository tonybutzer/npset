#! /bin/bash

for year in {2005..2018};  do {
	echo $year
	python3 json-workload-creator.py $year
	python3 play.py
} done
