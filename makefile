SHELL = /bin/bash

# Environment
.PHONY: setup
setup:
	python3 -m venv ~/.dev && \
	source ~/.dev/bin/activate && \
	pip3 install -r ./requirements.txt 

# remove redundant files
.PHONY: clean
clean: 
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".trash" | xargs rm -rf
	rm -f .coverage

.PHONY: run
run: 
	python3 ./myrobot.py


.PHONY: help
help:
	@echo "Commands:"
	@echo "setup    : creates a virtual environment (.dev) for the project."
	@echo "clean   : deletes all unnecessary files and executes style formatting."
	@echo "run   	: starts running the robot."
