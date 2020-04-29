run:
	python3 cog_thread.py


git:
	(cd /opt/npset; make)


fix_certs:
	sudo apt-get install ca-certificates
	sudo mkdir -p /etc/pki/tls/certs 
	sudo cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
	mkdir -p ./junkbox
