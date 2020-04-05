up:
	docker-compose up -d
down:
	docker-compose down


redis-tune:
	sudo sysctl -w net.core.somaxconn=65535
	sudo sysctl vm.overcommit_memory=1
	sudo echo never > /sys/kernel/mm/transparent_hugepage/enabled
git:
	(cd /opt/npset; make)


fluentd-start:
	sudo systemctl start td-agent.service
