Image='tbutzer/cogxfer'

build:
	docker build --tag ${Image} .

publish: ## Send this image to docker hub!
	sudo docker login -u tbutzer
	sudo docker push ${Image}


run:
	docker run -it tbutzer/cogxfer python3 cogxfer.py


git:
	(cd /opt/npset; make)
