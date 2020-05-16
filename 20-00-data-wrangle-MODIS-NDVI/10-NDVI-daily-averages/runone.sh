#! /bin/bash

for year in {2004..2004};  do {
	echo $year
	python3 json-workload-creator.py $year
	python3 play.py
} done
