build:
	$(MAKE) local-server
	$(MAKE) prod-server
	$(MAKE) test-server
	$(MAKE) analytic
	$(MAKE) coverage
	$(MAKE) flake8

.PHONY: local-server
local-server:
	gunicorn core.wsgi:application


.PHONY: prod-server
prod-server:
	gunicorn core.wsgi:application --env DJANGO_SETTINGS_MODULE=core.settings.prod

.PHONY: test-server
test-server:
	gunicorn core.wsgi:application --env DJANGO_SETTINGS_MODULE=core.settings.test

.PHONY: analytic
analytic:
	pylint -d C0301 partenaire/*.py --disable=inconsistent-return-statements

.PHONY: tests
tests:
	python manage.py test --verbosity=2 --settings=core.settings.test

.PHONY: coverage
coverage:
	coverage run  manage.py  test --settings=core.settings.test && coverage report && coverage html 

.PHONY: flake8
flake8:
	flake8 --max-line-length=120 partenaire/*.py 
