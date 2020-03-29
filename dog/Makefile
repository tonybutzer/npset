IMAGE=tbutzer/dogpng

build: ## Build the container
	sudo docker build -t $(IMAGE) .

publish: ## Send this image to docker hub!
	sudo docker login -u tbutzer
	sudo docker push $(IMAGE)

git:
	(cd /opt/npset; make)
