clean:
	rm -rf venv

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

main-net-restart:
	ansible-playbook ansible/bitdust_refresh.yml -i ansible/inventory/main -e "application_name=main"

main-net-config-update:
	ansible-playbook ansible/telegraf.yml -i ansible/inventory/main -K -e "application_name=main"

build-pypi: venv
	@./pypi/pypi_build.sh

release-prepare:
	@./cicd/release_prepare

release-start:
	@./cicd/release_start
