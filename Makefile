venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt


main-net-restart:
	make -C ansible refresh

