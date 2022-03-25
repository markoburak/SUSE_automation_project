# SUSE_automation_project

Clone this repository to your own local storage.
```
git clone https://github.com/markoburak/SUSE_automation_project.git
```
In order to run this project, firstly create a virtualenv and install all libraries with the command:
```
pip install -r /path/to/requirements.txt
```
There are two implementations of the test
- Selenium with unittest
- Playwright with pytest

They work independently, it's just two options to test the flow.

To run first version A.K.A Selenium run file Selenium_e2e.py from IDE/editor or use this command:
```
python Selenium_e2e.py
```

To run second version A.K.A Playwright in headless mode, run command pytest from 'SUSE_automation_project' directory:
```
pytest
```
To run Playwright in headed mode use:
```
pytest --headed
```

