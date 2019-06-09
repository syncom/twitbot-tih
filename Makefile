VENV_DIR := tih_venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(PYTHON) -m pip

install: venv
	( \
	. $(VENV_DIR)/bin/activate; \
	$(PIP) install --upgrade pip setuptools wheel; \
	$(PIP) install -r requirements.txt; \
	)

venv:
	python3 -m venv $(VENV_DIR)
	ln -Tsf $(VENV_DIR)/bin/activate venv

clean:
	rm -rf $(VENV_DIR) venv

.PHONY: venv install
