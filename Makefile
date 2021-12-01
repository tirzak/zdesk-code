init: requirements.txt
	pip3 install -r requirements.txt

test:
	nosetests

run: 
	python3 app.py