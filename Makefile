.PHONY: slides

default: slides

slides:
	python build-slides.py code-slides/[0-9][0-9][0-9][0-9]*.py

run: slides
	./venv/bin/twistd -n web --path=./html --port=tcp:8888

tarball: slides
	mkdir -p ./decorators
	cp slidy.css slidy.js slides.html tim_and_eric_mind_explosion-90292.gif source-code-pro-regular.ttf avatar-transparent.svg ./decorators
	tar -cf pyyyc-decorators.tar ./decorators
	gzip pyyyc-decorators.tar
