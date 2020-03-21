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



mount_bucket:
	sudo mkdir -p /mnt/ga-et-data
	sudo chown ubuntu /mnt/ga-et-data
	sudo s3fs -o iam_role="tonyEC2" -o url="https://s3-us-west-2.amazonaws.com" -o endpoint=us-west-2 -o dbglevel=info -o curldbg -o allow_other -o umask=0022 -o use_cache=/tmp ga-et-data /mnt/ga-et-data


umount:
	sudo fusermount -u /mnt/ga-et-data
