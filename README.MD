# Selenium Classic Framework README

This repository contains automated tests for darkwebid login page using  python 3, pipenv, unittest, selenium, 'Classic framework'.

## Prerequisites

Before you can run the tests, make sure you have the following installed:

- Python 3: You can download it from the [Python website](https://www.python.org/downloads/).
- pipenv: You can install it using pip with the following command:

  ```bash
  pip install pipenv

# Installation
## Clone the repository:
-```git clone https://github.com/AlehHpro/selenium_classic_framework.git``` 
#### or
-```git clone git@github.com:AlehHpro/selenium_classic_framework.git```   

  cd selenium_classic_framework

## Install necessary packages:
-```pipenv install```

# Running Tests

### NOTE: In base_page.py file change VALID_EMAIL and VALID_PASSWORD variables to a valid values.

1. Open your terminal.

2. Navigate to the directory where your tests are located using the `cd` command. For example:

   ```bash
   cd */selenium_classic_framework/tests

3. To run the automated tests, use the following command:
   ```bash
   python -m unittest selenium_test_cf

# Test Cases
## The following selenium test cases are included:

1. Login positive/negative - test_login
2. Forgot password - test_forgot_password
3. Learn more about KaseyaOne - test_kaseya_helpdesk_display

