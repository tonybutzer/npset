Image='tbutzer/cifs'

build:
	docker build --tag ${Image} .

run:
	docker run --rm -it \
		-v /data3/butzer:/data \
		--cap-add SYS_ADMIN \
		--cap-add DAC_READ_SEARCH \
		--privileged \
		--name rcloner ${Image} /bin/bash

