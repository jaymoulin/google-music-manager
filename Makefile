.PHONY: install clean check

test:
	cd auth && make test && cd ..
	cd downloader && make test && cd ..
	cd uploader && make test && cd ..
publish:
	cd auth && make publish && cd ..
	cd downloader && make publish && cd ..
	cd uploader && make publish && cd ..
install:
	cd auth && make install && cd ..
	cd downloader && make install && cd ..
	cd uploader && make install && cd ..
check:
	cd auth && make check && cd ..
	cd downloader && make check && cd ..
	cd uploader && make check && cd ..
build:
	cd auth && make build && cd ..
	cd downloader && make build && cd ..
	cd uploader && make build && cd ..
dist:
	cd auth && make dist && cd ..
	cd downloader && make dist && cd ..
	cd uploader && make dist && cd ..
clean: build dist
	cd auth && make clean && cd ..
	cd downloader && make clean && cd ..
	cd uploader && make clean && cd ..
