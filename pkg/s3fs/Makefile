install:
	sudo apt-get update
	sudo apt-get install awscli
	sudo apt-get install automake autotools-dev fuse g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
	# git clone https://github.com/s3fs-fuse/s3fs-fuse.git
	(cd s3fs-fuse;  \
	./autogen.sh; \
	./configure; \
	make; \
	sudo make install)
	which s3fs
	echo s3fs-fuse >> .gitignore
