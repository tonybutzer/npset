Image='tbutzer/cogxfer'

build:
	docker build --tag ${Image} .

publish: ## Send this image to docker hub!
	sudo docker login -u tbutzer
	sudo docker push ${Image}


run:
	docker run -it -v `pwd`/junk:/opt/run/junkbox tbutzer/cogxfer python3 cogxfer.py

exec:
	docker run -it tbutzer/cogxfer bash

test:
	docker run -it tbutzer/cogxfer rio info /vsis3/ga-et-data/NDVI_filled/2001/2001001.250_m_NDVI.tif | python -m json.tool


git:
	(cd /opt/npset; make)
