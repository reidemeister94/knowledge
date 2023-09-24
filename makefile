COMMIT_MSG_HOOK = '\#!/bin/bash\nMSG_FILE=$$1\ncz check --allow-abort --commit-msg-file $$MSG_FILE'


install-pip-tools:
	pip install --upgrade pip
	pip install --upgrade pip-tools

requirements.txt: requirements.in install-pip-tools
	pip-compile --upgrade --resolver backtracking --output-file=$@ requirements.in

install: requirements.txt
	pip install -r requirements.txt
	pre-commit install
	echo $(COMMIT_MSG_HOOK) > .git/hooks/commit-msg
	chmod +x .git/hooks/commit-msg
