name:
	@echo $(shell basename $(PWD))

env:
	@virtualenv -p python3 env

.PHONY: name env
