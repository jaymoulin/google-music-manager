.PHONY: install clean check

test:
	make install
	twine upload -r testpypi dist/*
publish:
	make install
	twine upload dist/*
install:
	make clean
	make check
	sudo python3 setup.py sdist
check:
	python3 setup.py check --restructuredtext
build:
	mkdir -p build
dist:
	mkdir -p dist
clean: build dist
	sudo rm -Rf build/*
	sudo rm -Rf dist/*
