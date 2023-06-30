install:
	pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

lint:
	pylint dictionarytool/main.py

run: requirements.txt
	python3 dictionarytool/main.py $(word) $(api_key)

build: setup.py
	python3 setup.py build bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf dict_tool.egg-info

