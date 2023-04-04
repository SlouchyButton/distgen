PYTHON = `which python3`

all:
	@echo no build make rule yet, just '"make check"'

test-end2end:
	@cd tests/ && PYTHON=${PYTHON} ./testsuite

test-unit:
	PYTHONPATH=..:$${PYTHONPATH} ${PYTHON} -m pytest `[ ! -z ${COVERAGE} ] && echo "--cov distgen"` tests/unittests/

# Note that flake8 reports both W503 and W504 ATM :-/ so ignore W503 for now,
# which is what should be considered the right setup.
test-lint:
	flake8 distgen/ --ignore=W503 --max-line-length 99

# Check that testsuite in packaged sources work fine, too.
test-sdist-check:
	rm -rf dist
	$(PYTHON) setup.py sdist
	cd dist/ && tar xf *.tar.gz && cd distgen-*/ && $(MAKE) check PYTHON=$(PYTHON)

# Check that tarball generated by git-archive also passes the testsuite
test-git-archive-check:
	rm -rf archive && mkdir archive
	git archive --prefix distgen/ HEAD | tar -x -C archive
	cd archive/distgen && $(MAKE) check PYTHON=$(PYTHON)


check: test-unit test-end2end
