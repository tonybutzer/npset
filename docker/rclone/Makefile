Image='tbutzer/rclone'

build:
	docker build --tag ${Image} .

shell:
	docker run --rm -it \
		-v /data3/butzer:/data \
		--name rcloner tbutzer/rclone /bin/bash
