.PHONY:build
build:
	python -m pip install -e .[tests]
	pytest src/tfds 