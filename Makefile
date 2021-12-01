init: requirements.txt
	pip install -r requirements.txt

test:
	nosetests

run: 
	python src/app.py