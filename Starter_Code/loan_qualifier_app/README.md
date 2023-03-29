# LOAN QUALIFIER APPLICATION

This application helps:
* 1. The user to quickly scan the banks that qualify them to receive the desired loan.
* 2. Helps the banks to quickly screen their potential prospects that meet their criteria to give out a loan.

This app uses a python command line interface along with a csv file `daily_rate_sheet`, to compare and assess the user inputted information for screening.

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs


---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage

To use this application, clone the repository and run the **app.py** with:

`` python app.py ``

Upon launching please use the path `./data/daily_rate_sheet.csv` to initiate the application and then input the users requested information.

---

## Contributors

Brought to you by PShum Loan Consulting

---

## License

MIT