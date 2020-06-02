SRC = $(wildcard nbs/*.ipynb)

all: ob_example docs

ob_example: $(SRC)
	nbdev_build_lib
	touch ob_example

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist