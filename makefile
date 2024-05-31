COMMIT_MSG_HOOK = '\#!/bin/bash\nMSG_FILE=$$1\ncz check --allow-abort --commit-msg-file $$MSG_FILE'

install-uv:
	pip install --upgrade pip
	pip install --upgrade uv

requirements.txt: requirements.in install-uv
	uv pip compile --upgrade requirements.in -o $@

install: requirements.txt
	uv pip install -r requirements.txt
	pre-commit install
	echo $(COMMIT_MSG_HOOK) > .git/hooks/commit-msg
	chmod +x .git/hooks/commit-msg
