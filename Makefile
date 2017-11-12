.PHONY: install clean

install:
	make clean
	sudo python3 setup.py sdist
	twine upload dist/*
build:
	mkdir -p build
dist:
	mkdir -p dist
clean: build dist
	sudo rm -Rf build/*
	sudo rm -Rf dist/*
