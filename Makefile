# define the name of the virtual environment directory
#  NAME ?= VALUE ? assign variable if ist not defined
VENV := venv # assign variable
PYTHON := python
SETTINGS := --settings 'project.settings'

.PHONY: all venv test run clean
# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)

# venv is a shortcut target
venv: $(VENV)/bin/activate


test:
	@$(PYTHON) -m unittest

serve:
	$(PYTHON) manage.py runserver $(SETTINGS)

run_migration:
	$(PYTHON) manage.py makemigrations $(SETTINGS)
	$(PYTHON) manage.py migrate $(SETTINGS)

create_superuser:
	$(PYTHON) manage.py createsuperuser $(SETTINGS) --username admin --email admin@wp.pl

run_fixtures:
	$(PYTHON) manage.py loaddata $(SETTINGS) $(shell bash -c 'read -s -p "Fixture name: " fixture; echo $$fixture')

build:
	docker-compose up --build

run_docker:
	docker-compose up

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

